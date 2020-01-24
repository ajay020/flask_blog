from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistraionForm,LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '526669b03620e2ed8bb3a81010d8'

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



if __name__ == '__main__':
    app.run(debug=True)