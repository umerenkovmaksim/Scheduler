import datetime
import threading

from plyer import notification


class TimerManager:
    def __init__(self):
        self.timers = []

    def add_timer(self, timer):
        self.timers.append(timer)

    def remove_timer(self, timer):
        self.timers.remove(timer)

    def cancel_timers(self):
        for timer in self.timers:
            if timer.timer:
                timer.timer.cancel()
        self.timers.clear()


class NotificationThread:

    def __init__(self, task, add_time=0):
        self.task = task
        self.add_time = add_time
        self.timer = None
        self.start()

    def start(self):
        date_and_time = tuple(map(int, self.task[2].split('-')[::-1] + self.task[3].split(':')))
        self.notify_time = datetime.datetime(*date_and_time)
        time_delta = (self.notify_time - datetime.datetime.now()).total_seconds()
        if time_delta > 0 and not self.task[4]:
            self.timer = threading.Timer(time_delta - self.add_time * 60, self.send_notification)
            print(time_delta)
            self.timer.setName('Планировщик задач')
            self.timer.start()

    def send_notification(self):
        notification.notify(
            title="Напоминание",
            message=f'''На {self.task[3]} у вас поставлено напоминание {self.task[1]}''',
            timeout=120
        )
