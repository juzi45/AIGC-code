
# 导入所需的库
import os
import skimage.io
import skimage.metrics
import skimage.color
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# 定义两个文件夹的路径，你可以修改成你自己的路径
folder1_path = "./流萤/"
folder2_path = "./fy/"


# 定义相似度的阈值，越大越宽松
threshold = 0.9

# 创建一个字典，存储图片的文件名和图片对象
image_dict = {}

# 遍历第一个文件夹中的所有图片
for filename in os.listdir(folder1_path):
    # 如果是图片文件，就读取它
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image = skimage.io.imread(folder1_path + filename)
        # 转换图片为灰度图
        gray_image = skimage.color.rgb2gray(image)
        # 把文件名和图片对象存入字典
        image_dict[filename] = gray_image

# 遍历第二个文件夹中的所有图片
for filename in os.listdir(folder2_path):
    # 如果是图片文件，就读取它
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image = skimage.io.imread(folder2_path + filename)
        # 转换图片为灰度图
        gray_image = skimage.color.rgb2gray(image)
        # 把文件名和图片对象存入字典
        image_dict[filename] = gray_image

# 创建一个列表，存储重复的图片的文件名
duplicates = []

# 遍历字典中的所有键值对
for file1, image1 in image_dict.items():
    # 再次遍历字典中的所有键值对
    for file2, image2 in image_dict.items():
        # 如果两个文件名不同，但是SSIM值高于阈值，就认为是相似的图片
        if file1 != file2 and skimage.metrics.structural_similarity(image1, image2) > threshold:
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
    os.remove(folder2_path + file)
    print(f"已删除{file}")
