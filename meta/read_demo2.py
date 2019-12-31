from osconfeed import load
from explore0 import FrozenJSON


if __name__ == '__main__':
    raw_feed = load()
    feed = FrozenJSON(raw_feed)

    print(len(feed.Schedule.speakers))
    print(feed.Schedule.keys())

    for key, value in sorted(feed.Schedule.items()):
        print(f'{len(value):3} {key}')

    print(feed.Schedule.speakers[-1].name)
    talk = feed.Schedule.events[40]
    print(type(talk))
    print(talk.name)
    print(talk.speakers)
    # print(talk.flavor)

    grad = FrozenJSON({'name': 'hardy', 'class': 1996})
    print(f'name = {grad.name}, class = {getattr(grad, "class")}')
