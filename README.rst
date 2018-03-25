=============================
Smashing Wallpaper Downloader
=============================


CLI утилита, основанная на Scrapy, для загрузки обоев с сайта www.smashingmagazine.com


* Free software: MIT license


Установка
---------
Предполагается, что все манипуляции проводятся в virtualenv

.. code-block:: bash

   virtualenv -p $(which python3.6) .venv
   source .venv/bin/activate

Получение репозитория и установка в virtualenv:

.. code-block:: bash

   git clone https://github.com/aezhov/sw_downloader.git .
   cd sw_downloader
   pip install .


теперь можно запустить тесты

.. code-block:: bash

   python setup.py test


Запуск
------
* запуск утилиты
* запуск тестов

Описание реализации
-------------------

