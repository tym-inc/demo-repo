import schedule
import time

def main():
    schedule.every(1).seconds.do(job)
    schedule.every(5).seconds.do(less_frequent_job)

    while True:
        schedule.run_pending()
        time.sleep(100)


if __name__ == "__main__":
    main()
