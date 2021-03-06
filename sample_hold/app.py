from flask import Flask, render_template

from controllers.modules_controller import modules_blueprint
from controllers.manufacturers_controller import manufacturers_blueprint

app = Flask(__name__)

app.register_blueprint(modules_blueprint)
app.register_blueprint(manufacturers_blueprint)


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
