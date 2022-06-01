from flask import Flask,jsonify,request
import csv
from demographic_filtering import output
from content_based_filtering import get_recommendations

all_articles = []

with open('articles.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles =[]
unliked_articles =[]

app = Flask(__name__)

popular_articles = list(output)

@app.route('/popular-articles',methods=['GET'])
def popular_articles():
    return jsonify({
        'data':popular_articles,
        'status':'success'
    })


@app.route('/recommend-movies',methods=['GET'])
def recommend_movies():
    title = request.files.get('title')
    recommendation = get_recommendations(title)
    return jsonify({
        'recommendation':recommendation
    }),200

@app.route('/get-articles')
def get_articles():
    return jsonify({
        'data':all_articles[0],
        'status':'success'
    })

@app.route('/liked-articles',methods=['POST'])
def liked_articles():
    articles = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(articles)
    return jsonify({
        'status':'success'
    })

@app.route('/unliked-articles',methods=['POST'])
def unliked_articles():
    articles = all_articles[0]
    all_articles = all_articles[1:]
    unliked_articles.append(articles)
    return jsonify({
        'status':'success'
    })

if __name__ == '__main__':
    app.run()