import os
import exifread

if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(BASE_DIR)
    path_name = os.path.join(BASE_DIR, 'statics\images\loncol.jpg')
    f = open(path_name, 'rb')
    tags = exifread.process_file(f)
    print(tags)

