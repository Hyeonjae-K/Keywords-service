from flask import Flask, render_template
import time
app = Flask(__name__)
sites = {}
data = {}


def get_sites():
    with open("./test-data/data/sites.txt", "r", encoding="UTF-8") as f:
        while True:
            site, space, url = f.readline().strip().rpartition(" ")
            if site == "":
                break
            sites[site] = url


def get_data():
    date = time.strftime("%Y%m%d")
    for site in sites:
        data[site] = {}
        path = f"./test-data/data/{site}/{date}.txt".format(site=site, date=date)
        with open(path, "r", encoding="UTF-8") as f:
            while True:
                data_time = f.readline().strip()
                if data_time == "":
                    break
                titles = []
                urls = []
                for i in range(10):
                    title, space, url = f.readline().strip().rpartition(" ")
                    titles.append(title)
                    urls.append(url)
                data[site].update({data_time: [titles, urls]})
    print(data)


@app.route('/')
def index():
    get_data()
    return render_template("test.html", data=data, sites=sites)


get_sites()
get_data()

if __name__ == '__main__':
    app.run()