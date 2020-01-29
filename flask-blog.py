from flask import Flask , render_template ,url_for,flash,redirect
from forms import RegistrationForm,LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a43cdd64687a3224012fe27c3d5e29e6'

posts = [
    {
        'author':'Akshara',
        'title':'Code with Ease',
        'content':'First Post Content',
        'date_posted':'January 2, 2020'
    },
    {
        'author':'Purvi',
        'title':'GitHub Contribution',
        'content':'Second Post Content',
        'date_posted':'January 12, 2020'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title= 'About')

@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if(form.validate_on_submit()):
        flash(f"Account created for {form.username.data}!!",'success')
        return redirect(url_for('home'))
    return render_template('register.html',title="Register",form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    if (form.validate_on_submit()):
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash(f'Logged In !! ','success')
            return redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful. Please check username password','danger')
    return render_template('login.html',title="Login",form=form)

if __name__ == '__main__':
    app.run(debug=True)