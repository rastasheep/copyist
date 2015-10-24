import logging
import webapp2
from gose_configuration import GoseConfiguration
from webapp2_extras import json
from goose import Goose

class BaseHandler(webapp2.RequestHandler):
    def __init__(self, request, response):
        self.initialize(request, response)
        response.headers['Content-Type'] = 'application/json'

    @classmethod
    def handle_not_found(self, request, response, exception):
        response.write(json.encode({'message':'Page not found.'}))
        response.set_status(404)

    def handle_exception(self, exception, debug):
        logging.exception(exception)

        self.response.write(json.encode({'message':'Ad error occurred, try again later.'}))

        # If the exception is a HTTPException, use its error code.
        if isinstance(exception, webapp2.HTTPException):
            self.response.set_status(exception.code)
        else:
            self.response.set_status(500)

class ApiV1(BaseHandler):
    def get(self):
        url = self.request.get('url')
        g = Goose(GoseConfiguration())

        if url:
            article = g.extract(url=url)
            return self.response.write(json.encode(article.infos))

        BaseHandler.handle_not_found(self.request, self.response, None)

app = webapp2.WSGIApplication([('/v1/?$', ApiV1)], debug=True)
app.error_handlers[404] = BaseHandler.handle_not_found

def main():
    from paste import httpserver
    httpserver.serve(app, host='0.0.0.0', port='80')

if __name__ == '__main__':
    main()
