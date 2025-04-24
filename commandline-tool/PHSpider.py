from bs4 import BeautifulSoup
import requests
import re

# index_title = re.compile(r'index_title\.php\?id=(\d+)')
# index_cover_image = re.compile(r'index_cover_image\.php\?id=(\d+)')
index_video_range = re.compile(r'"mediaDefinitions":\[{(.*?)}')
index_video = re.compile(r'"videoUrl":"(.*?)"')

class PHSpider:
    def __init__(self, base_url):
        self.headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0" }
        self.response = requests.get(base_url, headers=self.headers)
        self.html = self.response.text
        self.soup = BeautifulSoup(self.html, 'html.parser')

        video_range_url = re.findall(index_video_range, self.html)[0]
        self.video_url = re.findall(index_video, video_range_url)[0]
        self.video_url = self.video_url.replace('\\', '')

        self.title = self.soup.title.string.split(' - ')[0]