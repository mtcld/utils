from bs4 import BeautifulSoup
import requests
import subprocess


def download_img(url):
    print(url)
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    img_link = soup.select("#allsizes-photo > img[src]")[0]['src']
    print(img_link)
    cmd = ['wget', img_link]
    subprocess.Popen(cmd).communicate()   
    


file_path = "./urllist.txt"
with open(file_path) as f:
    for line in f:
        download_img(line)

'''
from lxml import html
import requests

page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.content)
#This will create a list of buyers:
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
prices = tree.xpath('//span[@class="item-price"]/text()')

print 'Buyers: ', buyers
print 'Prices: ', prices
'''

