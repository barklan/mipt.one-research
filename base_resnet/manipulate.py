import os
import glob

os.chdir(r"train/notsolution2")
for index, oldfile in enumerate(glob.glob('*.JPEG'), start=1):
    newfile = f'{index}.jpg'
    os.rename (oldfile, newfile)

print('DONE!')