from flask import Flask, render_template,request, url_for,redirect,jsonify,session
from db import select_role, insert_users,insert_into,select_user,select_avtoriz
app = Flask(__name__)
app.json.ensure_ascii=False
app.config["SESSION_COOKIE_HTTPONLY"]=True#передвёт куки только по https
app.config["SESSION_COOKIE_SAMESITE"]="Lax"
app.secret_key = "1211"
products=[
        {"id":1,"name": 'Видеокарты'},
        {"id":2,"name":'Мат платы'}
    ]
users={
    "login":"admin",
    "pass":"12345"
    }

@app.route('/')
def index():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template('index.html')

@app.route('/cataloge')
def cataloge():
    return render_template('cataloge.html',
                            products=products)

@app.route('/api/products', methods=['GET'])
def api_products():
    return jsonify(products) 

@app.route('/add')
def add():
    master=[[1, 'Мышки'],[2, 'Клавиатуры']]
    return render_template('add.html',
                        master=master)

@app.route('/app/products/<int:id>',methods=['GET'])
def api_product(id):
    for product in products:
        if product["id"]== id:
            return jsonify(product)
        return jsonify({'error':F"Товар{id} не найден"})
@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.get_json()
    login = data.get("login")
    password = data.get("password")
    user=select_avtoriz(login,password)

    if not isinstance(login,str) or not isinstance(password,str):
        return jsonify({
            "success":False,
            "messege":"Введите логин или пароль"
        }), 400
    if len(user)!=0:
        session.clear()
        session["user_id"]=user[0]
        return jsonify({
            "success":True,
            "message":"Авторизация успешна",
            "redirect":url_for('cataloge')
        }),201
    else:
        return jsonify({
            "success":False,
            "message":"Авторизация не успешна",
            "redirect":url_for('login')
        }),201
@app.route('/login')
def login():
    return render_template('login.html')
if __name__=='__main__':
        app.run()
