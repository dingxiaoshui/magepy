import sys
import re

def read_log(path):
    with open(path) as f:
        for line in f:
            yield line


def parse(path):
    o = re.compile(r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) .* .* \[(?P<time>.*)\] "(?P<method>\w+) (?P<url>[^\s]*) (?P<version>[\w|/\.\d]*)" (?P<status>\d{3}) (?P<length>\d+) "(?P<referer>[^\s]*)" "(?P<ua>.*)"'))
    for line in read_log(path):
        m = o.sreach(line.rstrip('\n'))
        if m:
            yield m.groupdict()

def count(key,data):
    if key not in data.keys():
        data[key] = 0
    data[key] += 1
    return data

def analyze(path):
    data = {
        'ip':{},
        'url':{},
        'ua':{},
        'status':{},
        'throughput':{}
    }
    for item in parse(path):
        for key,value in count_data.items():
            if key != 'throughput':
                data[key] = count(item[key],value)
        data['throughput'] += item['length']
    return data


    return

def render_line():
    pass

def render_bar():
    pass

def render_pie():
    pass


def main():
    data = analyze(sys.argv[1])
    render_line('throughput',data[ ])