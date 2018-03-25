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
пример запуска утилиты
.. code-block:: bash

   sw-downloader --year 2018 --month 2 --resolution=1024x768
   
Собранные обои будут в каталоге "2018-February-1024x768".

Параметры --year и --month можно опустить, вместо них будет взят 
текущий месяц и год соответвенно.


Описание реализации
-------------------

Утилита сделана на основе фреймворка `Scrapy <https://scrapy.org/>`_

Логика выборки элементов задана в классе `SmashingMagazineSpider <https://github.com/aezhov/sw_downloader/blob/master/sw_downloader/sw_downloader/spiders/smashing_magazine.py>`_

