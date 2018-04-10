import jieba
import jieba.analyse
import numpy
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def jiebaAnalyse(corpus=[""]):
    jieba.set_dictionary('./example/dict.txt.big')
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(corpus)
    fv = tfidf.toarray()
    print(tfidf.shape)

    articles = []
    words = vectorizer.get_feature_names()
    for i in range(len(corpus)):
        print('----Document %d----' % (i+1))
        for j in range(len(words)):
            if tfidf[i,j] > 1e-5:
                try:
                    # print(words[j], tfidf[i,j])
                    articles.append(cosine_similarity(tfidf[0],tfidf))
                    # print(result)
                    # print(fv[j])
                except:
                    pass
    print(articles)
    return articles,i+1
        
def comparisonSimilarity(articles,number):
    pass
    # line = []
    # for i in range(number):
    #     line[i] = numpy.array([])
    #     for j in range(number):
    #         if not j == i:
    #             line[i][i,j] = cosine_similarity(articles[i],articles[j])