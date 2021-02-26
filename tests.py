from unittest import TestCase

from app import app
from modesl import db, User, Post

# uses test database
app.config['SQLAlchemy_DATABASE_URI'] = 'postgresl:///blog_test'
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all()

class UserModelTestCase(TestCase):
    """Tests for model User"""

    def setUp(self):
        """Clean up any existing users"""

        User.query.delete()

    def tearDown(self):
        """Clean up any messed up transaction"""

        db.session.rollback()


class PostModelTestCase(TestCase):
    """Tests for model Posts"""

    def setUp(self):

    def tearDown(self):
        