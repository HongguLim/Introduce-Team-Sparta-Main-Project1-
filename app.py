from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.numzcdz.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/name", methods=["POST"])
def name_post():
    name_receive = request.form['name_give']

    name_list = list(db.comment.find({}, {'_id':False}))
    # count = len(name_list) + 1

    doc = {
        'name':name_receive
    }
    db.comment.insert_one(doc)
    return jsonify({'msg': '등록 완료!'})


@app.route("/comment", methods=["POST"])
def comment_post():
    comment_receive = request.form['comment_give']

    comment_list = list(db.comment.find({}, {'_id':False}))
    # count = len(comment_list) + 1

    doc = {
        'comment':comment_receive
    }
    db.comment.insert_one(doc)
    # return jsonify({'msg': '등록 완료!'})






#
# @app.route("/name", methods=["GET"])
# def name_get():
#     name_list = list(db.name.find({},{'_id':False}))
#     return jsonify({'names': name_list})
#
# @app.route("/comment", methods=["GET"])
# def comment_get():
#     comment_list = list(db.comment.find({},{'_id':False}))
#     return jsonify({'comments': comment_list})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5006, debug=True)