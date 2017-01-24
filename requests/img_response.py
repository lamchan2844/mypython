#-*-coding:utf-8-*-
import requests


def download_image():
    """
    download image/file
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2141.400 QQBrowser/9.5.10219.400'}
    url = 'http://img1.gamersky.com/image2017/01/20170123_359_jyf_9/gamersky_01small_02_20171231758C06.jpg'
    response = requests.get(url, headers=headers, stream=True)
    print response.status_code, response.reason
    with open('demo.jpg', 'wb') as fd:
        for chunk in response.iter_content(128):
            fd.write(chunk)


def download_image_improved():
    """
    download image/file
    """
    # 伪造heeaders
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2141.400 QQBrowser/9.5.10219.400'}
    # 限定url
    url = 'http://img1.gamersky.com/image2017/01/20170123_359_jyf_9/gamersky_01small_02_20171231758C06.jpg'
    from contextlib import closing
    #close the stream while ending the program
    with closing(requests.get(url, headers=headers, stream=True)) as response:
        print response.status_code, response.reason
        with open('demo1.jpg', 'wb') as fd:
        	#每128写一次
            for chunk in response.iter_content(128):
                fd.write(chunk)


if __name__ == '__main__':
    # download_image()
    download_image_improved()
