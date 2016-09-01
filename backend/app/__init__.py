from flask import Flask
import exif_extract
import imagga_api

app = Flask(__name__, static_url_path='')
from app import views
