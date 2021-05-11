import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path_log = os.path.normpath(os.path.join(current_dir, f'../../logs/access.log'))
file_path_json = os.path.normpath(os.path.join(current_dir, f'../../results/python_result.json'))


def count_requests():
    with open(file_path_log, encoding='utf-8') as f:
        count = int(sum(chunk.count('\n')
                        for chunk in iter(lambda: f.read(), '')))
        return count


def count_methods():
    methods = {"GET": 0, "PUT": 0, "POST": 0, "HEAD": 0, "DELETE": 0, "CONNECT": 0, "OPTIONS": 0, "TRACE": 0,
               "PATCH": 0}
    with open(file_path_log, encoding='utf-8') as f:
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
            result_dict = {}
        for m in sorted_methods:
            if methods[m] > 0:
                result_dict[methods[m]] = m
        return result_dict


def top10_requests():
    uniq_url = dict()
    with open(file_path_log, encoding='utf-8') as f:
        for line in f:
            line_list = line.split()
            uniq_url.setdefault(line_list[6], 0)
            uniq_url[line_list[6]] += 1
        sorted_counted_urls = list(
            dict(sorted(uniq_url.items(), key=lambda url: int(url[1]), reverse=True)).items())[
                              :10]
        result_dict = {}
        for u in sorted_counted_urls:
            result_dict[u[1]] = u[0]
        return result_dict


def top5_heavy4XX():
    new_lines = []
    with open(file_path_log, encoding='utf-8') as f:
        for line in f:
            line_list = line.split()
            if 400 <= int(line_list[8]) < 500:
                new_lines.append(line.split())
        sorted_new_lines = sorted(new_lines, key=lambda line: int(line[9]), reverse=True)
        result_list = []
        for i in range(5):
            sorted_split_new_lines = sorted_new_lines[i]
            result_list.append([sorted_split_new_lines[6], sorted_split_new_lines[8], sorted_split_new_lines[9],
                                sorted_split_new_lines[0]])
        return result_list


def top5_count5XX():
    new_lines = []
    ip_list = []
    with open(file_path_log, encoding='utf-8') as f:
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
        result_dict = {}
        for i in range(5):
            result_dict[sorted_counted_ips[i]] = counted_ips[sorted_counted_ips[i]]
        return result_dict
