"""Seed file to make sample data for db."""

from models import User, Post, Tag, PostTag, db
from App import app

# Create all tables
db.drop_all()
db.create_all()


PostTag.query.delete()
User.query.delete()
Post.query.delete()
Tag.query.delete()

# Add sample users and posts
leonard = User(first_name='Leonard', last_name="Smith")
liz = User(first_name='Liz', last_name="Tyie")
maggie = User(first_name='Maggie', last_name="Sand")
nadine = User(first_name='Nadine', last_name="Mite")

db.session.add_all([leonard, liz, maggie, nadine])
db.session.commit()

p1 = Post(title='Financials', content='Finance blah blah', user_id=1)
p2 = Post(title='Legalities of Basketball', content='Legal stuff is legit boring', user_id=1)
p3 = Post(title='CatsRule', content='Cats will rule the world', user_id=1)
p4 = Post(title='Taco Trials', content='Vegan Tacos By Liz', user_id=2)
p5 = Post(title='Dessert', content='Dessert By Liz', user_id=2)
p6 = Post(title='Soccer', content='Soccer By Maggie', user_id=3)


db.session.add_all([p1, p2, p3, p4, p5, p6])
db.session.commit()


t_food = Tag(name="Food")
t_sport = Tag(name="Sport")
t_cat = Tag(name="Cat")
t_boring = Tag(name="Boring")

db.session.add_all([t_food, t_sport, t_cat, t_boring])
db.session.commit()

pt1 = PostTag(post_id="1", tag_id="4")
pt2 = PostTag(post_id="2", tag_id="4")
pt3 = PostTag(post_id="2", tag_id="2")
pt4 = PostTag(post_id="3", tag_id="3")
pt5 = PostTag(post_id="4", tag_id="1")
pt6 = PostTag(post_id="4", tag_id="2")
pt7 = PostTag(post_id="5", tag_id="1")
pt8 = PostTag(post_id="6", tag_id="2")

db.session.add_all([pt1, pt2, pt3, pt4, pt5, pt6, pt7, pt8])
db.session.commit()

# pc = Project(proj_code='car', proj_name='Design Car',
#              assignments=[EmployeeProject(emp_id=liz.id, role='Chair'),
#                           EmployeeProject(emp_id=maggie.id)])

# ps = Project(proj_code='server', proj_name='Deploy Server',
#              assignments=[EmployeeProject(emp_id=liz.id),
#                           EmployeeProject(emp_id=leonard.id, role='Auditor')])

# db.session.add_all([ps, pc])
# db.session.commit()
