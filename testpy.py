
import os
import json

with open("pipelines_index.json", "w") as json_file:
    data = []
    for root, _, files in os.walk('pipelines'):
        for file in files:
            data.append({
                name: str(root+file)
            })
    json.dump(data, json_file, ensure_ascii=False)

