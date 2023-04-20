# Sentiment analysis for reviews by customers and visualize the same. 

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn import svm
import numpy as np

df = pd.read_csv('./AmazonReview.csv')  # give absolute path
#getting rid of null values
df = df.dropna()

#Taking a 30% representative sample
np.random.seed(34)
df1 =df.sample(frac = 0.3)

#Adding the sentiments column
df1['sentiments'] = df1.rating.apply(lambda x: 0 if x in [1, 2] else 1)

X = df1['review']
y = df1['sentiments']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.05, random_state=0)

#Vectorizing the text data
cv = CountVectorizer()
ctmTr = cv.fit_transform(X_train)
X_test_dtm = cv.transform(X_test)

#Training the model
svcl = svm.SVC()
svcl.fit(ctmTr, y_train)
svcl_score = svcl.score(X_test_dtm, y_test)
print("Results for Support Vector Machine with CountVectorizer")
print(svcl_score)

y_pred_sv = svcl.predict(X_test_dtm)

#Conclusion matrix
print(y_pred_sv)
