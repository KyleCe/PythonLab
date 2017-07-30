import os

cwd = os.getcwd()
to_process_dir = '/Users/elex/Pictures/GC_sources'
mPicExtent = '.png'


def task():
    for root, dirs, fileList in os.walk(to_process_dir):
        for f in fileList:
            if f.endswith(mPicExtent):
                f_with_path = to_process_dir + os.pathsep + f
                os.rename(f_with_path, f_with_path[:-mPicExtent.__len__()])


task()
