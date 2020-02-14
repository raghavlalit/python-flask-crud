from flask import Blueprint, render_template

route = Blueprint('route', __name__, template_folder="templates")

@route.route('/home')
def home():
	return render_template('index.html')