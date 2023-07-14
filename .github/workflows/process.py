
import os
import os.path as osp
import json

data = {}

def main():
    with open("pipelines/pipelines_index.json", 'w') as json_file:
        check_dir('pipelines')
        json.dump(data, json_file, ensure_ascii=False)

def check_dir(root_path):
    for name in os.listdir(root_path):
        if name == 'README.md' or name == 'pipelines_index.json' or name.startswith('.'):
            continue

        path = osp.join(root_path, name)

        # Check for other files if this is a directory
        if osp.isdir(path):
            check_dir(path)
            continue

        # Not a directory and not a non-pipeline file
        # So add this to the data
        name_no_ext = name.split('.')[0]
        ext = name.split('.')[1]
        pipeline = name_no_ext
        if name_no_ext.endswith('_highres'):
            pipeline = name_no_ext[:-(len('_highres'))]
        
        if not pipeline in data:
            data[pipeline] = {'json': '', 'screenshots': [], 'metadata': {}}

        if ext == 'json':
            data[pipeline]['json'] = get_direct_url(path)
            with open(path, 'r') as pipeline_json:
                pipeline_data = json.load(pipeline_json)
                data[pipeline]['metadata'] = pipeline_data.get('project')
        else:
            data[pipeline]['screenshots'].append(get_direct_url(path))

def get_direct_url(full_file):
    return 'https://raw.githubusercontent.com/google/visualblocks/main/{full_file}'.format(full_file=full_file)

main()