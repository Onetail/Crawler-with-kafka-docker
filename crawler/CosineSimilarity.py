import jieba
import jieba.analyse

def jiebaAnalyse():
    jieba.set_dictionary('../example/dict.txt.big')
    content = open('lyrics.txt', 'rb').read()
    tags = jieba.analyse.extract_tags(content, 10, withWeight=True)
    print(tags)