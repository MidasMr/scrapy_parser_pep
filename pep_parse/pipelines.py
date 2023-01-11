from collections import defaultdict
import csv
import datetime as dt

from .settings import BASE_DIR, RESULTS_DIR, RESULTS_FOLDER_NAME


class PepParsePipeline:
    RESULTS_DIR.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / RESULTS_FOLDER_NAME
        current_time = dt.datetime.today().strftime(
            '%Y-%m-%dT%H-%M-%S'
        )
        file_name = f'status_summary_{current_time}.csv'
        file_path = results_dir / file_name
        with open(file_path, 'w', encoding='utf-8') as f:
            csv.writer(
                f,
                dialect=csv.unix_dialect,
                quoting=csv.QUOTE_NONE
            ).writerows([
                ('Статус', 'колличество'),
                *self.statuses.items(),
                ('Всего', sum(self.statuses.values()))
            ])
