
import os
import json

data = []

def main():
    with open("pipelines_index.json", "w") as json_file:
        check_dir('pipelines')
        json.dump(data, json_file, ensure_ascii=False)

def check_dir(root_path):
    for path in os.listdir(root_path):
        if os.path.isdir(path):
            check_dir(path)
        # Not a directory, so this is a file
        if path == 'README.md':
            continue

        data.append({
            'name': root_path+path
        })

main()
