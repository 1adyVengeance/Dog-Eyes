from flask import Flask
from flask_script import Manager
from app.views import api_blueprint

app = Flask(
    __name__,
    template_folder='./templates',
    static_folder='./static'
)

app.register_blueprint(blueprint=api_blueprint, url_prefix='/')

manage = Manager(app=app)

if __name__ == '__main__':
    manage.run()
