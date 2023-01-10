from collections import defaultdict
import csv
import datetime as dt

from constants import BASE_DIR


class PepParsePipeline:
    def open_spider(self, spider):
        self.statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.statuses[str(item['status'])] += 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / 'results'
        current_time = dt.datetime.today().strftime(
            '%Y-%m-%dT%H-%M-%S'
        )
        results_dir.mkdir(exist_ok=True)
        file_name = f'status_summary_{current_time}.csv'
        file_path = results_dir / file_name
        with open(file_path, 'w', encoding='utf-8') as f:
            csv.writer(
                f, dialect=csv.unix_dialect
            ).writerows([
                ('Статус', 'колличество'),
                *self.statuses.items(),
                ('Всего', sum(self.statuses.values()))
            ])
        self.statuses.clear()
