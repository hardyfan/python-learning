from datetime import datetime
import os


if __name__ == '__main__':
    pwd = os.path.abspath('.')
    print(f'pwd={pwd}')
    print('Size         Last Modified          Name')
    print('-------------------------------------------------------')
    for f in os.listdir(pwd):
        size = os.path.getsize(f)
        mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
        flag = '/' if os.path.isdir(f) else ''
        print('%10d    %s   %s  %s' % (size, mtime, f, flag))
