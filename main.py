from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://buid-a-blog:hello@localhost:8889/buid-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(1000))

    def __init__(self, title, body):
        self.title = title
        self.body = body

@app.route('/blogentry', methods=['GET', 'POST'])
def add_blog():
    if request.method == 'POST':
        test_title = request.form['title']
        test_body = request.form['new_blog']
        new_blog = Blog(test_title, test_body)
        db.session.add(new_blog)
        db.session.commit()
        query_param= "/blog?id=" + str(new_blog.id)
    return render_template('blogentry.html', title="New Blog Post")

@app.route('/blog')
def view_post():
        blog = Blog.query.filter_by(id=request.args.get('id')).first()   
        return render_template('blog.html', blog=blog)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        blog_id = request.args.get('id')
        blog = Blog.query.get(blog_id)
        return render_template('newpost.html', title='Here are your blogs!', blog=blogs)

    else:
        blogs = Blog.query.all()
        return render_template('blog.html', title='build a blog', blogs=blogs)


if __name__=='__main__':
    app.run()



