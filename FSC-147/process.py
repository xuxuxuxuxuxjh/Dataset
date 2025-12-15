# 读取test.json文件
import json

with open('test.json', 'r') as f:
    data = json.load(f)

data_new = []
for i, item in enumerate(data):
    data_new.append({
        'id': i,
        'image': item['image'],
        'question': item['question'],
        'answer': item['answer']
    })

print(data_new)

with open('data.json', 'w') as f:
    json.dump(data_new, f, ensure_ascii=False, indent=4)