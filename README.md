TG - @artemcringe

## Предварительные условия
Прежде чем начать, убедитесь, что у вас установлено следующее:
- [Python](https://www.python.org/downloads/) **версии 3.11**
- [Docker](https://www.docker.com/get-started): Необходим для контейнеризации приложения. Вы можете скачать и установить Docker с [официального сайта](https://www.docker.com/get-started).
- [Docker Compose](https://docs.docker.com/compose/install/): Используется для управления многоконтейнерными приложениями. Установите Docker Compose, следуя [инструкциям на официальном сайте](https://docs.docker.com/compose/install/).


## Установка
```shell
git clone https://github.com/web3artem/MeraCapitalTest.git
cd MeraCapitalTest
```

## Запуск приложения
1. Запустите приложение с помощью Docker Compose:
```shell
docker-compose up
```
2. После запуска приложения откройте браузер и перейдите по адресу `http://localhost:8000/docs`

## Логика приложения
Приложение раз в 60 секунд посылает запрос на API биржи и забирает тикер, цену и отметку в UNIX времени. В документации можно протестировать эндпоинты API:
В качестве базы данных использовался PostgreSQL, для миграция - Alembic, все упаковано в docker-контейнеры.
1. Эндпоинт **/get_currency_data_by_ticker** позволяет получить всю информацию из базы данных по тикеру, принимает query-параметр ticker (eth_usd, btc_usd) 
2. Эндпоинт **/get_last_price_by_ticker** получает самую последнюю (свежую) запись в базе данных, принимает query-параметр ticker (eth_usd, btc_usd)
3. Эндпоинт **/get_currency_price_by_date** получает информацию о тикере в переданный диапазон времени. Передавать время можно в UNIX формате либо "DD-MM-YY", принимает 3 query параметра: ticker, start_time, end_time
 
