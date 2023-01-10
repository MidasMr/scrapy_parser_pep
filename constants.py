import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

PATTERN = re.compile(r'^PEP\s(?P<number>\d+)\s[–]\s(?P<name>.*)')
