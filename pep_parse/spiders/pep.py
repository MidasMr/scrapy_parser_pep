import scrapy

from constants import PATTERN
from ..items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_peps = response.css(
            'section[id="numerical-index"] '
            'a::attr(href)'
        ).getall()
        for pep in all_peps:
            yield response.follow(
                pep,
                callback=self.parse_pep
            )

    def parse_pep(self, response):
        number, name = PATTERN.search(
                response.css('h1.page-title::text').get()
            ).group('number', 'name')
        yield PepParseItem(
            number=number,
            name=name,
            status=response.css(
                'dt:contains("Status") + dd abbr::text'
            ).get()
        )
