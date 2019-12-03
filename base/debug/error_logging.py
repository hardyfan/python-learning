import logging

try:
    print('try...')
    r = 10/0
    print('result:', r)
except ZeroDivisionError as e:
    logging.exception(e)
finally:
    print('finally...')
print('END')