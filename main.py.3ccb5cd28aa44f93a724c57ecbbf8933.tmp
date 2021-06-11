import schedule
import time


def job():
    print("I'm working...")


def main():
    schedule.every(10).seconds.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == "__main__":
    main()
