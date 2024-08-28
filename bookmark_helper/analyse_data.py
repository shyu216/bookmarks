"""
concat content and use TFIDF to get the tags
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import json
import jieba
import jieba.posseg as pseg
import matplotlib.pyplot as plt
import numpy as np

import nltk
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('maxent_ne_chunker_tab')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('chinese'))
stop_words_eng = set(stopwords.words('english'))
from nltk.corpus import wordnet as wn
from nltk import ne_chunk, pos_tag, word_tokenize

def is_english(word):
    """检查一个字符串是否为英文"""
    return all(ord(c) < 128 for c in word)

def is_english_noun(word):
    """检查一个英文单词是否为名词"""
    synsets = wn.synsets(word, pos=wn.NOUN)
    return len(synsets) > 0

def is_proper_noun(word):
    """检查一个英文单词是否为专有名词"""
    words = word_tokenize(word)
    tagged = pos_tag(words)
    named_entities = ne_chunk(tagged)
    for chunk in named_entities:
        if hasattr(chunk, 'label') and chunk.label() in ['PERSON', 'ORGANIZATION', 'GPE']:
            return True
    return False

def tokenize(text):
    # words = pseg.lcut(text)
    # # 仅保留中文名词和英文单词
    # words = [word.word for word in words if word.flag == 'n' or word.flag == 'nz' or (word.flag == 'eng' and (is_english_noun(word.word) or is_proper_noun(word.word)))]
    words = jieba.lcut(text)
    words = [word for word in words if word.isalpha() and len(word) > 1]
    words = [word for word in words if not is_english(word) or is_english_noun(word)]
    words = [word for word in words if word not in stop_words and word not in stop_words_eng]
    words = set(words)
    print(words)
    return words

if __name__ == '__main__':
    content = []
    with open('bookmarks.json', 'r', encoding='utf-8') as f:
        full_info = json.load(f) 
        for info in full_info:
            content.append(info['raw_text'])

    
    # # 创建TfidfVectorizer实例
    # vectorizer = TfidfVectorizer(tokenizer=tokenize)
    # tfidf_matrix = vectorizer.fit_transform(content)
    # feature_names = vectorizer.get_feature_names_out()

    tags = {}

    # # 创建CountVectorizer实例
    vectorizer = CountVectorizer(tokenizer=tokenize)
    count_matrix = vectorizer.fit_transform(content)
    feature_names = vectorizer.get_feature_names_out()


    for i, website in enumerate(content):
        tfidf_scores = count_matrix[i].toarray().flatten()
        # 找出所有大于0的分数
        positive_scores_indices = np.where(tfidf_scores > 0)[0]

        # 如果没有大于0的分数，就跳过
        if len(positive_scores_indices) == 0:
            full_info[i]['tags'] = []
        else:
            # 从大于0的分数中选择前5个
            top5_indices = tfidf_scores[positive_scores_indices].argsort()[-5:][::-1]
            top5_indices = positive_scores_indices[top5_indices]
            print(f"Top 5 tags for website {i}:")
            print ([(feature_names[j], tfidf_scores[j]) for j in top5_indices])
            full_info[i]['tags'] = [feature_names[j] for j in top5_indices]

            for j in top5_indices:
                if feature_names[j] in tags:
                    tags[feature_names[j]] += 1
                else:
                    tags[feature_names[j]] = 1



    # # 计算每个标签的覆盖范围
    # tag_coverage = {}
    # for i, website in enumerate(content):
    #     count_scores = count_matrix[i].toarray().flatten()
    #     positive_scores_indices = np.where(count_scores > 0)[0]
    #     for j in positive_scores_indices:
    #         if feature_names[j] in tag_coverage:
    #             tag_coverage[feature_names[j]].add(i)
    #         else:
    #             tag_coverage[feature_names[j]] = {i}

    # # 贪心算法实现最小集合覆盖
    # uncovered_websites = set(range(len(content)))
    # selected_tags = []

    # while uncovered_websites:
    #     # 选择覆盖最多未覆盖文本的标签
    #     best_tag = max(tag_coverage, key=lambda tag: len(tag_coverage[tag] & uncovered_websites))
    #     selected_tags.append(best_tag)
    #     uncovered_websites -= tag_coverage[best_tag]

    # print("Selected tags for minimum set cover:")
    # print(selected_tags)

    # # 将选中的标签添加到full_info
    # for i, website in enumerate(content):
    #     count_scores = count_matrix[i].toarray().flatten()
    #     positive_scores_indices = np.where(count_scores > 0)[0]
    #     full_info[i]['tags'] = [feature_names[j] for j in positive_scores_indices if feature_names[j] in selected_tags]

    # 计算每个出现次数的标签数量
    count_dict = {}
    for count in tags.values():
        if count in count_dict:
            count_dict[count] += 1
        else:
            count_dict[count] = 1

    # 准备绘图数据
    x = list(count_dict.keys())
    y = list(count_dict.values())

    # 绘制柱状图
    plt.figure()
    plt.bar(x, y)
    plt.yscale('log')
    plt.xlabel('Occurrences')
    plt.ylabel('Number of tags')
    plt.title('Relationship between tag occurrences and number of similar tags')
    plt.show()

    with open("tags.json", "w", encoding="utf-8") as f:
        sorted_tags = sorted(tags.items(), key=lambda x: x[1], reverse=True)
        json.dump(sorted_tags, f, ensure_ascii=False, indent=4)

    with open('sites.json', 'w', encoding='utf-8') as f:
        # 删除raw_text字段
        for info in full_info:
            del info['raw_text']
            # 在。/.后切掉
            if info["description"]:
                description = info["description"]
                has_chinese_dot = description.find("。")
                if has_chinese_dot != -1:
                    info["description"] = description[:has_chinese_dot+1]
                has_dot = description.find(". ")
                if has_dot != -1:
                    info["description"] = description[:has_dot+1]
        json.dump(full_info, f, ensure_ascii=False, indent=4)
