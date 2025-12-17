import kagglehub
import os
import shutil
import json

# Download latest version
# path = kagglehub.dataset_download("zaraks/pascal-voc-2007")

path = '/Users/jyxc-dz-0101053/.cache/kagglehub/datasets/zaraks/pascal-voc-2007/versions/1/VOCtest_06-Nov-2007/VOCdevkit/VOC2007/JPEGImages'

image_name = []
for file in os.listdir(path):
    image_name.append(file)

path = '/Users/jyxc-dz-0101053/.cache/kagglehub/datasets/zaraks/pascal-voc-2007/versions/1/VOCtrainval_06-Nov-2007/VOCdevkit/VOC2007/JPEGImages'
for file in os.listdir(path):
    image_name.append(file)

print(len(image_name), image_name[0])

os.makedirs('images', exist_ok=True)

# 读取sampled_pascal.csv文件，匹配上的图片保存到/images目录下
import csv
new_data = []
with open('sampled_pascal.csv', 'r') as f:
    reader = csv.reader(f)
    id = 0
    for i, row in enumerate(reader):
        if row[0] in image_name:
            # save image
            path = '/Users/jyxc-dz-0101053/.cache/kagglehub/datasets/zaraks/pascal-voc-2007/versions/1/VOCtrainval_06-Nov-2007/VOCdevkit/VOC2007/JPEGImages'

            for file in os.listdir(path):
                if file == row[0]:
                    shutil.copy(os.path.join(path, file), 'images')
                    new_data.append({
                        'id': id,
                        'image': file,
                        'question': f"How many {row[1]} are visibile in the image?",
                        'answer': row[2]
                    })
                    id += 1
                    break

            path = '/Users/jyxc-dz-0101053/.cache/kagglehub/datasets/zaraks/pascal-voc-2007/versions/1/VOCtest_06-Nov-2007/VOCdevkit/VOC2007/JPEGImages'
            for file in os.listdir(path):
                if file == row[0]:
                    shutil.copy(os.path.join(path, file), 'images')
                    new_data.append({
                        'id': id,
                        'image': file,
                        'question': f"How many {row[1]} are visibile in the image?",
                        'answer': row[2]
                    })
                    id += 1
                    break
        else:
            print(row[0])

# import shutil
# with open('data.json', 'w') as f:
#     json.dump(new_data, f, ensure_ascii=False, indent=4)

# # from datasets import load_dataset

# # ds = load_dataset("merve/pascal-voc")

# # print(ds['train'][0])

# # image_name = []
# # for i, item in enumerate(ds['train']):
# #     image_name.append(ds['train'][i]['text'])
# # for i, item in enumerate(ds['validation']):
# #     image_name.append(ds['validation'][i]['text'])

# # print(len(image_name))

# # import csv
# # new_data = []
# # with open('sampled_pascal.csv', 'r') as f:
# #     reader = csv.reader(f)
# #     id = 0
# #     for i, row in enumerate(reader):
# #         for y in ['2012']:
# #             if y + '_' + row[0].split('.')[0] in image_name:
# #                 print('Yes', y + '_' + row[0].split('.')[0])
# #             else:
# #                 print(row[0].split('.')[0])