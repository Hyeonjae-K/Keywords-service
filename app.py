import time, atexit
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, render_template
app = Flask(__name__)


def print_date_time():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))


@app.route('/')
def hello():
    return render_template("index.html")


scheduler = BackgroundScheduler()
scheduler.add_job(func=print_date_time, trigger="interval", seconds=3)
scheduler.start()

if __name__ == '__main__':
    app.run()