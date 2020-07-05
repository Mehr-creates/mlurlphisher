
from flask import Flask,render_template,url_for,request
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib



app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
	mnb_count= pd.read_csv("Malicious URLs.csv")

	mnb_count = CountVectorizer()
	mnb_count = cv.fit_transform(X)
	from sklearn.model_selection import train_test_split
	df_test, df_train = train_test_split(X, y, test_size=0.3, random_state=23)
	#Naive Bayes Classifier
	from sklearn.naive_bayes import MultinomialNB

	mnb_count = MultinomialNB()
	mnb_count.fit(count_X,labels)
	mnb_count.score(count_X,labels)

	if request.method == 'POST':
		message = request.form['message']
		data = [message]
		vect = test_count.transform(data).toarray()
		my_prediction = mnb_count.predict(vect)
	return render_template('result.html',prediction = my_prediction)



if __name__ == '__main__':
	app.run(debug=True)
