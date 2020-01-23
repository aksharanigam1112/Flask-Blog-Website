from flask import Flask , render_template
app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)