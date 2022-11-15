import logging

from flask import Flask, request, render_template, send_from_directory

from loader.views import loader_blueprint
from main.views import main_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

# регистрация блюпринтов
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

# установка уровня логирования для всего проекта INFO
# логи будут сохроняться в basic.log
logging.basicConfig(filename='basic.log', level=logging.INFO)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()
