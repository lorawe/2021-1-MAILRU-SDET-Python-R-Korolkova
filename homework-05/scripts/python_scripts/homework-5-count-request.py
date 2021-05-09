import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.normpath(os.path.join(current_dir, f'../../logs/access.log'))
counter_request = 0
print("Общее количество запросов:")
with open(file_path, encoding='utf-8') as f:
    print(sum(chunk.count('\n')
              for chunk in iter(lambda: f.read(), '')))
