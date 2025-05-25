from flask import Flask, render_template, request, redirect, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    waste_type = db.Column(db.String(50))
    pickup_date = db.Column(db.String(20))
    pickup_time = db.Column(db.String(20))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        db.session.add(User(username=username, password=password))
        db.session.commit()
        return redirect('/login')
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password, request.form['password']):
            session['user_id'] = user.id
            return redirect('/dashboard')
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user_id' not in session:
        return redirect('/login')
    if request.method == 'POST':
        booking = Booking(
            user_id=session['user_id'],
            waste_type=request.form['waste_type'],
            pickup_date=request.form['pickup_date'],
            pickup_time=request.form['pickup_time']
        )
        db.session.add(booking)
        db.session.commit()
    bookings = Booking.query.filter_by(user_id=session['user_id']).all()
    return render_template('dashboard.html', bookings=bookings)

@app.route('/tracking')
def tracking():
    return render_template('tracking.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/login')

@app.route('/api/bookings')
def api_bookings():
    if 'user_id' not in session:
        return jsonify([])
    bookings = Booking.query.filter_by(user_id=session['user_id']).all()
    return jsonify([{
        'waste_type': b.waste_type,
        'pickup_date': b.pickup_date,
        'pickup_time': b.pickup_time
    } for b in bookings])

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)