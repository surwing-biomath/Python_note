# PIL是用于图像处理的第三方库，它支持图像存储、处理和显示等操作
# 安装：pip install pillow
# jieba是Python中用于对中文进行分词的模块，它可以将一段中文文本分隔成中文词组的序列
# 安装：pip install jieba

# 使用PIL模块进行图像颜色的交换
from PIL import Image
# 加载图片
im = Image.open('Google.png')
# print(type(im), im)  # <class 'PIL.PngImagePlugin.PngImageFile'>
im = im.convert('RGB')  # Convert image to RGB format
# 提取图像的颜色通道，返回结果是一个包含三个通道的元组
# 分别对应红色、绿色和蓝色通道
r, g, b = im.split()
# print(type(r), r)  # <class 'PIL.Image.Image'>
# 合并颜色通道
om = Image.merge(mode='RGB', bands=(r, b, g))  
om.save('new_Google.png')  # 保存新图像