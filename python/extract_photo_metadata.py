
import glob
import shutil
import sys

import exifread

pics = sorted(glob.glob('./*.jpg'))
for p in pics:
    with open(p, 'rb') as f:
        tags = exifread.process_file(f)
        datetime = str(tags['EXIF DateTimeOriginal'])
        datetime = datetime.replace(' ', '__').replace(':', '_')
        print datetime
        shutil.copy(p, 'sorted/pic_%s.jpg' % datetime)
