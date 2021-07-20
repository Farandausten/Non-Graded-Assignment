import scrapy
from h8dsft_scrapy.items import H8DsftScrapyItem

class Reviewspider123Spider(scrapy.Spider):
    name = 'reviewspider123'
    start_urls = ['https://imdb.com/search/title/?genres=animation/']

    for i in range(2, 100):
        start_urls.append('https://imdb.com/search/title/?genres=animation/'+str(i)+'')

    def parse(self, response):
        for href in response.xpath('//div[@class="lister-item-content"]/h3/a/@href'):
            url  = href.extract() 
            yield scrapy.Request(url, callback=self.parse_dir_contents)
 
    def parse_dir_contents(self, response):
        item = H8DsftScrapyItem()
        item['filmName'] = response.xpath('//div[@class="TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt"]/h1/text()').extract()
        item['durasi'] = response.xpath('//div[@class="TitleBlock__TitleMetaDataContainer-sc-1nlhx7j-2 hWHMKr"]/ul/li/text()').extract()
        item['genre'] = response.xpath('//div[@class="ipc-chip-list GenresAndPlot__GenresChipList-cum89p-4 gtBDBL"]/a/span/text()').extract()
        yield item
