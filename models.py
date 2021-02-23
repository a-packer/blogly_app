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
    first_name = db.Column(db.String(50), nullable="False")
    last_name = db.Column(db.String(50), nullable="False")
    img_url = db.Column(db.String(3000), nullable="False", default="https://i.pinimg.com/564x/85/21/df/8521df4e1ac0c6f1af2f3ac166e5390b.jpg")
