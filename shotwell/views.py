#!flask/bin/python
import datetime
import glob
import pprint
import json
import os
import random, string
import base64
from flask import Flask, request, make_response, render_template, send_from_directory, Response
from flask import flash, redirect, session, url_for, g
from flask_restful import Resource, Api, reqparse, abort
from werkzeug import secure_filename
from shotwell import app, api, Photo

class PhotoList(Resource):
    """
    Listing, adding, searching photos. 
    """
    def get(self,):
        pass

    def post(self,):
        pass

    def delete(self,):
        pass
    pass

class Photo(Resource):
    """
    Photo Metadata.
    """
    def patch(self, photo_id):
        pass
    
    def get(self,photo_id):
        pass
    pass

class PhotoContent(Resource):
    """
    Photo content.
    """
    def get(self,photo_id):
        pass
    
    def put(self,photo_id):
        pass
    pass

api.add_resource(PhotoList,'/photo','/Photo')
api.add_resource(Photo,'/photo/<photo_id>','/Photo/<photo_id>')
@app.route('/')
def index():
    return render_template('index.html',
                           title="Flask Shotwell")

