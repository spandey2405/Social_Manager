__author__ = 'saurabh'
import os,sys
BASE_DIR = os.path.realpath(sys.argv[0]).split('Social_Manager/')[0]
sys.path.append(BASE_DIR)

class Posting():
    def __init__(self):
        self.access_token="1425161467767256|NhF9K2ZLgNmKyhLx9q3TjM8-pvk"
        self.copy_page_id="funnymiku.in"

    def get_choice(self):
        print "1. Get Post From Facebook Page"

        choice = int(raw_input("\n\n>>"))
        if choice == 1:
            self.check_make_image_data()

    def check_make_image_data(self):
        from src.helper.make_image_data import make_image_data
        make_image_data(access_token=self.access_token, copy_page_id=self.copy_page_id)

def init():
    a = Posting()
    a.check_make_image_data()



if __name__ == '__main__':
    init()