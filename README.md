asf-mail-spider
===============

A scrapy based crawler of the ASF mail archives

You need to install scrapy (http://www.scrapy.org):

    pip install Scrapy

Pick the ASF project that you want to crawl from:
http://mail-archives.apache.org/mod_mbox/

Edit the settings.py script and add the name of the project in the list,

    ASFPROJECT = ['cloudstack','couchdb']

Then launch the spider :

    scrapy crawl asf -o items.json -t json

It can be done via script as well with a twisted reactor.

The result will be `items.json` containing several dictionaries.

You can improve the spider in `./spiders/asf_spider.py`
You can improve the post processing by defining items pipelines in `pipelines.py`
