__author__ = 'saurabh'

import os,sys
BASE_DIR = os.path.realpath(sys.argv[0]).split('/src')[0]
sys.path.append(BASE_DIR)
print os.path.abspath(sys.argv[0])
def check_login():
    from src.conf import loggingmix
    loggingmix.DEBUG("MESSAGE")
    loggingmix.WARNING("MESSAGE")
    loggingmix.CRITICAL("MESSAGE")
    loggingmix.ERROR("MESSAGE")

def check_fetch():
    from src.helper.fetch import get_data_json
    get_data_json(access_token="1425161467767256|NhF9K2ZLgNmKyhLx9q3TjM8-pvk", page_id="funnymiku.in", limit=1)


def check_get_post():
    from src.helper.get_fb_post import get_post
    get_post(access_token="1425161467767256|NhF9K2ZKyhLx9q3TjM8-pvk", page_id="funnymiku.in", limit=1)

def check_next_page():
    from src.helper.get_fb_post import next_page
    next_page(access_token="1425161467767256|NhF9K2ZLgNmKyhLx9q3TjM8-pvk", page_id="funnymiku.in", limit=1)

def check_make_image_data():
    from src.helper.make_image_data import make_image_data
    make_image_data(access_token="1425161467767256|NhF9K2ZLgNmKyhLx9q3TjM8-pvk", copy_page_id="funnymiku.in")

#check_make_image_data()
