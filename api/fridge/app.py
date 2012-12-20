# -*- coding: utf-8 -*-

# Copyright (c) 2012 theo crevon
#
# See the file LICENSE for copying permission.

from flask import Flask

from wrappers import JSONResponse
from resources import users_resource

app = Flask(__name__)

# Blueprints registration
app.register_blueprint(users_resource)


@app.route('/')
def api_root():
	return JSONResponse(status=301)


if __name__ == "__main__":
	app.run()