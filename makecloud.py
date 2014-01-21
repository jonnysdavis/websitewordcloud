#!/usr/bin/python

import urllib2
from collections import defaultdict
import re
from pytagcloud import create_tag_image, make_tags
from pytagcloud.lang.counter import get_tag_counts
import pygame
from BeautifulSoup import BeautifulSoup
from easygui import enterbox
from PIL import Image

result = enterbox(msg='Enter in the FULL website adress including http://\nClick on the generated image to alter it!', title=' ', default="http://www.", strip=True)

req = urllib2.Request(result,headers={'User-Agent' : "Magic Browser"}) 
con = urllib2.urlopen(req)
page = con.read()

soup = BeautifulSoup(page)
texts = soup.findAll(text=True)

def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element)):
        return False
    return True

page = filter(visible, texts)
page = str(page)
page = ''.join([i for i in page if not i.isdigit()])

page = page[2000:10000]


tags = make_tags(get_tag_counts(page), maxsize=120)
create_tag_image(tags, 'cloud.png', size=(900, 600), fontname='Droid Sans')


f = Image.open("cloud.png").show()
