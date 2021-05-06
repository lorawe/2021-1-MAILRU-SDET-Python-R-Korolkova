import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.normpath(os.path.join(current_dir, f'../../logs/access.log'))
print("Общее количество запросов по типу:")
methods = {"GET": 0, "PUT": 0, "POST": 0, "HEAD": 0, "DELETE": 0, "CONNECT": 0, "OPTIONS": 0, "TRACE": 0,
               "PATCH": 0}
with open(file_path, encoding='utf-8') as f:
    for line in f:
        line_splited = line.split()
        line_method = line_splited[5].replace('"', '')
        if line_method in methods:
            methods.setdefault(line_method, 0)
            methods[line_method] += 1
        else:
            methods.setdefault(f"Неккоретный метод: {line_method}", 0)
            methods[f"Неккоретный метод: {line_method}"] += 1
        sorted_methods = dict(sorted(methods.items(), key=lambda method: int(method[1]), reverse=True))
for m in sorted_methods:
    if methods[m] > 0:
        print(methods[m], m)


