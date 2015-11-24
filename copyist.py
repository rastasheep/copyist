import os
from flask import Flask, request, abort, jsonify
from goose import Goose
from lxml.etree import tostring

app = Flask(__name__)

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify(message=error.message), 500

@app.errorhandler(404)
def page_not_found(error):
    return jsonify(message='Page not found.'), 404

@app.route('/v1')
def v1():
    url = request.args.get('url', None)
    lang = request.args.get('lang', None)

    if url:
        response = __parse_url(url.encode('utf8'), lang)
        return jsonify(response), 200
    abort(404)

def __parse_url(url, lang):
    options = {'use_meta_language': False, 'target_language':lang} if lang else {}
    g = Goose(options)

    article = g.extract(url=url)
    resp = article.infos
    resp['html'] = __raw_html(article.doc)
    resp['text'] = resp.pop('cleaned_text')
    return resp

def __raw_html(doc):
    raw_html = None
    if doc:
        raw_html = tostring(doc) if not doc.find('body') else None

    return raw_html

if __name__ == '__main__':
    host = os.getenv('HOST', '0.0.0.0')
    port = os.getenv('PORT', 80)

    app.run(host=host, port=int(port))
    app.run()
