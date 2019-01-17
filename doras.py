# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 23:00:25 2018

@author: USER
"""

from flask import Flask


app = Flask(__name__)
mount_type = None
#page_type = None


@app.route('/')
def home_view():
    return 'hello world'
   

