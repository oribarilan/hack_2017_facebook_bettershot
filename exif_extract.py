import piexif
import json
from urllib import parse
import requests
import uuid
import os

UPLOAD_DIR = "uploads"


def url_extract(url):
    filename = parse.urlparse(url).path.split('/')[-1]
    file_ext = filename.split('.')[-1]
    image_uuid = str(uuid.uuid4())
    out_path = os.path.join(os.path.abspath(os.path.curdir), UPLOAD_DIR, image_uuid + "." + file_ext)
    response = requests.get(url)
    with open(out_path, 'wb') as fd:
        for chunk in response.iter_content(4096):
            fd.write(chunk)
    props = extract(out_path)
    return props


def extract(path):
    print(path)
    exif_dict = piexif.load(path)
    props = {}
    for ifd in ("0th", "Exif", "GPS", "1st"):
        for tag in exif_dict[ifd]:
            props[piexif.TAGS[ifd][tag]["name"]] = exif_dict[ifd][tag]
    return normalize_exif(filter(props))


def print_exif(props):
    print(json.dumps(props, indent=4, separators=(',', ': ')))


def clean_upload_dir():
    for filename in os.listdir(UPLOAD_DIR):
        os.remove(os.path.join(UPLOAD_DIR, filename))


def filter(props):
    filters = ["ExposureTime", "FNumber", "FocalLength", "ISOSpeedRatings"]
    filtered_dict = {k: v for k, v in props.items() if k in filters}
    return filtered_dict
    # return props


def normalize_exif(exif_data):
    exposure_time = exif_data["ExposureTime"]
    f_stop = exif_data["FNumber"]
    result = {}

    # TODO eval is EVIL!
    result["shutter_speed"] = eval(str(exposure_time[0]) + '/' + str(exposure_time[1]))
    result["f_stop"] = eval(str(f_stop[0]) + '/' + str(f_stop[1]))
    result["focal_length"] = exif_data["FocalLength"][0]
    result["iso"] = exif_data["ISOSpeedRatings"]

    return result

if __name__ == '__main__':
    # clean_img_repo()
    clean_upload_dir()
