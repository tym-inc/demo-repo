import sched
import time


def print_time(a='default'):
    print("From print_time", time.time(), a)


def print_some_times(s: sched.scheduler):
    print(time.time())
    s.enter(10, 1, print_time)
    s.enter(5, 2, print_time, argument=('positional',))
    s.enter(5, 1, print_time, kwargs={'a': 'keyword'})
    s.run()


def main():
    s = sched.scheduler(time.time, time.sleep)
    print_some_times(s)


if __name__ == "__main__":
    main()
