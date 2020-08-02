from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    # 1.클라이언트로 값을 서버로 받아서 변수에 저장
    name = request.form['name_give']
    count = request.form['count_give']
    address = request.form['address_give']
    phone = request.form['phone_give']
    order_list = {
        'name': name,
        'count': count,
        'address': address,
        'phone': phone,
    }
    db.order_lists.insert_one(order_list)
    return jsonify({'result': 'success', 'msg': '주문이 완료되었습니다.'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    order_list = list(db.order_lists.find({},{'_id':0}))
    # 여길 채워나가세요!
    return jsonify({'result': 'success', 'order_list': order_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=4000, debug=True)
