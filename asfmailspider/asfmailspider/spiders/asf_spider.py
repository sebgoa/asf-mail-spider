from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from asfmailspider.items import asfproject,listmbox
from scrapy.conf import settings
import datetime

class ASFSpider(BaseSpider):
    name = "asf"
    allowed_domains = ["apache.org"]
    start_urls = [
        "http://mail-archives.apache.org/mod_mbox/",
    ]
    
    project=settings['ASFPROJECT']

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        projects = hxs.select('//li')
        for index, list in enumerate(projects):
            if (list.select('./h3') != []) and (str(list.select('./h3/a/@name').extract()[0]) in self.project):
                item = asfproject()
                item['project'] = list.select('./h3/a/@name').extract()
                item['list'] = list.select('.//li/a/text()').extract()
                item['link']= list.select('.//li/a/@href').extract()
                print item['project'], item['list'], item['link']
                for i in range(len(item['link'])):
	            request = Request(url=response.request.url+item['link'][i], callback=self.parse_item)
                    request.meta['item']=item
                    request.meta['ml']=item['link'][i]
                    yield request
                    continue

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        table = hxs.select('//tr')
        item = response.meta['item']
        ml = response.meta['ml']
        print ml
        tmp=[]
        pml = listmbox()
        for index, td in enumerate(table):
            if td.select('./td[contains(@class,"date")]/text()').extract() != []:
                dates = td.select('./td[contains(@class,"date")]/text()').extract()
                msgcount = td.select('./td[contains(@class,"msgcount")]/text()').extract() 
                #tmp.append((dates[0],msgcount[0]))
                tmp.append((datetime.datetime.strptime(dates[0],"%b %Y"),msgcount[0]))
                pml['datatime']=tmp
                pml['ml']=ml
                print dates, msgcount 
        return pml,item


