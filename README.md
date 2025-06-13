![изображение](https://github.com/user-attachments/assets/e36e1105-a3b8-4073-8b37-70ae30f2db77)

161.35.198.12/docs

![изображение](https://github.com/user-attachments/assets/53e64f3c-953d-48cd-920c-6031a03a8c22)
failed((((((

## Запуск проекта

1. Убедитесь, что у вас установлен Docker и Docker Compose.
2. Соберите и запустите контейнеры:
   ```sh
    sudo docker-compose -f docker-compose.dev.yml up --build
   ```
3. Открывайте API-документацию в браузере:
   - Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
   - Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Остановка контейнеров

```sh
docker-compose -f docker-compose.dev.yml down
```
