# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 17:10:41 2019

@author: USER
"""

import resource

maxsize = 500000000 # In bytes
try:
    softas, hardas = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (maxsize, hardas))
    print('For address space: ', '\n', 'Soft is: ', softas, '\n', 'Hard is: ', hardas)
finally:
    try:
        softvm, hardvm = resource.getrlimit(resource.RLIMIT_VMEM)
        resource.setrlimit(resource.RLIMIT_VMEM, (maxsize, hardvm))
        print('For virtual memory: ', '\n', 'Soft is: ', softvm, '\n', 'Hard is: ', hardvm)
    finally:
        try:
            softrss, hardrss = resource.getrlimit(resource.RLIMIT_RSS)
            resource.setrlimit(resource.RLIMIT_RSS, (maxsize, hardrss))
            print('For RSS: ', '\n', 'Soft is: ', softrss, '\n', 'Hard is: ', hardrss)
        finally:
            print('done')

    


























