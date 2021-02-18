import string
import random
import time

def random_string(string_len):
    char_list = string.ascii_uppercase + string.digits
    return ''.join(random.choice(char_list) for i in range(string_len))


sites = ["Google", "Nate", "Zum", "Dreamwiz", "KOREA.COM"]
date = time.strftime("%Y%m%d")

for hour in range(24):
    for site in sites:
        path = "./data/{site}/{date}.txt".format(site=site, date=date)
        f = open(path, "a", encoding="utf-8")
        f.write("%02d시\n" % hour)

        for rank in range(10):
            title = random_string(random.randint(1, 10))
            url = random_string(random.randint(20, 50))
            f.write(title + " " + url + "\n")