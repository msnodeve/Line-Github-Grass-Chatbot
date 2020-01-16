import requests
import time
from bs4 import BeautifulSoup

def userCommitFromGithub(userId):
    ti = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    request = requests.get('https://github.com/PresentJay')
    soup = BeautifulSoup(request.content, 'html.parser')
    attr = {"class" : "day", "data-date" : ti}
    data = soup.find_all("rect", attrs=attr)
    print(data[0].get('data-count'))

userCommitFromGithub("ADSa")