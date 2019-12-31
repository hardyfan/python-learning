from osconfeed import load


if __name__ == '__main__':
    feed = load()
    print(sorted(feed['Schedule'].keys()))

    for key, value in sorted(feed['Schedule'].items()):
        print(f'{len(value):3} {key}')

    print(feed['Schedule']['speakers'][-1]['name'])
    print(feed['Schedule']['speakers'][-1]['serial'])
    print(feed['Schedule']['events'][40]['name'])
    print(feed['Schedule']['events'][40]['speakers'])