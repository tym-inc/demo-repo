import schedule
import time



def test():
    print('hi')



def less_frequent_job():
    print("I'm working... occassionally...")

def main():
    schedule.every(1).seconds.do(job)
    schedule.every(5).seconds.do(less_frequent_job)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
