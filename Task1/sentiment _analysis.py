import nltk
from nltk.corpus import movie_reviews
import random
import matplotlib.pyplot as plt
from collections import Counter

nltk.download('movie_reviews')
nltk.download('punkt')


documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = list(all_words)[:2000]

def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features[f'contains({word})'] = (word in document_words)
    return features

feature_sets = [(document_features(d), c) for (d, c) in documents]

train_set, test_set = feature_sets[:1600], feature_sets[1600:]

classifier = nltk.NaiveBayesClassifier.train(train_set)

accuracy = nltk.classify.accuracy(classifier, test_set)
print(f'Accuracy: {accuracy * 100:.2f}%')

classifier.show_most_informative_features(10)


test_reviews = [category for (features, category) in test_set]
predictions = [classifier.classify(features) for (features, category) in test_set]

actual_counts = Counter(test_reviews)
predicted_counts = Counter(predictions)

print(f'Actual sentiment distribution: {actual_counts}')
print(f'Predicted sentiment distribution: {predicted_counts}')


plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.bar(actual_counts.keys(), actual_counts.values(), color=['blue', 'red'])
plt.title('Actual Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Number of Reviews')

plt.subplot(1, 2, 2)
plt.bar(predicted_counts.keys(), predicted_counts.values(), color=['blue', 'red'])
plt.title('Predicted Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Number of Reviews')

plt.tight_layout()
plt.show()
