import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def connect_db(app):
    """Connects this database to Flask app."""
    db.app = app
    db.init_app(app)

# Models go below
class User(db.Model):
    """User Class"""

    __tablename__ = 'users'
   
    def __repr__(self):
        u=self
        return f"<User id={u.id} first_name={u.first_name} last_name={u.last_name} image_url={u.image_url}>"


    # table schema
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    img_url = db.Column(db.String(3000), nullable=False, default="https://i.pinimg.com/564x/85/21/df/8521df4e1ac0c6f1af2f3ac166e5390b.jpg")

    posts = db.relationship("Post", backref="users", cascade="all, delete-orphan")

class Post(db.Model):
    """Blog post."""

    __tablename__ = "posts"

    def __repr__(self):
        p = self
        return f"<Post {p.id} {p.title}>"

     # table schema
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False, default="Post Title")
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    #assignments = db.relationship('EmployeeProject', backref='employee')
    subjects = db.relationship('PostTag', backref='post')

    # projects = db.relationship('Project', secondary="employees_projects", backref="employees")
    tags = db.relationship('Tag', secondary="post_tags", backref="posts")


class Tag(db.Model):
    """Tags are connected to posts in order to search for posts about certain topics"""

    __tablename__ = "tags"

    def __repr__(self):
        return f"<Tag {self.id} {self.name}>"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)

    #  assignments = db.relationship('EmployeeProject', backref="project")
    subjects = db.relationship('PostTag', backref="tag")

class PostTag(db.Model):

    __tablename__ = "post_tags"

    def __repr__(self):
        return f"<PostTag post-{self.post_id} tag-{self.tag_id}>"

    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)




