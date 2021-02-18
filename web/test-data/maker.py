import string
import random
import csv


def random_string(string_len):
    char_list = string.ascii_uppercase + string.digits
    return ''.join(random.choice(char_list) for i in range(string_len))


sites = ["Google", "Nate", "Zum", "Dreamwiz", "KOREA.COM"]

for hour in range(24):
    dataDic = {}
    for site in sites:
        dataList = []
        for rank in range(10):
            dataList.append(random_string(random.randint(2, 10)))