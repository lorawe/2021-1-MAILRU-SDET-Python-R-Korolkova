# установка базового образа (host OS)
FROM python:3.8
# копирование файла зависимостей в рабочую директорию
ADD /requirements.txt requirements.txt
# установка зависимостей
RUN pip install -r requirements.txt
# копирование содержимого локальной директории src в рабочую директорию
ADD /code code
# установка рабочей директории в контейнере
WORKDIR /code

# команда, выполняемая при запуске контейнера
CMD [ "python", "mock/vk_api_mock.py" ]