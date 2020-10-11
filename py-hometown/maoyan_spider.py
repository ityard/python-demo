import requests, json, time, re, datetime, pandas as pd

# 获取页面内容
def get_page(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'
                      '/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        'accept': '*/*'
    }
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        return r.text
    except requests.HTTPError as e:
        print(e)
    except requests.RequestException as e:
        print(e)
    except:
        print("出错了")

# 解析接口返回数据
def parse_data(html):
    json_data = json.loads(html)['cmts']
    comments = []
    # 解析数据并存入数组
    try:
        for item in json_data:
            comment = []
            comment.append(item['nickName']) # 昵称
            comment.append(item['cityName'] if 'cityName' in item else '') # 城市
            comment.append(item['content'].strip().replace('\n', '')) # 内容
            comment.append(item['score']) # 星级
            comment.append(item['startTime'])
            comment.append(item['time']) # 日期
            comment.append(item['approve']) # 赞数
            comment.append(item['reply']) # 回复数
            if 'gender' in item:
                comment.append(item['gender'])  # 性别
            comments.append(comment)
        return comments
    except Exception as e:
        print(comment)
        print(e)

# 保存数据，写入 csv
def save_data(comments):
    filename = 'comments.csv'
    dataObject = pd.DataFrame(comments)
    dataObject.to_csv(filename, mode='a', index=False, sep=',', header=False, encoding='utf_8_sig')

# 爬虫主函数
def main():
    # 当前时间
    start_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # 电影上映时间
    end_time = '2020-10-01 00:00:00'
    while start_time > end_time:
        url = 'http://m.maoyan.com/mmdb/comments/movie/1328712.json?_v_=yes&offset=0&startTime=' \
              + start_time.replace('  ', '%20')
        html = None
        print(url)
        try:
            html = get_page(url)
        except Exception as e:  # 如果有异常,暂停一会再爬
            time.sleep(1)
            html = get_page(url)
        time.sleep(0.5)
        comments = parse_data(html)
        start_time = comments[14][4]  # 获取每页中最后一条评论时间,每页有15条评论
        #print(start_time)
        # 最后一条评论时间减一秒，避免爬取重复数据
        start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d  %H:%M:%S') + datetime.timedelta(seconds=-1)
        start_time = datetime.datetime.strftime(start_time, '%Y-%m-%d  %H:%M:%S')
        print(start_time)
        save_data(comments)

if __name__ == '__main__':
    main()