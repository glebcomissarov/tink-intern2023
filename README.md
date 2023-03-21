# Кейс для системных аналитиков

## Анализ задания

Согласно заданию, предполанается, что ритейлер будет ежедневно предоставлять следующие данные

- ФИО
- Номер телефона
- Email
- Список покупок в рамках акции с ценой товаров

Мне кажется, что ритейлеру будет довольно сложно (или невозможно) предосавить первые три вида данных, т.к. связать личные данные попупателя с совершенное покупкой:

- зачастую невозможно (у магазина нет карты специальной карты лояльности или покупатель ее не преобрел / предоставил при оплате)
- к карте лояльности зачастую привязана неактуальная (или фейковая) информация

Скорее всего со стороны ритейлера следует запросить только информацию о покупках за день, которую можно будет связать с

## API doc (openapi)

```
https://api.roga-and-kopita.com/get_purchases?date=2023-03-21&bank_name=tinkoff&auth_key=1d43f345bv65f45
```

```yaml
openapi: 3.0.2
info:
  title: Рога и Копыта API
  description: >
    part of API of
    marketplace "Рога и Копыта"
  version: "0.21.1"

servers:
  - url: https://api.roga-and-kopita.com
    description: API server

paths:
  /get_purchases:
    get:
      description: get array of purchases
      security:
        - ApiKeyAuth: []
      parameters:
        - in: query
          name: date
          schema:
            type: string
            example: "2023-03-21"
        - in: query
          name: bank_name
          schema:
            type: string
            example: "tinkoff"
      responses:
        "200":
          description: array of purchases returned
          content:
            application/json:
              schema:
                type: object
                properties:
                  response:
                    type: array
                    items:
                      $ref: "#/components/schemas/Purchase"
        "401":
          description: Not authenticated
        "403":
          description: Access token does not have the required scope

# create component (allows reuse)

components:
  schemas:
    Purchase:
      properties:
        purchase_id:
          type: integer
          example: 12500075
        date:
          type: string
          example: "2023-03-21 10:00:00.000"
        category_id:
          type: integer
          example: 45
        product_id:
          type: integer
          example: 78
        product_price:
          type: number
          example: 1205.20

  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: query
      name: auth_key
```

## API

Я написал небольшой сервер (на FastAPI)

```sh
# клонируем репозиторий
git clone

# создаем и активируем виртуальное окружение
python3.11 -m venv .env
source .env/bin/activate

# скачиваем зависитости


# запускаем сервер
```
