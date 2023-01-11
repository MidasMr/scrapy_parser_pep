import re

import scrapy

from ..items import PepParseItem


PATTERN = re.compile(r'^PEP\s(?P<number>\d+)\s[–]\s(?P<name>.*)')
PEP_URL = 'peps.python.org'


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [PEP_URL]
    start_urls = [f'https://{PEP_URL}/']

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
