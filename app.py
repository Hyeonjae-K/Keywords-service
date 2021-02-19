import time
# from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, render_template


app = Flask(__name__)
sites_dic = {}
data_dic = {}


def set_sites():
    with open('./test-data/data/sites.txt', 'r', encoding='utf-8') as f:
        while True:
            title, space, url = f.readline().strip().rpartition(" ")
            if title == '':
                break
            sites_dic[title] = url


def set_data():
    data_dic.clear()
    date = time.strftime("%Y%m%d")

    for site in sites_dic:
        path = "./test-data/data/{site}/{date}.txt".format(site=site, date=date)
        data_dic[site] = {}

        with open(path, "r", encoding="utf-8") as f:
            while True:
                rec_time = f.readline().strip()
                titles = []
                urls = []

                if rec_time == '':
                    break
                else:
                    for i in range(10):
                        title, space, url = f.readline().strip().rpartition(" ")
                        titles.append(title)
                        urls.append(url)

                    data_dic[site].update({rec_time: [titles, urls]})


@app.route('/')
def index():
    set_data()
    print(sites_dic)
    print(data_dic)
    return render_template("test.html", data=data_dic)


# scheduler = BackgroundScheduler()
# scheduler.add_job(func=set_data, trigger="interval", minutes=1)
# scheduler.start()

if __name__ == '__main__':
    set_sites()
    app.run()