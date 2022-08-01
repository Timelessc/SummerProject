# 导入词云库
from wordcloud import WordCloud,STOPWORDS
# 导入图像处理库
import PIL.Image as image
# 导入数据处理库
import numpy as np
# 导入结巴分词库
import jieba
# 分词模块
# 导入文本文件,进行分词,制作词云
with open("comments.txt",'r',encoding='utf-8') as f:
    text = f.read()
    print('666',text)

# 将读取的中文文档进行分词
word_list = jieba.lcut(text, cut_all=True)  # 三种模式：精确模式（默认效果）、全模式（True）、搜索引擎模式
print(word_list)
# 分词后在单独个体之间加上空格
text = " ".join(word_list)      # join将列表中的字符串给拼接起来

print(text)

# 过滤器(拓展1)  目的是将单独一个文字的字符串去掉，因为一个字不是词
filter = []
for s in word_list:
    if len(s) <= 1:
        filter.append(s)

print(filter)
# 设置词云形状
mask = np.array(image.open("../image/model/china.jpg"))
# 自定义词云 创建词云对象
wordcloud = WordCloud(relative_scaling='auto',          # 词频和字体大小的关联性，设置成自动
                      stopwords=filter,                 # 指定词云的排除词列表，即不显示的单词列表
                      mask=mask,                        # 指定词云图形状，默认为长方形
                      background_color='white',         # 背景颜色
                      scale=2,                          # 按照比例进行放大画布
                      font_path="../font/font1.ttf",       # 设置字体
                      width=900,                        # 设置宽
                      height=700)                       # 设置高
# 注入文字，加载文本
wd = wordcloud.generate(text)
# 保存图片  将词云图输出为图像文件，必须为.png或者.jpg格式的图片
pic_obj = wd.to_file("../image/load/myPic.jpg")

# 返回对象  产生词云图图片
image_produce = wd.to_image()
# 显示图像
image_produce.show()