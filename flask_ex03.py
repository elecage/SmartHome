from flask import Flask

app = Flask(__name__)

@app.route('/user/<username>')
def show_user_porfile(username):
    #show user profile for that user
    return 'User %s'%username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d'%post_id

if __name__ == '__main__':
    app.run()