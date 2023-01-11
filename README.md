# Проект парсинга pep

### Описание проетка:

Это учебный проект асинхронного парсера, созданный на базе фреймворка Scrapy. Он создан, чтобы собирать информацию о PEP и считать их общее количество и в чатсности по каждому статусу

### Установка:

Клонировать репозиторий и перейти в него:

```
git clone git@github.com:MidasMr/scrapy_parser_pep.git
```

```
cd scrapy_parser_pep
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```


Windows
```
source venv/Scripts/activate
```

Linux, Mac OS
```
source venv/bin/activate
```

```
Обновить pip до последней версии

python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Для запуска нужно выполнить команду:
```
scrapy crawl pep
```

После этого результаты появятся в директории ```./results/```

В файле ```pep_Дата-Время.csv``` появятся информация про каждый PEP (Его номер имя и статус)

В файле ```status_summary_ДатаВремя.csv``` появится информация о количетсве PEP в каждом статусе и их общее число

Стек технологий:
```
Python 3.9
Scrapy 2.5
```


Автор:
[Александр Вязников(MidasMr)](https://github.com/MidasMr)