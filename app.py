from celery import Celery
from celery.schedules import crontab

app = Celery("tasks", broker='redis://127.0.0.1/1', backend="redis://127.0.0.1/2")
CELERY_TIMEZONE = 'Asia/Shanghai'
app.conf.timezone = CELERY_TIMEZONE
@app.on_after_configure.connect
def setup(sender, **kwargs):
    sender.add_periodic_task(
        crontab(hour=20, minute='*'),
        add.s(1,2)
    )

@app.task
def add(x,y):
    print("ok!! x=%s y=%s"%(x,y))
    return x+y




