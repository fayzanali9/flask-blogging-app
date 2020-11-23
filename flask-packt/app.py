from flask import Flask,render_template,request,url_for,redirect

app = Flask(__name__)

# posts = {
#     0:{
#         'title' : 'First page',
#         'content': 'My first blog'
#     },
#     1:{'title' : 'Second page',
#         'content' : 'Trying to get into flask'
#     }
# }

posts = {
    0:{ 'id' : 0,
        'title' : 'First page',
        'content': 'My first blog'
    },
    1:{ 'id' : 1,
        'title' : 'Second page',
        'content' : 'Trying to get into flask'
    }
}




@app.route('/post/<int:post_id>')
def post(post_id):
    # post = posts.get(post_id)
    '''not using render template'''
    # return f"Post {post['title']} \n, content \t {post['content']}"  
    '''just using post.html with render template'''
    # return render_template('post.html') 

    # return render_template('post.html',post = post)
    '''above line can be written as below line'''
    '''the post argument in render_template below acts as {{post: }} in post.html'''
    # return render_template('post.html',post = posts.get(post_id))
    
    post = posts.get(post_id)
    if not post:
        return render_template('404.html',message = f'Post with id {post_id} was not found')
    return render_template('post.html',post = post)   



# form for creating your own posts
"""
@app.route('/post/form')
def form():
    return render_template('create.jinja2')
"""
"""The above endpoint is removed as the functionality can be implemented 
    in create endpoint with GET method """


# the browser does GET requests and form does POST requests.

# 127.0.1;5000/post/create?title=blablah&content=something_else 
# @app.route('/post/create') # this doesnt accept method POST (only GET)
@app.route('/post/create',methods = ['GET','POST'])
def create():
    if request.method == 'POST':
        # title = request.args.get('title') # providing query string parameters
        title = request.form.get('title')   
        # content = request.args.get('content')
        content = request.form.get('content')
        post_id = len(posts)
        posts[post_id] = {'id' : post_id,'title' : title,'content' : content}
        # url_for here takes 'post' function name(endpoint) 
        # which gives '/post/<int:post_id>' (url)address from above
        # we also specify arg 'post_id' required by 'post' function 
        # by our own post_id developed just above
        # redirect wraps this url and sends response back to browser telling it 
        # to load url_for('post',post_id =post_id) page instead of /post/create page 
        return redirect(url_for('post',post_id =post_id))
    return render_template('create.jinja2')



@app.route('/')
def home():
    # return 'Welcome to the world of flask'
    return render_template('home.jinja2',posts = posts)

if __name__ == "__main__":
    app.run(debug=True)