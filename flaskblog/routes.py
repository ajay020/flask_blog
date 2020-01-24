from flask import render_template,url_for,flash,redirect
from flaskblog import app
from flaskblog.forms import RegistraionForm,LoginForm
from flaskblog.models import User,Post

posts = [
    {
        'author':'Corey Schafar',
        'title':'Blog post 1',
        'content':'first post content',
        'date_posted':'April 20, 2020'
    },
    {
        'author':'Hoa Doe',
        'title':'Blog post 2',
        'content':'second post content',
        'date_posted':'April 23, 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/register', methods=['POST','GET'])
def register():
    form = RegistraionForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}','success')
        return redirect(url_for('home'))

    return render_template('register.html', title="Register",form = form)

@app.route('/login', methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged In!!','success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful , Please check your username and password ','danger')    

    return render_template('login.html', title="Login" ,form=form)

