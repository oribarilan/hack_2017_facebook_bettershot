import requests
import json
import logging

API_KEY = 'acc_582557cbfd168cc'
API_SECRET = 'bf7c52e7f5c7f95757dc41a2fd8686d5'
HTTP_SUCCESS = 200
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)


categories_url = "https://api.imagga.com/v1/categorizers"

logger.debug("API key: {}:{}".format(api_key, api_secret))

def categorize_image(url=None, content=None):
    categorize_url = "https://api.imagga.com/v1/categorizations/personal_photos?"
    logger.debug("Entering 'categorize_image'")
    logger.debug("URL={}\tContent ID={}".format(url, content))
    query_parameters = ""
    if url:
        query_parameters += "url={}".format(url)
    elif content:
        query_parameters += "content={}".format(content)
    response = requests.get(categorize_url + query_parameters, auth=(API_KEY, API_SECRET))
    if response.status_code is not HTTP_SUCCESS:
        error_json = response.json()
        logger.error(error_json["error"] + " - " + error_json["message"])
        return "Error"
    image_result = response.json()["results"][0]["categories"][0]
    category = image_result["name"]
    confidence = image_result["confidence"]
    logger.info("Image was classiffied as '{}' with confidence of {}".format(category, confidence))
    logger.debug("Leaving 'categorize_image'")
    return category

def imagga_upload_image(filepath):
    logger.debug("Entering 'imagga_upload_image'")
    url = 'https://api.imagga.com/v1/content'
    files = {'media': open(filepath, 'rb')}
    response = requests.post(url, files=files, auth=(api_key, api_secret))
    logger.debug("Leaving 'imagga_upload_image'")
    return response.json()["uploaded"][0]["id"]

# Sample run
image_id = imagga_upload_image("/home/liran/fb_hackathon_2016/sample_shots/landscape2.jpg")
print(categorize_image(content=image_id))
image_url = 'http://docs.imagga.com/static/images/docs/sample/japan-605234_1280.jpg'
categorize_image(url=image_url)

# Pretty print JSON
# print(json.dumps(response.json(), sort_keys=True, indent=4))
