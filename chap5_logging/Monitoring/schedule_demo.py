import schedule
import time

def job1():
    print("JOB1")

def job2():
    print("JOB2")

schedule.every(1).minutes.do(job1)
schedule.every(10).seconds.do(job2)

while True:
    schedule.run_pending()
    time.sleep(5)

print("end")