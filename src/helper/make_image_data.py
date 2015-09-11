__author__ = 'saurabh'
import sys,os
BASE_DIR = os.path.realpath(sys.argv[0]).split('/conf')[0]
sys.path.append(BASE_DIR)

from src.helper.get_fb_post import get_post,format_message,get_title,get_file_name,count_lines,next_page
import src.helper.create_image as imagecreator
import src.db_handler.database as db
def make_image_data(copy_page_id, access_token):
    choice = "y"
    parameters = None
    while (choice != "n"):
        os.system("clear")
        posts = get_post(copy_page_id,access_token,limit=1, parameters=parameters)
        for post in posts:
            try:
                message = format_message(post["message"])
                post_id = post["id"]
                lines = count_lines(message)
                title = get_title(message)
                file = post_id+".png"
                data = {"title":title, "filename":file, "fbid":post_id}
                status= db.write_data(data)
                if status == True:
                    print(post["message"])
                    choice_post = raw_input("\nPress Enter To post .... \nPress x to see next post\nCtrl + Z to Exit")
                    if choice_post !="x":
                        imagecreator.createImage(no_of_lines=lines, message=message, file=file , fbid= post_id, title=title)
            except Exception as e:
                print e

        parameters = next_page(copy_page_id, access_token, limit=1, parameters=parameters)
