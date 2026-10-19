from flask import Flask, render_template,request, url_for, redirect, jsonify
app = Flask(__name__)
app.json.ensure_ascii=False
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
    if not isinstance(login,str) or not isinstance(password,str):
        return jsonify({
            "success":False,
            "messege":"Введите логин или пароль"
        }), 400
    if login==users["login"] and password==users['pass']:
        return jsonify({
            "success":True,
            "message":"Авторизация успешна",
            "redirect":url_for('cataloge')
        })
    return None
@app.route('/login')
def login():
    return render_template('login.html')
if __name__=='__main__':
        app.run()
