# установка базового образа (host OS)
FROM python:3.8
# установка рабочей директории в контейнере
WORKDIR /code
# копирование файла зависимостей в рабочую директорию
COPY requirements.txt .
# установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt
# копирование содержимого локальной директории src в рабочую директорию
COPY code/mock .
# команда, выполняемая при запуске контейнера
CMD [ "python", "./vk_api_mock.py" ]