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


# решение с использованием defaultdict, останется для примера, на всякий случай
def solution_with_defaultdict():
    stats = defaultdict(int)
    for address, _, _ in read_file('nginx_logs.txt'):
        stats[address] += 1
    spammer, requests_count = sorted(stats.items(), key=itemgetter(1))[-1]
    # spammer, requests_count = sorted(stats.items(), key=itemgetter(1), reverse=True)[0]
    print(spammer, requests_count)


stats = Counter()
for addr, _, _ in read_file('nginx_logs.txt'):
    stats[addr] += 1
spammer, requests_count = stats.most_common()[0]
print(spammer, requests_count)
