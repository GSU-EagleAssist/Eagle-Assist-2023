import scrapy
from ..items import chatbotEntry

class MembershipSpider(scrapy.Spider):
	name = "memberships"
	
	custom_settings = {
        'FEEDS': { 'Recreation-Memberships.csv': { 'format': 'csv', 'overwrite': 'True', 'item_export_kwargs': {'include_headers_line': False,}}},
        }

	def start_requests(self):
		allowed_domains = ['https://recreation.georgiasouthern.edu']
		start_urls = ['https://recreation.georgiasouthern.edu/facility-memberships/']
		for url in start_urls:
			yield scrapy.Request(url = url, callback = self.parse)


	def parse(self, response):
		for memberships in response.css('#main > div.tabswrap.ui-tabs.ui-corner-all.ui-widget.ui-widget-content'):

			q1 = chatbotEntry()
			q1['Question'] = '"Do students automatically get a gym membership?"',
			q1['Answer'] = memberships.css('#statesboro > p:nth-child(5)::text').get(),
			yield q1
			
			q2 = chatbotEntry()
			q2['Question'] = '"Can a students spouse have a gym membership"',
			q2['Answer'] = memberships.css('#statesboro p:nth-child(10)::text').get(),
			yield q2

			q3 = chatbotEntry()
			q3['Question'] = '"What is the price for gym passes for the Statesboro campus?"',
			q3['Answer'] = memberships.css('#statesboro ul:nth-child(11)::text').getall(),
			yield q3

			q4 = chatbotEntry()
			q4['Question'] = '"What is the price for gym passes for the Armstrong campus?"',
			q4['Answer'] = memberships.css('#armstrong ul:nth-child(11)::text').getall(),
			yield q4