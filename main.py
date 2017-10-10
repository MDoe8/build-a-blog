from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import sqlalchemy


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['sqlalchemy_database_uri'] = 'mysql+mymysql://build-a-blog:hello@localhost:8889/build-a-blog'
app.config['sqlalchemy_echo'] = True
db = sqlalchemy(app)

class blog(db.model):
    id=db.Column(db.Integer, primary_key=True)
    title - db.Colument(db.String(120))
    body = db.Column(db.String(1000))

    def __init__(self, title, body):
        self.title=title
        self.body=body

@app.route('/newpost', method=['GET', 'POST'])
def add_blog():
    return render_template('newpost.html')

@app.route('/', methods=['POST', 'GET'])
def index():
    if request_args:
        blog_id =request.args.get("id")
        blog - blog.query.get(blog_id_)
        return render_template('blog.html')

    else:
        blogs=Blog.query.all()
        return render_template('blog.html', title='build a blog', blogs=blogs)

    if not title_error and not body_error:
        new_blog = Blog(blog_title, blog_body)
        db.session.add(new_blog)
        db.session.commit()
        query_param= "/blog?id=" + str(new_blog.id)

    else:
        return render_template('newpost.html', title='add blog entry', title_error=title_error, body_error=body_error)
    if __name__=='__main__':
        app.run()

