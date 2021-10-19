from collections import Counter, defaultdict
from operator import itemgetter


def read_file(file_name):
    with open(file_name, mode='r', encoding='utf8') as file:
        for line in file:
            if line:
                items = line.strip().split()
                addr = items[0]
                type_ = items[5][1:]
                resource = items[6]
                yield addr, type_, resource


def proof():
    file = read_file('nginx_logs.txt')
    i = 0
    while i < 10:
        print(next(file))
        i += 1


# addrs = [addr for addr, _, _ in read_file('nginx_logs.txt')]
# spammer, requests_count = Counter(addrs).most_common()[0]

stats = defaultdict(int)
for address, _, _ in read_file('nginx_logs.txt'):
    stats[address] += 1
spammer, requests_count = sorted(stats.items(), key=itemgetter(1))[-1]
# spammer, requests_count = sorted(stats.items(), key=itemgetter(1), reverse=True)[0]

print(spammer, requests_count)
