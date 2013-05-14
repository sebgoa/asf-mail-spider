# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class AsfItem(Item):
    # define the fields for your item here like:
    # name = Field()
    pass

class asfproject(Item):
    project = Field()
    list = Field()
    link = Field()

class listmbox(Item):
    ml = Field()
    datatime = Field()
    
