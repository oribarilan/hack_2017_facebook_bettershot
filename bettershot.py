import flask
from flask import Flask, request, json, Response
from exif_extract import url_extract, extract
from flask_cors import CORS
from imagegrader import GraderFactory
import imagga_api
import os
import uuid

app = Flask(__name__, static_url_path='')
CORS(app)

UPLOAD_DIR = "uploads"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/<path:path>')
def static_proxy(path):
    # send_static_file will guess the correct MIME type
    return app.send_static_file(path)


@app.route('/process/src/url', methods=['POST'])
def api_process_src_url():
    url = request.form["src"]
    exif_props = url_extract(url)
    classification = imagga_api.categorize_image(url=url)
    image_result = GraderFactory().create_factory(classification)
    grade_result = image_result.grade(exif_props)
    return flask.jsonify(grade_result)


@app.route('/process/src/file', methods=['POST'])
def api_process_src_file():
    img_file = request.files["file"]

    filename = str(uuid.uuid1()) + '.' + img_file.filename.split('.')[1]

    directory = os.path.dirname(__file__)
    path = os.path.join(directory, UPLOAD_DIR, filename)
    print(path)

    img_file.save(path)

    exif_props = extract(path)
    image_id = imagga_api.imagga_upload_image(path)
    classification = imagga_api.categorize_image(content=image_id)
    image_result = GraderFactory().create_factory(classification)
    grade_result = image_result.grade(exif_props)

    js = json.dumps(grade_result)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'

    return resp


if __name__ == "__main__":
    app.run(debug=True)
