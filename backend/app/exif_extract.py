import ntpath
import piexif
import json
import urllib.request as urllib
import uuid
import os

_img_repo_name = "./img_repo/"


def url_extract(url):
    file = urllib.URLopener()
    split_basename = ntpath.basename(url).split('.')
    extension = 'jpg'
    if len(split_basename) == 2:
        extension = split_basename[1]
    id = str(uuid.uuid1())


    dir = os.path.dirname(__file__)
    imgpath = os.path.join(dir, _img_repo_name)

    fullname = imgpath + id + "." + extension

    file.retrieve(url, fullname)
    props = extract(fullname)
    return props
    #return filter(props)


def extract(path):
    exif_dict = piexif.load(path)
    props = {}
    for ifd in ("0th", "Exif", "GPS", "1st"):
        for tag in exif_dict[ifd]:
            props[piexif.TAGS[ifd][tag]["name"]] = exif_dict[ifd][tag]
    return normalize_exif(filter(props))


def print_exif(props):
    print(json.dumps(props, indent=4, separators=(',', ': ')))


def clean_img_repo():
    file_list = [f for f in os.listdir("./" + _img_repo_name) if f.endswith(".jpg")]
    for f in file_list:
        os.remove(_img_repo_name + "/" + f)


def filter(props):
    filters = ["ExposureTime", "FNumber", "FocalLength", "ISOSpeedRatings"]
    filtered_dict = {k: v for k, v in props.items() if k in filters}
    return filtered_dict
    # return props

def normalize_exif(exif_data):
    exposure_time = exif_data["ExposureTime"]
    #exif_data["ExposureTime"] = exposure_time[0] + '/' + exposure_time[1]
    #exif_data["FNumber"] = exif_data["Fnumber"][0]
    #exif_data["FocalLength"] = exif_data["FocalLength"][0]
    #exif_data["ISOSpeedRatings"] = exif_data["ISOSpeedRatings"]
    result = {}

    # TODO eval is EVIL!
    result["shutter_speed"] = eval(str(exposure_time[0]) + '/' + str(exposure_time[1]))
    result["f_stop"] = exif_data["FNumber"][0]
    result["focal_length"] = exif_data["FocalLength"][0]
    result["iso"] = exif_data["ISOSpeedRatings"]

    return result

if __name__ == '__main__':
    # clean_img_repo()
    print_exif(url_extract("https://upload.wikimedia.org/wikipedia/commons/6/67/Inside_the_Batad_rice_terraces.jpg"))

