
import os
import os.path as osp
import json

data = []

def main():
    with open("pipelines_index.json", "w") as json_file:
        check_dir('pipelines')
        json.dump(data, json_file, ensure_ascii=False)

def check_dir(root_path):
    for name in os.listdir(root_path):
        if name == 'README.md':
            continue

        path = osp.join(root_path, name)
        if osp.isdir(path):
            check_dir(path)
            continue

        # Not a directory and not README file
        # So add this to the data
        data.append({
            'name': path
        })

main()
