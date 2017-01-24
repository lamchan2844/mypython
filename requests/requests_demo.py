#!/usr/bin/python
#-*-coding:utf-8-*-
import requests

#URL_IP = 'http://localhost:8000/ip'
#URL_GET = 'http://localhost:8000/get'
URL_IP = 'http://www.httpbin.org/ip'
URL_GET = 'http://www.httpbin.org/get'


def use_simple_requests():
    response = requests.get(URL_IP)
    print '>>>>Response Headers:'
    print response.headers
    print '>>>>Response Body:'
    print response.text


def use_params_requests():
    params = {'param1': 'hello', 'param2': 'world'}
    print 'Request Params:'
    print params
    response = requests.get(URL_GET, params=params)
    print '>>>>Response Headers:'
    print response.headers
    print '>>>>Response status:'
    print response.status_code
    print response.reason
    print '>>>>Response Body:'
    print response.json()
if __name__ == '__main__':
    print '>>>>Use Simple requests:'
    use_simple_requests()
    print
    print '>>>>Use params requests:'
    use_params_requests()
