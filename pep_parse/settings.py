from pathlib import Path


BASE_DIR = Path(__file__).parent.parent
RESULTS_FOLDER_NAME = 'results'
RESULTS_DIR = BASE_DIR / RESULTS_FOLDER_NAME
SPIDERS_PATH = 'pep_parse.spiders'

BOT_NAME = 'pep_parse'

SPIDER_MODULES = [SPIDERS_PATH]
NEWSPIDER_MODULE = SPIDERS_PATH

FEEDS = {
    f'{RESULTS_FOLDER_NAME}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    }
}

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
