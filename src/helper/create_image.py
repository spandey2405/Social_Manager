__author__ = 'saurabh'

import sys,os,ImageDraw,ImageFont,Image
from src.conf import loggingmix
from src.conf.conf import img_dir,font

def createImage(no_of_lines,message,title,file,fbid):
    fontsize = 20
    colorText = "black"
    height = no_of_lines * 50
    try:
        fontname = ImageFont.truetype(font, fontsize)
        logoname = ImageFont.truetype(font, 16)
    except Exception as e:
        loggingmix.ERROR(str(sys.argv[0])+str(e))
    if height<150:
        height = 150
    img = Image.new( 'RGB', (500,height), "#f2f2f2")
    d = ImageDraw.Draw(img)
    messages = message.split("\n")
    count = 1
    for key in messages:
        d.text((20,30*count), key, fill=colorText, font=fontname)
        count = count + 1
    d.text((20,height-30),"Share  ||  Like ||  Read More On Funnymiku.in" , fill="green", font=logoname)
    try:
        img.save(img_dir+file)
        print "Images save at location /home/saurabh/mikz/src/img/%s" % file
    except Exception as e:
        loggingmix.ERROR("ERROR IN MAKING FILE at location" + img_dir + title)
