# 导入所需的库
import os
import imagehash
from PIL import Image

# 定义工作路径

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 定义两个文件夹的路径，你可以修改成你自己的路径
folder1_path = "D:/Users/juzi45/Pictures/fy/"
folder2_path = "D:/Users/juzi45/Pictures/流萤/"

# 定义相似度的阈值，越小越严格
threshold = 5

# 创建一个字典，存储图片的文件名和哈希值
hash_dict = {}

# 遍历第一个文件夹中的所有图片
for filename in os.listdir(folder1_path):
    # 如果是图片文件，就打开它
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image = Image.open(folder1_path + filename)
        # 计算图片的哈希值
        image_hash = imagehash.phash(image)
        # 把文件名和哈希值存入字典
        hash_dict[filename] = image_hash

# 遍历第二个文件夹中的所有图片
for filename in os.listdir(folder2_path):
    # 如果是图片文件，就打开它
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image = Image.open(folder2_path + filename)
        # 计算图片的哈希值
        image_hash = imagehash.phash(image)
        # 把文件名和哈希值存入字典
        hash_dict[filename] = image_hash

# 创建一个列表，存储重复的图片的文件名
duplicates = []

# 遍历字典中的所有键值对
for file1, hash1 in hash_dict.items():
    # 再次遍历字典中的所有键值对
    for file2, hash2 in hash_dict.items():
        # 如果两个文件名不同，但是哈希值的差异小于阈值，就认为是重复的图片
        if file1 != file2 and (hash1 - hash2) < threshold:
            # 把其中一个文件名加入重复列表
            duplicates.append(file1)

# 去除重复列表中的重复元素
duplicates = list(set(duplicates))

# 打印重复图片的数量和文件名
print(f"找到了{len(duplicates)}张重复的图片：")
for file in duplicates:
    print(file)

# 删除重复的图片
for file in duplicates:
    os.remove(folder1_path + file)
    # os.remove(folder2_path + file)
    print(f"已删除{file}")
