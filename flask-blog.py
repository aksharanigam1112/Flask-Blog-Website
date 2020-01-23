from flask import Flask , render_template ,url_for
from forms import RegistrationForm,LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a43cdd64687a3224012fe27c3d5e29e6'

posts = [
    {
        'author':'Akshara',
        'title':'Blog post 1',
        'content':'First Post Content',
        'date_posted':'January 2, 2020'
    },
    {
        'author':'Purvi',
        'title':'Blog post 2',
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

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html',title="Register",form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html',title="Login",form=form)

if __name__ == '__main__':
    app.run(debug=True)