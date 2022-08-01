# 导入词云库
from wordcloud import WordCloud,STOPWORDS
# 导入图像处理库
import PIL.Image as image
# 导入数据处理库
import numpy as np
# 导入jieba库  用来分词的
import jieba

# 导入文本文件，进行分词
with open('comments.txt','r',encoding='utf-8') as f:
    text = f.read()
    print(text)

# 将读取的文本进行分词
word_list = jieba.lcut(text,cut_all=True)
print(word_list)

# 分词之后在单独的词语之间加上空格
text = ' '.join(word_list)
print(text)

# 筛选出单个的字
filter = []     # 创建一个空列表
for s in word_list:
    if len(s)<=1:
        filter.append(s)

# 设置词云图的形状
mask = np.array(image.open('../image/model/china.jpg'))

# 自定义词云图，也就是创建词云图的对象
wordcloud = WordCloud(relative_scaling='auto',  # 设置词频和字体大小的关联性
                      stopwords=filter,    # 指定不显示的字
                      mask = mask,
                      background_color= 'white',
                      scale=1,      # 按照比例进行放大图片
                      font_path="../font/font1.ttf",    # 设置字体
                      width=900,
                      height=700)

# 注入文字，加载文本
wd = wordcloud.generate(text)

# 生成词云图的结果图片，并保存在文件夹中
pic_obj = wd.to_file('../image/load/myPic.jpg')

# 产生词云图图片
image_produce = wd.to_image()
image_produce.show()

