import schedule
import time


def job():
    print("I'm working...")


def less_frequent_job():
    print("I'm working... occassionally...")


def main():
    schedule.every(2).seconds.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
