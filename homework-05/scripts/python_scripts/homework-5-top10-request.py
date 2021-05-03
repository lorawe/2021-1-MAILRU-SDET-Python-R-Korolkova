import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.normpath(os.path.join(current_dir, f'../../logs/access.log'))
new_lines = []
ip_list = []
print("Топ 10 запросов:")
request_list = []
url_list = []
with open(file_path, encoding='utf-8') as f:
    for line in f:
        line_list = line.split()
        url_list.append(line_list[6])
    request_list_set = set(url_list)
    counted_urls = {}
    for url in request_list_set:
        counted_urls[url] = url_list.count(url)
    sorted_counted_urls = sorted(counted_urls, reverse=True, key=lambda urls: urls[2])
    for i in range(10):
        print(sorted_counted_urls[i], counted_urls[sorted_counted_urls[i]])
