import time
import requests


def requests_infomation():
    URL = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
    rest = requests.get(URL)
    json_rest = rest.json()
    json_list = json_rest[0:30]  # 1ページ分表示
    for item in json_list:
        time.sleep(1)
        try:
            title_info = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{item}.json?print=pretty").json()
            print(f"title : {title_info['title']}, link : {title_info['url']}")
        except KeyError:
            print("エラー箇所")
        time.sleep(1)


def main():
    requests_infomation()
    time.sleep(1)


if __name__ == '__main__':
    start = time.time()  # 開始時間
    main()
    print(time.time() - start)  # 終了時間-開始時間＝かかった時間
