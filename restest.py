# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 17:10:41 2019

@author: USER
"""

import time
import resource


print(time.localtime())

maxsize = 500000000 # In bytes
try:
    softas, hardas = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (maxsize, hardas))
    new_soft, new_hard = resource.getrlimit(resource.RLIMIT_AS)
    print('For Address space: ', '\n', 'Soft is: ', new_soft, '\n', 'Hard is: ', new_hard)
finally:
    softrss, hardrss = resource.getrlimit(resource.RLIMIT_RSS)
    resource.setrlimit(resource.RLIMIT_RSS, (maxsize, hardrss))
    news_rss, newh_rss = resource.getrlimit(resource.RLIMIT_RSS)
    print('\n', 'For RSS: ', '\n', 'Soft is: ', news_rss, '\n', 'Hard is: ', newh_rss)
  
