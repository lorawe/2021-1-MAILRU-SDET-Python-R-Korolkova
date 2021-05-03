import os



current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.normpath(os.path.join(current_dir, f'../../logs/access.log'))
get_counter = 0
post_counter = 0
put_counter = 0
delete_counter = 0
print("Общее количество запросов по типу, например:")
with open(file_path, encoding='utf-8') as f:
    for line in f:
        if "GET" in line:
            get_counter += 1
        if "POST" in line:
            post_counter += 1
        if "PUT" in line:
            put_counter += 1
        if "DELETE" in line:
            delete_counter += 1
print(f"GET - {get_counter}, POST - {post_counter}, PUT - {put_counter}, DELETE - {delete_counter}")


