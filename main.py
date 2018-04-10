import time
from crawler import Crawler
from crawler import CosineSimilarity as cs
from assets import Global

def main():
    while 1:
        cs.makeCsv()
        Crawler.get_articles(Global.YAHOO_URL_POLITICS,"politics")
        Crawler.get_articles(Global.YAHOO_URL_ENTERTAINMENT,"entertainment")  
        print("\n本次資料已取完!\n")
        time.sleep(10800) # 3 hours

if __name__ == '__main__':
    main()
