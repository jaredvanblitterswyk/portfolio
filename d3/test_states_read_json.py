# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 15:20:40 2021

@author: Jared
"""

import json
  
# Opening JSON file
with open('states-10m.json','r') as f:
    # returns JSON object as 
    # a dictionary
    data = json.load(f)