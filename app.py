from flask import Flask, render_template, redirect, url_for, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev_key'  # Change this for production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

@app.route('/')
def home():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    if not user:
        session.pop('user_id', None)
        return redirect(url_for('login'))
    return render_template('home.html', user=user)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        if User.query.filter_by(username=username).first():
            return 'Username already exists!'
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('home'))
        error = 'Invalid username or password. Please try again.'
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

@app.route('/alevel')
def alevel():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('Alevel.html')

@app.route('/alevel/data_representation')
def alevel_data_representation():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('Alevel/Data_Representation/index.html')

@app.route('/alevel/communications')
def alevel_communications():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('Alevel/Communications/index.html')

@app.route('/alevel/hardware')
def alevel_hardware():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('Alevel/Hardware/index.html')

@app.route('/alevel/software')
def alevel_software():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('Alevel/Software/index.html')

@app.route('/alevel/security')
def alevel_security():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('Alevel/Security/index.html')

@app.route('/alevel/ethics')
def alevel_ethics():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('Alevel/Ethics/index.html')

@app.route('/alevel/databases')
def alevel_databases():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('Alevel/Databases/index.html')

@app.route('/alevel/programming')
def alevel_programming():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('Alevel/Programming/index.html')

@app.route('/alevel/data_types')
def alevel_data_types():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('Alevel/Data_Types/index.html')

@app.route('/alevel/algo_desgn')
def alevel_algo_desgn():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('Alevel/Algo_desgn/index.html')

@app.route('/alevel/software_devolopment')
def alevel_software_devolopment():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('Alevel/Software_Devolopment/index.html')

if __name__ == '__main__':
    if not os.path.exists('site.db'):
        with app.app_context():
            db.create_all()
    app.run(debug=True)




