
import os
import os.path as osp
import json

data = {}

def main():
    with open("pipelines_index.json", "w") as json_file:
        check_dir('pipelines')
        json.dump(data, json_file, ensure_ascii=False)

def check_dir(root_path):
    for name in os.listdir(root_path):
        if name == 'README.md':
            continue

        path = osp.join(root_path, name)

        # Check for other files if this is a directory
        if osp.isdir(path):
            check_dir(path)
            continue

        # Not a directory and not README file
        # So add this to the data
        name_no_ext = name.split('.')[0]
        ext = name.split('.')[1]
        pipeline = name_no_ext
        if name_no_ext.endswith('_highres'):
            pipeline = name_no_ext[:-('_highres'.length)]
        
        if not data[pipeline]:
            data[pipeline] = {'json': '', 'screenshots': []}

        if ext == 'json':
            # TODO: set as raw url
            data[pipeline]['json'] = name
        else:
            # TODO: set as raw url
            data[pipeline]['screenshots'].append(name)

main()