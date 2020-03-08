import pandas as pd
import jieba
from PIL import Image
from jieba import analyse
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import wordcloud

if __name__ == '__main__':
    data = pd.read_csv('./climb.csv',sep='\t')
    #获取评论信息
    comments = ';'.join([str(c) for c in data['comment'].tolist()])

    #使用jiebe进行分词
    gen = jieba.cut(comments)
    words = ' '.join(gen)

    #分好的词，进行jieba分析
    tags = analyse.extract_tags(words,topK=500,withWeight=True)
    word_result = pd.DataFrame(tags,columns=['词语','重要性'])
    word_result.sort_values(by='重要性',ascending=False,inplace=True)


    #数据可视化
    plt.barh(y = np.arange(0, 20),width =word_result[:20]['重要性'][::-1])
    plt.ylabel('Importance')
    #print(word_result[:20]['词语'][::-1])
    plt.yticks(np.arange(0,20),word_result[:20]['词语'][::-1], fontproperties ='KaiTi')
    # 保存条形图,!!!保存代码一定要写到plt.show()之前
    plt.savefig('./条形图_20keywords.jpg', dpi=200)
    plt.show()

    # 词云操作，pip install wordcould
    mountain = np.array(Image.open('./山.jpg'))  # 词云图片
    # 将tags，jieba分词提取出来数据，dict字典
    words = dict(tags)
    cloud = wordcloud.WordCloud(width=1200, height=968, font_path='./simkai.ttf', background_color='white',
                                mask=mountain, max_words=500, max_font_size=150)
    # 词云
    word_cloud = cloud.generate_from_frequencies(words)
    plt.figure(figsize=(12, 12))
    plt.imshow(word_cloud)
    # 词云保存
    plt.savefig('./攀登者_词云.jpg', dpi=200)
    plt.show()
