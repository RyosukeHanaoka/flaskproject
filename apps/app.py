# app.py の中で
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

password_hash = generate_password_hash('your_password')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///arthritis_detector_database.db'
db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
# ここで `user` はデータベースから取得したユーザーオブジェクトとします
# そして `form_password` はログインフォームから送信されたパスワードとします
user = User.query.filter_by(email='user_email').first()
check = check_password_hash(user.password_hash, 'form_password')
if check:
    # パスワードが一致する場合
    print("パスワードが一致します。")
else:
    # パスワードが一致しない場合
    print("パスワードが一致しません。")
    
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form', methods = ['GET', 'POST'])
def informed_consent():
    return render_template('form.html')

@app.route('/form1', methods=['GET', 'POST'])
def symptom():
    return render_template('form1.html')

@app.route('/form2', methods=['GET', 'POST'])
def sign():
    return render_template('form2.html')

if __name__ == '__main__':
    app.run(debug=True)

