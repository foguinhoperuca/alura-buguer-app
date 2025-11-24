import logger
import os

from dotenv import load_dotenv
from flask import Flask, redirect, session, url_for

from controller.auth_controller import auth_bp


load_dotenv()
app = Flask(__name__)
secret_key = os.getenv('SECRET_KEY')
# # TODO debug log it!
# logger.debug(f'SECRET_KEY: {SECRET_KEY}')

app.secret_key = secret_key

app.register_blueprint(auth_bp, url_prefix='/auth')

@app.route('/')
def index():
    return redirect(url_for('auth.login_page'))


if __name__ == '__main__':
    app.run(port=5000, debug=True)
