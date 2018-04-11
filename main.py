import time
import sys
from crawler import Crawler
from crawler import CosineSimilarity as cs
from assets import Global
from connectKafka import cons

def main():
    if len(sys.argv)<2:
        print("默認 爬資料")
        cs.makeCsv()
        while 1:
            Crawler.get_articles(Global.YAHOO_URL_POLITICS,"politics")
            Crawler.get_articles(Global.YAHOO_URL_ENTERTAINMENT,"entertainment")  
            print("\n本次資料已取完!\n")
            time.sleep(10800) # 3 hours

    else:
        
        if sys.argv[1] == "consumer":
             cons.run("politics")
             cons.run("entertainment")

        elif sys.argv[1] == "request":
            cs.makeCsv()
            while 1:
                Crawler.get_articles(Global.YAHOO_URL_POLITICS,"politics")
                Crawler.get_articles(Global.YAHOO_URL_ENTERTAINMENT,"entertainment")  
                print("\n本次資料已取完!\n")
                time.sleep(10800) # 3 hours

if __name__ == '__main__':
    main()
