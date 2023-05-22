import scrapy

class JobboleSpider(scrapy.Spider):
    name = "jobbole"  # 爬虫名称
    allowed_domains = ["news.cnblogs.com"]
    start_urls = ["https://news.cnblogs.com"]

    def start_requests(self):
        # 入口可以模拟登录拿到cookie

        for url in self.start_urls:
            yield Request(url, dont_filter=True)

    def parse(self, response):
        pass
