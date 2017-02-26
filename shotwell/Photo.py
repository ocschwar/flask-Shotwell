#!flask/bin/python
"""
Todo: retrieve or create a Shotwell Database in 
order to run SqlSoup on it. 

Proceed from there. 
"""
import pprint
from flask import Flask, request, url_for
import csv, json, os, datetime

from flask_restful import Resource, Api, reqparse, abort
#from sqlalchemy.ext.hybrid import hybrid_property
import hashlib
from PIL import Image, ImageFilter, ExifTags
import sys
#import 
from shotwell import app, api, db

class Photo(db.Model):
    __tablename__ = 'PhotoTable'
    id = db.Column(db.Integer, primary_key=True,unique=True)
    filename = db.Column(db.String, unique=True,nullable=False,
                         doc="first filename in the DB"
    )
    width = db.Column(db.Integer)
    height = db.Column(db.Integer)
    # file stat
    filesize = db.Column(db.Integer)
    
    timestamp = db.Column(db.Integer)
    exposure_time = db.Column(db.Integer)
    orientation = db.Column(db.Integer)

    #?
    original_orientation = db.Column(db.Integer)
    
    import_id = db.Column(db.Integer)
    event_id = db.Column(db.Integer)
    transformations = db.Column(db.String)
    sha256 = db.Column(db.String)
    thumbnail_sha256 = db.Column(db.String)
    exif_sha256 = db.Column(db.String)
    time_created = db.Column(db.Integer)
    # default 0
    flags = db.Column(db.Integer, server_default='0')
    # default 0
    rating = db.Column(db.Integer, server_default='0')
    # default 0
    file_format = db.Column(db.Integer, server_default='0')
    title = db.Column(db.String)
    backlinks = db.Column(db.String)
    time_reimported = db.Column(db.Integer)
    # default -1
    editable_id = db.Column(db.Integer, server_default="-1")
    # default 0
    metadata_dirty= db.Column(db.Integer, server_default='0')
    developer = db.Column(db.String)
    # default -1
    develop_shotwell_id = db.Column(db.Integer, server_default="-1")
    # default -1
    develop_camera_id = db.Column(db.Integer, server_default="-1")
    # default -1
    develop_embedded_id = db.Column(db.Integer, server_default="-1")
    comment = db.Column(db.String)

    def __repr__(self):        
        return '<%s %r>' % (type(self),self.filename)

    def content(self):
        return open(self.filename).read()


def create_entry(path):
    im = Image.open(path)
    exif = dict([
        (ExifTags.TAGS[t],v)
        for (t,v) in 
        im._get_exif()])
    
    s = stat(path)
    print (exif)
    return

    P = Photo(
        filename=path,
        width = im.width,
        height=im.height,
        timestamp = exif.get(306),
        )
        
def main(args):
    for arg in args[1:]:
        create_entry(arg)


if __name__ == '__main__':
    # Entry point for script
    main(sys.argv)

