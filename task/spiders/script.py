import scrapy
from ..items import TaskItem
class QuoteSpider(scrapy.Spider):
	name = 'quotes'
	page_number = 2
	start_urls = [
	'https://www.simplyhired.com/search?q=&l=Austin%2C+TX&job=rL-FPHmOlO8S0LDRzJZQ1C1-GcuCOZ1Z6Au5yRSFG3M7X_c1ZcOmGA'
	]
	
	def parse(self,response):
		items = TaskItem()
		urls = 'https://www.simplyhired.com'
		all_div_quotes = response.css('article.SerpJob')

		for quote in all_div_quotes:
			job_role = quote.css('a.card-link::text')[0].extract()
			job_link = quote.css('a.card-link').xpath("@href").extract()
			job_company = quote.css('span.jobposting-company::text').extract() 
			company_location = quote.css('span.jobposting-location::text')[0].extract() 
			if not job_company:
				job_company.append(quote.css('a.card-link::text')[1].extract())
			summary = quote.css('p.jobposting-snippet::text').extract() 
			salary = quote.css('span.jobposting-salary::text').extract() 
			if salary[0] == "Estimated: ":
				salary[0] = salary[1]
			items['company_name'] = job_company
			items['location'] = company_location
			items['job_role'] = job_role
			items['job_link'] = urls+""+job_link[0]
			items['summary'] = summary
			items['salary']=salary[0]

			yield items
			next_page = "https://www.simplyhired.com/search?l=Austin%2C+TX&pn="+str(QuoteSpider.page_number)+"&job=380F5vdkwZikDiGf3s4a_3eH3-C2X4PGkJbB_JUmDwV0XnuKtWRJjw"

			if QuoteSpider.page_number<=91:
				QuoteSpider.page_number +=1
				yield response.follow(next_page,callback=self.parse)