#Entry point for website

#importing Flask
from flask import Flask

#importing views/routes
from views import views

#initialising app
app = Flask(__name__)

#calling route
app.register_blueprint(views, url_prefix="/views")

#setting port
if __name__ == '__main__':
    app.run(debug=True, port = 8000)