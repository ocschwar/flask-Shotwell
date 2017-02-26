#!flask/bin/python
"""
Todo: retrieve or create a Shotwell Database in 
order to run SqlSoup on it. 

Proceed from there. 
"""
import pprint

import hashlib
from PIL import Image, ImageFilter, ExifTags
import sys, os



def create_entry(path):
    im = Image.open(path)
    exif = dict([
        (ExifTags.TAGS[t],v)
        for (t,v) in 
        im._getexif().items()])
    
    s = os.stat(path)
    pprint.pprint (exif)

    P = {
        "filename":path,
        "width":im.width,
        "height":im.height,
        "timestamp": exif.get("DateTimeOriginal"),
        "exposure_time":exif.get("ExposureTime"),
        "orientation":exif.get("Orientation"),
        }
    pprint.pprint(P)
        # = exif.get(306),
        #    )
        
def main(args):
    for arg in args[1:]:
        create_entry(arg)


if __name__ == '__main__':
    # Entry point for script
    main(sys.argv)

