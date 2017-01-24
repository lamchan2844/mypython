#-*- coding:utf-8-*-
import json
import requests
from requests import exceptions
URL = 'https://api.github.com'


def build_uri(endpoint):
    return '/'.join([URL, endpoint])


def better_print(json_str):
    return json.dumps(json.loads(json_str), indent=4)


def print_response(response):
    print better_print(response.text)
    print response.request.headers
    print response.url
    print response.request.body
    print response.status_code


def request_method():
    response = requests.get(build_uri('user/emails'),
                            auth=('xxxx', 'xxxx'))
    # print response.text
    print better_print(response.text)


def params_request():
    response = requests.get(build_uri('users'), params={'since': 11})
    print_response(response)


def json_resquest():
    # response = requests.patch(build_uri('user'), auth=(
    #    'xxxx', 'xxxx'), json={'name': 'xxxx'})
    response = requests.post(build_uri(
        'user/emails'), auth=('xxxx', 'xxxx'), json=['xxxx@xxxx.com'])
    print_response(response)


def timeout_resquest():
    try:
        response = requests.get(build_uri('user/emails'), timeout=10)
        response.raise_for_status()
    except exceptions.Timeout as e:
        print e.message
    except exceptions.HTTPError as e:
        print e.message
    else:
        print_response(response)


def hard_requests():
    from requests import Request, Session
    s = Session()
    headers = {'User-Agent': 'fake1.3.4'}
    req = Request('GET', build_uri('user/emails'),
                  auth=('xxxx', 'xxxx'), headers=headers)
    prepped = req.prepare()
    print prepped.body
    print prepped.headers

    resp = s.send(prepped, timeout=5)
    print resp.request.headers
    print resp.text

if __name__ == '__main__':
    # request_method()
    # params_request()
    # json_resquest()
    # timeout_resquest()
    hard_requests()
