# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TaskItem(scrapy.Item):
    # define the fields for your item here like:
    company_name = scrapy.Field()
    location = scrapy.Field()
    job_role = scrapy.Field()
    job_link = scrapy.Field()
    summary = scrapy.Field()
    salary = scrapy.Field()
    
