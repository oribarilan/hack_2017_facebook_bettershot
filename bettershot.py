from flask import request, json, Response
#from app import app
from exif_extract import url_extract, extract
from flask import Flask, request, send_from_directory
from imagegrader import GraderFactory
import imagga_api
import os
import uuid

from flask import Flask


from flask_cors import CORS
app = Flask(__name__, static_url_path='')
CORS(app)
#from app import views


@app.route('/<path:path>')
def root(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(os.path.join('js', path).replace("\\", "/"))


@app.route('/hello')
def hello_world():
    return 'Hello World'

#@app.route('/hello', methods = ['GET'])
#def api_hello():
#    data = {
#        'hello': 'world',
#        'number': 3
#    }
#    js = json.dumps(data)
#
#    resp = Response(js, status=200, mimetype='application/json')
#    resp.headers['Access-Control-Allow-Origin'] = '*'
#    resp.headers['Link'] = 'http://somelink.com'
#
#    return resp
#
#
@app.route('/process/src/url', methods=['POST'])
def api_process_src_url():

    url = request.form["src"]
    # url = "https://upload.wikimedia.org/wikipedia/commons/6/67/Inside_the_Batad_rice_terraces.jpg"

    exif_props = url_extract(url)
    classification = imagga_api.categorize_image(url=url)
    image_result = GraderFactory().create_factory(classification)
    grade_result = image_result.grade(exif_props)

    #data = {
    #    'props': exif_props,
    #    'analysis': "Wow! this is a great picture. You should consider going out more and explore the world"
    #}
    js = json.dumps(grade_result)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'

    return resp


@app.route('/process/src/file', methods=['POST'])
def api_process_src_file():
    file = request.files["file"]

    filename = str(uuid.uuid1()) + '.' + file.filename.split('.')[1]

    dir = os.path.dirname(__file__)
    path = os.path.join(dir + '/img_repo/', filename)

    file.save(path)

    exif_props = extract(path)
    image_id = imagga_api.imagga_upload_image(path)
    classification = imagga_api.categorize_image(content=image_id)
    image_result = GraderFactory().create_factory(classification)
    grade_result = image_result.grade(exif_props)

    js = json.dumps(grade_result)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'

    return resp
    #data = {
    #    'props': exif_props,
    #    'analysis': "Wow! this is a great picture. You should consider going out more and explore the world"
    #}
    #js = json.dumps(data)

    #resp = Response(js, status=200, mimetype='application/json')
    #resp.headers['Access-Control-Allow-Origin'] = '*'
    #resp.headers['Link'] = 'http://somelink.com'

    #return resp

app.run()