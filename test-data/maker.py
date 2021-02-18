import string
import random
import csv


def random_string(string_len):
    char_list = string.ascii_uppercase + string.digits
    return ''.join(random.choice(char_list) for i in range(string_len))


sites = ["Google", "Nate", "Zum", "Dreamwiz", "KOREA.COM"]
f = open("./data/test.txt", "a", encoding="utf-8")

for hour in range(24):
    f.write("{time:02d}\n".format(time=hour))

    for site in sites:
        f.write(site+"\n")

        for rank in range(10):
            title = random_string(random.randint(1, 10))
            url = random_string(random.randint(20, 50))

            f.write(title + " " + url + "\n")

    f.write("\n")