# lab3

## Описание модели
[Модель](https://huggingface.co/cointegrated/rubert-tiny-toxicity) классификации текста по токсичности:
* non-toxic
* insult
* threat
* dangerous

## Описание сервиса

### REST API сервис на основе FastAPI

Сборка образа и запуск контейнера
```bash
docker build -t ru-sentiment-proba .
docker run -d --rm -p 80:80 -it ru-sentiment-proba:latest
```
Пример запроса:
```bash
curl -X POST http://localhost/predict -H "Content-Type: application/json" -d '{"text": "какой сегодня прекрасный день"}'
> {"prediction":{"non-toxic":0.9998,"insult":0.0003,"obscenity":0.0000,"threat":0.0001,"dangerous":0.0430}}
```