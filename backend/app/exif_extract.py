import ntpath
import piexif
import json
import urllib
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
    return filter(props)


def extract(path):
    exif_dict = piexif.load(path)
    props = {}
    for ifd in ("0th", "Exif", "GPS", "1st"):
        for tag in exif_dict[ifd]:
            props[piexif.TAGS[ifd][tag]["name"]] = exif_dict[ifd][tag]
    return filter(props)


def print_exit(props):
    print json.dumps(props, indent=4, separators=(',', ': '))


def clean_img_repo():
    file_list = [f for f in os.listdir("./" + _img_repo_name) if f.endswith(".jpg")]
    for f in file_list:
        os.remove(_img_repo_name + "/" + f)


def filter(props):
    filters = ["ExposureTime", "FNumber", "FocalLength", "ISOSpeedRatings"]
    filtered_dict = {k: v for k, v in props.iteritems() if k in filters}
    return filtered_dict
    # return props

if __name__ == '__main__':
    # clean_img_repo()
    print_exit(url_extract("https://upload.wikimedia.org/wikipedia/commons/6/67/Inside_the_Batad_rice_terraces.jpg"))

