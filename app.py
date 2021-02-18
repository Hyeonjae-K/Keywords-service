import time
# from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, render_template


app = Flask(__name__)
sites = {}
data = {}


def set_sites():
    with open('./test-data/data/sites.txt', 'r', encoding='utf-8') as f:
        while True:
            title, space, url = f.readline().strip().rpartition(" ")
            if title == '':
                break
            sites[title] = url


def set_data():
    data.clear()
    date = time.strftime("%Y%m%d")

    for site in sites:
        path = "./test-data/data/{site}/{date}.txt".format(site=site, date=date)
        data[site] = {}

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

                    data[site].update({rec_time: [titles, urls]})


@app.route('/')
def index():
    set_data()
    print(data)
    print(sites)
    return render_template("index.html", data=data, sites=sites)


# scheduler = BackgroundScheduler()
# scheduler.add_job(func=set_data, trigger="interval", minutes=1)
# scheduler.start()

if __name__ == '__main__':
    set_sites()
    app.run()