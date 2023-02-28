import scrapy

class advanceSpider(scrapy.Spider):
	name = "advance"

	def start_requests(self):
		allowed_domains = ['https://research.georgiasouthern.edu']
		start_urls = ['https://research.georgiasouthern.edu/impact-areas/advanced-materials-and-manufacturing/']
		for url in start_urls:
			yield scrapy.Request(url = url, callback = self.parse)


	def parse(self, response):
		for advance in response.css('#main'):
			yield {
				'What does this team research?' : advance.css('p:nth-child(6)::text').get(), 
                'What does this team specialize in?' : advance.css('p strong::text '+ '\n\n').getall(), 
                'What is Materials Engineering, Processing, and Characterization?': advance.css('p:nth-child(9)::text').get(),
                'What is Additive Manufacturing' : advance.css('p:nth-child(11)::text').get(),
                'What is Plant Operations including Robotics and Automation' : advance.css('p:nth-child(13)::text').get()
			}