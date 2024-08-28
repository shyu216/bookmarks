"""
concat content and use TFIDF to get the tags
"""
from sklearn.feature_extraction.text import TfidfVectorizer
import json
import jieba
import matplotlib.pyplot as plt
import numpy as np

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('chinese'))
stop_words_eng = set(stopwords.words('english'))


if __name__ == '__main__':
    content = []
    with open('sites.json', 'r', encoding='utf-8') as f:
        full_info = json.load(f)
        for info in full_info:
            content.append(info['raw_text'])

    # 定义分词函数
    def tokenize(text):
        words = jieba.lcut(text)
        words = [word for word in words if word.isalpha() and len(word) > 1]
        words = [word for word in words if word not in stop_words and word not in stop_words_eng]
        return words

    # 创建TfidfVectorizer实例
    vectorizer = TfidfVectorizer(tokenizer=tokenize)
    tfidf_matrix = vectorizer.fit_transform(content)
    feature_names = vectorizer.get_feature_names_out()

    tags = {}


    for i, website in enumerate(content):
        tfidf_scores = tfidf_matrix[i].toarray().flatten()
        # 找出所有大于0的分数
        positive_scores_indices = np.where(tfidf_scores > 0)[0]

        # 如果没有大于0的分数，就跳过
        if len(positive_scores_indices) == 0:
            full_info[i]['tags'] = []
        else:
            # 从大于0的分数中选择前10个
            top10_indices = tfidf_scores[positive_scores_indices].argsort()[-10:][::-1]
            top10_indices = positive_scores_indices[top10_indices]
            print(f"Top 10 tags for website {i}:")
            print ([(feature_names[j], tfidf_scores[j]) for j in top10_indices])
            full_info[i]['tags'] = [feature_names[j] for j in top10_indices]

            for j in top10_indices:
                if feature_names[j] in tags:
                    tags[feature_names[j]] += 1
                else:
                    tags[feature_names[j]] = 1

    sorted_tags = sorted(tags.items(), key=lambda x: x[1], reverse=True)
    plt.figure()
    plt.barh([tag[0] for tag in sorted_tags[-100:]], [tag[1] for tag in sorted_tags[-100:]])
    plt.show()

    with open("tags.json", "w", encoding="utf-8") as f:
        json.dump(sorted_tags, f, ensure_ascii=False, indent=4)

    with open('sites.json', 'w', encoding='utf-8') as f:
        # 删除raw_text字段
        for info in full_info:
            del info['raw_text']
        json.dump(full_info, f, ensure_ascii=False, indent=4)
