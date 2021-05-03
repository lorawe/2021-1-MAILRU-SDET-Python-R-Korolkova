import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.normpath(os.path.join(current_dir, f'../../logs/access.log'))
new_lines = []
with open(file_path, encoding='utf-8') as f:
    for line in f:
        line_list = line.split()
        if int(line_list[8]) >= 400 and int(line_list[8]) < 500:
            new_lines.append(line)
    sorted_new_lines = sorted(new_lines, key=lambda line: line.split()[9], reverse=True)
    print("Топ 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой")
    for i in range(5):
        sorted_split_new_lines = sorted_new_lines[i].split()
        print(sorted_split_new_lines[6], sorted_split_new_lines[8], sorted_split_new_lines[9], sorted_split_new_lines[1])

