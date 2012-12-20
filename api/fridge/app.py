from flask import Flask

from resources import users_resource

app = Flask(__name__)

# Blueprints registration
app.register_blueprint(users_resource)


@app.route('/')
def api_root():
	return 'Welcome'


if __name__ == "__main__":
	app.run()