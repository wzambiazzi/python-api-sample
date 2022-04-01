import flask
from routes.user_route import user_route

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/demo-python/hello', methods=['GET'])
def home():
    return 'Hello v1.2';
    
@app.route('/demo-python/test', methods=['GET'])
def demo():
    return 'teste v1.2';

#app.register_blueprint(user_route)
    
app.run(host='0.0.0.0',port=5000)