import kagglehub
import os

# # Download latest version
# path = kagglehub.dataset_download("gopalbhattrai/pascal-voc-2012-dataset")

# print("Path to dataset files:", path)

path = '/Users/jyxc-dz-0101053/.cache/kagglehub/datasets/gopalbhattrai/pascal-voc-2012-dataset/versions/1/VOC2012_train_val/VOC2012_train_val/JPEGImages'

image_name = []
for file in os.listdir(path):
    image_name.append(file.split('.')[0].split('_')[1])

path = '/Users/jyxc-dz-0101053/.cache/kagglehub/datasets/gopalbhattrai/pascal-voc-2012-dataset/versions/1/VOC2012_test/VOC2012_test/JPEGImages'
for file in os.listdir(path):
    image_name.append(file.split('.')[0].split('_')[1])

print(len(image_name), image_name[0])

# 读取sampled_pascal.csv文件
import csv
A, B = 0, 0
with open('sampled_pascal.csv', 'r') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        if row[0].split('.')[0] in image_name:
            print('Yes')
            A += 1
        else:
            print(row[0].split('.')[0])
            B += 1

print(A, B)
