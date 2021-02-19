import time
# from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, render_template


app = Flask(__name__)
data_dic = {}


def set_data():
    with open('./test-data/data/sites.txt', 'r', encoding='utf-8') as f:
        while True:
            site, space, url = f.readline().strip().rpartition(" ")
            if site == '':
                break
            data_dic[site] = {"url": url}
    date = time.strftime("%Y%m%d")
    for site in data_dic:
        path = './test-data/data/{site}/{date}.txt'.format(site=site, date=date)
        with open(path, "r", encoding="utf-8") as f:
            while True:
                data_time = f.readline().strip()
                titles = []
                urls = []
                if data_time == '':
                    break
                for i in range(10):
                    title, space, url = f.readline().strip().rpartition(" ")
                    titles.append(title)
                    urls.append(url)
                data_dic[site][data_time] = {"titles": titles, "urls": urls}


@app.route('/')
def index():
    set_data()
    return render_template("test.html", data=data_dic)


# scheduler = BackgroundScheduler()
# scheduler.add_job(func=set_data, trigger="interval", minutes=1)
# scheduler.start()

if __name__ == '__main__':
    app.run()