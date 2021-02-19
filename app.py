# import time
# from flask import Flask, render_template
#
#
# app = Flask(__name__)
# sites_dic = {}
# data_dic = {}
#
#
# def set_sites():
#     with open('./test-data/data/sites.txt', 'r', encoding='utf-8') as f:
#         while True:
#             site, space, url = f.readline().strip().rpartition(" ")
#             if site == '':
#                 break
#             sites_dic[site] = {"url": url}
#
#
# def set_data():
#     date = time.strftime("%Y%m%d")
#     for site in sites_dic:
#         path = f'./test-data/data/{site}/{date}.txt'.format(site=site, date=date)
#         data_dic[site] = {}
#         with open(path, "r", encoding="utf-8") as f:
#             while True:
#                 data_time = f.readline().strip()
#                 titles = []
#                 urls = []
#                 if data_time == '':
#                     break
#                 for i in range(10):
#                     title, space, url = f.readline().strip().rpartition(" ")
#                     titles.append(title)
#                     urls.append(url)
#                 data_dic[site][data_time] = [titles, urls]
#
#
# @app.route('/')
# def index():
#     set_data()
#     return render_template("test.html", sites=sites_dic)
#
#
# if __name__ == '__main__':
#     set_sites()
#     app.run()


from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("test.html", name="string")


if __name__ == '__main__':
    app.run()
