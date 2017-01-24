#-*-coding:utf-8-*-
import requests

BASE_URL = 'https://api.github.com'


def construct_url(end_point):
    return '/'.join([BASE_URL, end_point])


def basic_auth():
    response = requests.get(construct_url(
        'user'), auth=('xxxx', 'xxxx'))
    print response.text
    print response.request.headers


def basic_oauth():
    headers = {'Authorization': 'db8c8e8279b82af279b25c3a68168efe1f341f90'}
    # user/emails
    response = requests.get(construct_url('user/emails'), headers=headers)
    print response.request.headers
    print response.text
    print response.status_code

from requests.auth import AuthBase


class GithubAuth(AuthBase):

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers['Authorization'] = ' '.join(['token', self.token])
        return r


def oauth_advanced():
    auth = GithubAuth('db8c8e8279b82af279b25c3a68168efe1f341f90')
    response = requests.get(construct_url('user/emails'), auth=auth)
    print response.status_code, response.reason
    print response.text


if __name__ == '__main__':
    # basic_auth()
    # basic_oauth()
    oauth_advanced()
