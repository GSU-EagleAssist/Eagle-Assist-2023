import scrapy

class coastalSpider(scrapy.Spider):
	name = "coastal"

	def start_requests(self):
		allowed_domains = ['https://research.georgiasouthern.edu']
		start_urls = ['https://research.georgiasouthern.edu/coastal-sustainability-and-resilience/']
		for url in start_urls:
			yield scrapy.Request(url = url, callback = self.parse)


	def parse(self, response):
		for coastal in response.css('#main'):
			yield {
				'What does this team research?' : coastal.css('p:nth-child(7)::text').get() + coastal.css('p:nth-child(8)::text').get(), 
                		'What does this team specialize in?' : coastal.css('h6::text').getall(),
                		'What is Conservation Biology and Shoreline Ecology' : coastal.css('p:nth-child(12)::text').get(),
                		'What is Water Quality' : coastal.css('p:nth-child(14)::text').get(),
                		'What are Water Resources' : coastal.css('p:nth-child(16)::text').get()
			}
