import scrapy

class communitySpider(scrapy.Spider):
	name = "community"

	def start_requests(self):
		allowed_domains = ['https://research.georgiasouthern.edu']
		start_urls = ['https://research.georgiasouthern.edu/empowering-and-enriching-communities/']
		for url in start_urls:
			yield scrapy.Request(url = url, callback = self.parse)


	def parse(self, response):
		for community in response.css('#main'):
			yield {
				'What does this team research?' : community.css('p:nth-child(6)::text').get(),
				'What does this team specialize in?' : community.css('h6:nth-child(8)::text').get() + community.css('h6:nth-child(10)::text').get() + community.css('h6 strong::text').get(),
				'What is Civic Infrastructures and Public Services?' : community.css('p:nth-child(9)::text').get(),
				'What is Community Health and Wellbeing?' : community.css('p:nth-child(11)::text').get(),
				'What do they mean by Quality of Life?' : community.css('p:nth-child(13)::text').get()
			}