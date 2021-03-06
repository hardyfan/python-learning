import threading


def thread_job():
    print('This is a thread of %s' % threading.current_thread())


def main():
    thread = threading.Thread(target=thread_job,)
    thread.start()


if __name__ == '__main__':
    print(threading.active_count())
    print(threading.enumerate())
    print(threading.current_thread())

    main()
