from threading import Thread
from time import sleep
from datetime import datetime

from backend.models import File


def refresh():
    while True:
        now = datetime.now()
        for f in File.objects.filter(expiry__lte=now):
            # print("deleted " + f.url)
            f.delete()
        sleep(1800)


def start(*args, **kwargs):
    t = Thread(target=refresh, args=args, kwargs=kwargs)
    t.daemon = True
    t.start()

