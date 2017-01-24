#!/usr/bin/python
#-*-coding:utf-8-*-
import urllib2
import urllib

URL_IP = 'http://localhost:8000/ip'
URL_GET = 'http://localhost:8000/get'

def use_simple_urllib2():
    response = urllib.urlopen(URL_IP)
    print '>>>>Response Headers:'
    print response.info()
    print '>>>>Response Body:'
    print ''.join([line for line in response.readlines()])

def use_params_urllib2():
    params = urllib.urlencode({'param1':'hello','param2':'world'})
    print 'Request Params:'
    print params
    response = urllib2.urlopen('?'.join([URL_GET,'%s'])%params)
    print '>>>>Response Headers:'
    print response.info()
    print '>>>>Response Body:'
    print ''.join([line for line in response.readlines()])
if __name__ == '__main__':
    print '>>>>Use Simole urllib2:'
    use_simple_urllib2()
    print
    print '>>>>Use params urllib2:'
    use_params_urllib2()
