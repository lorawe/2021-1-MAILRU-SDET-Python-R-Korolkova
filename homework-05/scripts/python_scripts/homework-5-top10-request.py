import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.normpath(os.path.join(current_dir, f'../../logs/access.log'))
print("Топ 10 запросов:")
uniq_url = dict()
with open(file_path, encoding='utf-8') as f:
    for line in f:
        line_list = line.split()
        uniq_url.setdefault(line_list[6], 0)
        uniq_url[line_list[6]] += 1
    sorted_counted_urls = list(dict(sorted(uniq_url.items(), key=lambda url: int(url[1]), reverse=True)).items())[:10]
    for u in sorted_counted_urls:
        print(u[1], u[0])
