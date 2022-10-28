import os
import json
from collections import defaultdict

target_folder = r'C:\Windows\System32'
result_file_name = '_summary.json'

files_in_folder = []
result_counts = defaultdict(int)
result_extensions = defaultdict(list)

for root, folders, files in os.walk(target_folder):
    for file_path in files:
        filepath = os.path.join(root, file_path)
        files_in_folder.append(filepath)

for file_path in files_in_folder:
    size = os.stat(file_path).st_size
    key = 10 ** (len(str(size)))
    result_counts[key] += 1
    result_extensions[key].append(os.path.splitext(file_path)[1].lower())

result = {key: (result_counts[key], list(sorted(set(result_extensions[key]))))
          for key in sorted(result_counts.keys())}

with open(f'{os.path.split(target_folder)[1]}{result_file_name}', mode='w') as out_file:
    json.dump(result, out_file)
