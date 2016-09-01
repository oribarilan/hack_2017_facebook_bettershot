from flask import request, json, Response
from app import app
from exif_extract import url_extract

@app.route('/')
@app.route('/index')
def index():
    return 'Hello World'

@app.route('/hello', methods = ['GET'])
def api_hello():
    data = {
        'hello': 'world',
        'number': 3
    }
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Link'] = 'http://somelink.com'

    return resp


@app.route('/process/src/url', methods=['POST'])
def api_process_src_url():

    url = request.form["src"]
    # url = "https://upload.wikimedia.org/wikipedia/commons/6/67/Inside_the_Batad_rice_terraces.jpg"

    exif_props = url_extract(url)

    data = {
        'props': exif_props,
        'analysis': "Wow! this is a great picture. You should consider going out more and explore the world"
    }
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Link'] = 'http://somelink.com'

    return resp
