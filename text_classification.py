import pandas as pd
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Data Processing
input_data = pd.read_csv("reviews_Clothing_Shoes_and_Jewelry_5.csv")
dataset = {"reviewText": input_data["reviewText"], "overall": input_data["overall"]}
dataset = pd.DataFrame(data = dataset)
dataset = dataset.dropna() # ignore if any row contained NaN

dataset = dataset[dataset["overall"] != '3']
dataset["label"] = dataset["overall"].apply(lambda rating : +1 if rating > '3' else -1)

# Splitting data into training set and testing set
X = pd.DataFrame(dataset, columns = ["reviewText"])
y = pd.DataFrame(dataset, columns = ["label"])
train_X, test_X, trian_y, test_y = train_test_split(X, y, random_state=50)

# Bag of Words model
vectorizer = CountVectorizer(token_pattern=r'\b\w+\b')
train_vector = vectorizer.fit_transform(train_X["reviewText"])
test_vector = vectorizer.transform(test_X["reviewText"])

# LogisticRegression model for classification problems
clr = LogisticRegression()
clr.fit(train_vector, trian_y.values.ravel())
scores = clr.score(test_vector, test_y) # accracy
print(scores)
