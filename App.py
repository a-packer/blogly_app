from flask import Flask, request, redirect, render_template
from models import db, connect_db, User, Post, Tag, PostTag
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.debug = True

app.config['SECRET_KEY'] = '<aslfas249oiu2ejkrw9eiogkf>'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blog'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)

toolbar = DebugToolbarExtension(app)

connect_db(app)
# db.drop_all()
db.create_all()


@app.route("/")
def root():
    return redirect("/users")


@app.route("/users")
def list_users():
    """shows list of all users"""
    users = User.query.all()
    return render_template("all_users.html", users=users)

@app.route("/<int:user_id>")
def show_user(user_id):
    """Show details about a single user"""
    user = User.query.get_or_404(user_id)
    return render_template("user_details.html", user=user)


# --------------- Create New User Routes --------------- 

@app.route("/new_user", methods=["GET"])
def new_user_form():
    return render_template("new_user_form.html")

@app.route("/new_user", methods=["POST"])
def create_user():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    img_url = request.form["img_url"]
    img_url = img_url if img_url else None

    # create new User
    new_user = User(first_name=first_name, last_name=last_name, img_url=img_url)
    db.session.add(new_user)
    db.session.commit()

    return render_template('user_details.html', user=new_user) 

# --------------- Edit User Routes --------------- 
@app.route("/<int:user_id>/edit")
def edit_user_form(user_id):
    """Access edit form for an existing user"""
    user = User.query.get_or_404(user_id)

    return render_template("edit_user_form.html", user=user)

@app.route("/<int:user_id>/edit", methods=["POST"])
def edit_user(user_id):
    """Edit an existing user"""
    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.img_url = request.form['img_url']

    db.session.add(user)
    db.session.commit()

    return redirect("/users")

# --------------- Delete User Routes --------------- 
@app.route("/<int:user_id>/delete", methods=["GET"])
def delete_user_check(user_id):
    """Check to see if user really wanted to delete"""
    user = User.query.get_or_404(user_id)
    return render_template("delete_user.html", user=user)

@app.route("/<int:user_id>/delete", methods=["POST"])
def delete_user(user_id):
    """Delete an existing user"""
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/users")


# --------------- User's new Post Routes ---------------------

@app.route('/<int:user_id>/posts/new', methods=["GET"])
def form_to_post(user_id):
    """Show form to add post by a user"""
    user = User.query.get_or_404(user_id)
    return render_template("new_post_form.html", user=user)

@app.route('/<int:user_id>/posts/new', methods=["POST"])
def create_post(user_id):
    """Create post created by a specific user"""
    
    user = User.query.get_or_404(user_id)

    title = request.form['title']
    content = request.form['content']


    new_post = Post(title=title, content=content, user_id=user_id)

    db.session.add(new_post)
    db.session.commit()

    return redirect(f"/{user_id}")

@app.route('/post<int:post_id>', methods=["GET"])
def view_post(post_id):
    """View post details, content, datetime created"""

    post = Post.query.get_or_404(post_id)
    user_id = post.user_id
    user = User.query.get_or_404(user_id)

    return render_template("view_post.html", post=post, user=user)

@app.route('/posts', methods=["GET"])
def all_posts():
    """View all posts by all users in sequential order"""

    all_posts = Post.query.all()

    return render_template("all_posts.html", all_posts=all_posts)


@app.route('/post<int:post_id>/edit', methods=["GET"])
def edit_post_form(post_id):
    """Form to edit an existing post"""

    post = Post.query.get_or_404(post_id)
    return render_template('edit_post.html', post=post)

@app.route('/post<int:post_id>/edit', methods=["POST"])
def edit_post(post_id):
    """Edit an existing post"""
 
    post = Post.query.get_or_404(post_id)
    post.title = request.form['title']
    post.content = request.form['content']

    db.session.add(post)
    db.session.commit()

    return redirect(f"/post{post_id}")


@app.route("/post<int:post_id>/delete", methods=["GET"])
def delete_post_check(post_id):
    """Check to see if user wants to delete an existing post"""

    post = Post.query.get_or_404(post_id)

    return render_template('delete_post.html', post=post)

@app.route("/post<int:post_id>/delete", methods=["POST"])
def delete_post(post_id):
    """Delete an existing post from db"""

    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()

    return redirect("/posts")


# --------------- Tag Routes ---------------------

@app.route("/tags", methods=["GET"])
def all_tags():
    """Lists all tags, with links to the tag detail page."""
    return "all tags"


@app.route("/tags/<int:tag_id>", methods=["GET"])
def tag_details():
    """Show detail about a tag. Have links to edit form and to delete."""

    return "tag details"


@app.route("/tags/new", methods=["GET"])
def create_tag_form():
    """Shows a form to add a new tag."""
    return "tag form"


@app.route("/tags/new", methods=["POST"])
def add_new_tag():
    """Process add form, adds tag, and redirect to tag list."""
    return "added tag"


@app.route("/tags/<int:tag_id>/edit", methods=["GET"])
def edit_tag_form():
    """Show edit form for a tag."""
    return "edit tag form"


@app.route("/tags/<int:tag_id>/edit", methods=["POST"])
def edit_tag():
    """Process edit form, edit tag, and redirects to the tags list."""
    return "edited tag"


@app.route("/tags/<int:tag_id>/edit", methods=["GET"])
def delete_tag_check():
    """Just a check to make sure user really wants to delete a tag"""
    return "delete tag check"


@app.route("/tags/<int:tag_id>/delete", methods=["POST"])
def delete_tag():
    """Delete a tag."""
    return "deleted tag"