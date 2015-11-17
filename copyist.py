import os
from flask import Flask, request, abort, jsonify
from goose import Goose

app = Flask(__name__)

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify(message='An error occurred, try again later.'), 500

@app.errorhandler(404)
def page_not_found(error):
    return jsonify(message='Page not found.'), 404

@app.route('/v1')
def v1():
    url = request.args.get('url', None)

    if url:
        g = Goose()
        article = g.extract(url=url.encode('utf8'))
        return jsonify(article.infos), 200
    abort(404)


if __name__ == '__main__':
    host = os.getenv('HOST', '0.0.0.0')
    port = os.getenv('PORT', 80)

    app.run(host=host, port=int(port))
    app.run()
