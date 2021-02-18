import time
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, render_template


app = Flask(__name__)
sites = ["Google", "Nate", "Zum", "Dreamwiz", "KOREA.COM"]
dic = {}


def set_data():
    dic.clear()
    date = time.strftime("%Y%m%d")

    for site in sites:
        path = "./test-data/data/{site}/{date}.txt".format(site=site, date=date)
        times = []
        titles = []
        urls = []

        with open(path, "r", encoding="utf-8") as f:
            while True:
                rec_time = f.readline().strip()
                if rec_time == '':
                    break
                else:
                    times.append(rec_time)
                    for i in range(10):
                        title, space, url = f.readline().strip().rpartition(" ")
                        titles.append(title)
                        urls.append(url)

        dic[site] = [times, titles, urls]


@app.route('/')
def index():
    set_data()
    return render_template("index.html", data=dic)


# scheduler = BackgroundScheduler()
# scheduler.add_job(func=set_data, trigger="interval", minutes=1)
# scheduler.start()

if __name__ == '__main__':
    app.run()