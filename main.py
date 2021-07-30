import schedule
import time


def experimental_function(experiment):
    print("experiment: {experiment}")
    return experiment

def another_experiment():
    print("I'm working... occassionally...")


def less_frequent_job():
    print("I'm working... occassionally...")


def main():
    schedule.every(1).seconds.do(job)
    schedule.every(5).seconds.do(less_frequent_job)

    while True:
        schedule.run_pending()
        time.sleep(100)


if __name__ == "__main__":
    main()
