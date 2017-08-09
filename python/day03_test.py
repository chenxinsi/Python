# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os

class BeautifulPicture():
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'}
        self.web_url = 'https://unsplash.com'
        self.folder_path = '/home/liangyu/Code/python'

    def request(self, url):
        r = requests.get(url, headers = self.headers)
        return r

    def save_img(self, url, name):  ##保存图片
        print('开始请求图片地址，过程会有点长...')
        img = self.request(url)
        file_name = name + '.jpg'
        print('开始保存图片')
        f = open(file_name, 'ab')
        f.write(img.content)
        print(file_name, '图片保存成功！')
        f.close()

    def mkdir(self, path):  ##这个函数创建文件夹
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            print('创建名字叫做', path, '的文件夹')
            os.makedirs(path)
            print('创建成功！')
        else:
            print(path, '文件夹已经存在了，不再创建')

    def get_pic(self):
        print('开始网页get请求')
        r = self.request(self.web_url)
        print('开始获取所有a标签',r.text)
        all_a = BeautifulSoup(r.text, 'lxml').find_all('a', class_="cV68d")
        print('开始创建文件夹')
        self.mkdir(self.folder_path)
        print('开始切换文件夹')
        os.chdir(self.folder_path)
        print(all_a)
        for a in all_a:
            img_str = a['style']
            print('a标签中完整的style内容是：',img_str)
            first_pos = img_str.index('"') + 1
            second_pos = img_str.index('"',first_pos)
            img_url = img_str[first_pos: second_pos]
            width_pos = img_url.index('&w=')
            height_pos = img_url.index('&q=')
            width_height_str = img_url[width_pos : height_pos]
            print('高度和宽度数据字符串是：', width_height_str)

            name_start_pos = img_url.index('photo')
            name_end_pos = img_url.index('?')
            img_name = img_url[name_start_pos : name_end_pos]
            self.save_img(img_url, img_name)

beauty = BeautifulPicture()
beauty.get_pic()