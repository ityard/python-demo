import stylecloud, pandas as pd
from IPython.display import Image

df = pd.read_csv("comments.csv")

# 整体词云
cts_list = df.iloc[:, 2]
cts_str ="".join([str(i) for i in cts_list])
stylecloud.gen_stylecloud(text=cts_str, max_words=400,
                          collocations=False,
                          font_path="SIMLI.TTF",
                          icon_name="fas fa-home",
                          size=800,
                          output_name="total.png")
Image(filename="total.png")

# 热门评论
hot_str = ""
for index, row in df.iterrows():
    content = row[2]
    support = row[6]
    reply = row[7]
    if(support > 30):
        hot_str += content
    elif (reply > 5):
        hot_str += content
stylecloud.gen_stylecloud(text=hot_str, max_words=200,
                          collocations=False,
                          font_path="SIMLI.TTF",
                          icon_name="fas fa-fire",
                          size=800,
                          output_name="hot.png")
Image(filename="hot.png")