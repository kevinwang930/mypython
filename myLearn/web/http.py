# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 11:40:12 2019

@author: kevin
"""
import requests
r = requests.get('https://pypi.org/')
r
r.status_code

r.headers
r.text
