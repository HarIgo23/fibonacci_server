# Fibonacci service

## Run server

Run server that will be available on http://127.0.0.1:8080/

```bash
docker-compose up
```

## Initialize poetry

```bash
poetry install
```

## Run test

Without poetry

```bash
docker-compose run --rm app pytest 
```

or you should initialize poetry first

```bash
poetry run pytest
```

## Update container

If you modify dependencies, run this:

```bash
docker-compose build app 
```

## Параметры конфига

ENABLE_WARMUP - включает предзаполнение кэша

WARMUP_CACHE_LEN - регулирует количество предзаполненных элементов 

FIBONACCI_LIST_NAME - имя списка в Redis

## Задание
Реализовать сервис с единственным API методом, возвращающим срез последовательности чисел
из ряда Фибоначчи и простым UI для проверок.
Пример запроса: API GET http://example.com/fibonacci?from=3&to=6
Вернет ответ (в каком-то формате) с числами 2, 3, 5, 8

### Требования
* Сервис не должен вычислять повторно числа из ряда Фибоначчи. Значения необходимо
хранить в кеше (напр. Redis)
* Код должен быть выложен в репозиторий (напр. github.com)
* Необходимо продумать развертку/запуск сервиса на другом компьютере (напр. с помощью docker-compose)
* Описание сервиса в README.md