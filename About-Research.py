import scrapy
from ..items import chatbotEntry

class aboutRSpider(scrapy.Spider):
	name = "aboutR"
	
	custom_settings = {
        'FEEDS': { 'About-Research.csv': { 'format': 'csv', 'overwrite': 'True', 'item_export_kwargs': {'include_headers_line': False,}}},
        }

	def start_requests(self):
		allowed_domains = ['https://research.georgiasouthern.edu/']
		start_urls = ['https://research.georgiasouthern.edu/about-us/']
		for url in start_urls:
			yield scrapy.Request(url = url, callback = self.parse)


	def parse(self, response):
		for aboutR in response.css('#main'):

			q1 = chatbotEntry()
			q1['Question'] = '"Who is the Vice Provost for Research & Scholarship?"',
			q1['Answer'] = '"' + aboutR.css('div:nth-child(7)  p strong::text').get() + '. You can reach them at: ' + aboutR.css('div:nth-child(7) p a::text').get() + '"',
			yield q1
			
			q2 = chatbotEntry()
			q2['Question'] = '"Who is the  Associate Provost for Research?"',
			q2['Answer'] = '"' + aboutR.css('div:nth-child(8)  p strong::text').get() + '. You can reach them at: ' + aboutR.css('div:nth-child(8) p a::text').get() + '"',
			yield q2

			q3 = chatbotEntry()
			q3['Question'] = '"Who is the Director of Research Integrity?"',
			q3['Answer'] = '"' + aboutR.css('div:nth-child(9)  p strong::text').get() + '. You can reach them at: ' + aboutR.css('div:nth-child(9) p a::text').get() + '"',
			yield q3

			q4 = chatbotEntry()
			q4['Question'] = '"Who is the Director of Research Operations?"',
			q4['Answer'] = '"' + aboutR.css('div:nth-child(10)  p strong::text').get() + '. You can reach them at: ' + aboutR.css('div:nth-child(10) p a::text').get() + '"',
			yield q4

			q5 = chatbotEntry()
			q5['Question'] = '"Who is the Associate Provost for Innovation & Commercialization?"', 
			q5['Answer'] = '"' + aboutR.css('div:nth-child(11)  p strong::text').get() + '. You can reach them at: ' + aboutR.css('div:nth-child(11) p a::text').get() + '"',
			yield q5

			q6 = chatbotEntry()
			q6['Question'] = '"Who is the Associate Vice President for Finance, Research, Compliance, & Housing Foundations?"',
			q6['Answer'] =  '"' + aboutR.css('div:nth-child(12) p strong::text').get() + '. You can reach them at: ' + aboutR.css('div:nth-child(12) p a::text').get() + '"',
			yield q6

			q7 = chatbotEntry()
			q7['Question'] = '"What Research Centers and institutes do the school work with?"'
			q7['Answer'] = '"You can find the list of all centers and institutes at this site: "' + aboutR.css('h5:nth-child(18) a').attrib['href']
			yield q7

			q8 = chatbotEntry()
			q8['Question'] = '"What Labs does the school work with?"'
			q8['Answer'] = '"You can find the list of all labs here: "' + response.css('#menu-item-4797 > a').attrib['href']
			yield q8