import PHSpider
import sys

def main():
    base_url = sys.argv[1]
    spider = PHSpider.PHSpider(base_url)
    print(spider.title)
    print(spider.video_url)

if __name__ == '__main__':
    main()