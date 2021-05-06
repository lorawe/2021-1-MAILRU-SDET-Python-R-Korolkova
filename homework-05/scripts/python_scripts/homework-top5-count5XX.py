import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.normpath(os.path.join(current_dir, f'../../logs/access.log'))
new_lines = []
ip_list = []
print("Топ 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой")
with open(file_path, encoding='utf-8') as f:
    for line in f:
        line_list = line.split()
        if 500 <= int(line_list[8]) < 600:
            new_lines.append(line)
            ip_list.append(line_list[0])
    ip_list_set = set(ip_list)
    counted_ips = {}
    for ip in ip_list_set:
        counted_ips[ip] = ip_list.count(ip)
    sorted_counted_ips = sorted(counted_ips, reverse=True, key=lambda ips: ips[2])
    for i in range(5):
        print(sorted_counted_ips[i], counted_ips[sorted_counted_ips[i]])

