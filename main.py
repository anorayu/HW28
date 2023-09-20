import os
import requests
import random

# Создание новой папки для сохранения картинок
os.makedirs("random_images", exist_ok=True)

# Загрузка 10 случайных картинок
for i in range(10):
    # Генерация случайного URL-адреса картинки
    random_image_url = f"https://example.com/image{i}.jpg"

    # Определение пути для сохранения картинки
    image_path = f"random_images/image{i}.jpg"

    # Загрузка картинки с использованием библиотеки requests
    response = requests.get(random_image_url)
    with open(image_path, "wb") as file:
        file.write(response.content)