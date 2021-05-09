import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.normpath(os.path.join(current_dir, f'../../logs/access.log'))
print("Топ 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой")
new_lines = []
with open(file_path, encoding='utf-8') as f:
    for line in f:
        line_list = line.split()
        if 400 <= int(line_list[8]) < 500:
            new_lines.append(line.split())
    sorted_new_lines = sorted(new_lines, key=lambda line: int(line[9]), reverse=True)
    for i in range(5):
        sorted_split_new_lines = sorted_new_lines[i]
        print(sorted_split_new_lines[6], sorted_split_new_lines[8], sorted_split_new_lines[9],
              sorted_split_new_lines[0])
