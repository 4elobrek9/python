import schedule
import time
def job():
    print("Task is running...")
schedule.every(10).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)