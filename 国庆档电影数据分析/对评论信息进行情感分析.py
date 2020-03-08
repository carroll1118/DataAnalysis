import pandas as pd
from snownlp import SnowNLP

#该方法的作用就是将评论进行情感分析
def convert(comment):
    snow = SnowNLP(str(comment))
    sentiments = snow.sentiments  #0(消极)~1(积极)
    return sentiments
if __name__ == '__main__':
    data = pd.read_csv('./climb.csv','\t')

    #获取评论数据
    #DataFrame的apply()方法默认作用于DataFrame的各列.
    data['情感评分'] = data.comment.apply(convert)
    data.sort_values(by = '情感评分',ascending=False,inplace=True)

    data.to_csv('./climb_snownlp.csv',sep='\t',index=False)