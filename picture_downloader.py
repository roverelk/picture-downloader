import time
import urllib.request
from itertools import product

url = "http://www.WEBPAGE.com/file-location/"
url_end = ".jpg"

folder = "FolderName/"

start_time = time.time()
counter = 0

chars = '0123456789abcdefghijklmnopqrstuvwxyz-_'  # chars to look for


def print_time():
    finish_time = time.time() - start_time

    hours   = int(finish_time / 360)
    minutes = int(finish_time / 60) - (hours * 60)
    seconds = finish_time - (minutes * 60) - (hours * 60 * 60)

    print("%s:%s:%s" % (hours, minutes, seconds))


def run():
    for length in range(1, 5):  # only do lengths of 1 to 5
        to_attempt = product(chars, repeat=length)

        for attempt in to_attempt:
            try:
                urllib.request.urlretrieve(url + ''.join(attempt) + url_end, folder + ''.join(attempt) + url_end)
                counter = counter + 1
            except:
                counter = counter + 1

            if counter % 50 == 0:
                print_time()
                print(url + ''.join(attempt) + url_end)

        time.sleep(5)   # Without this it may overload the web page with requests.


run()
