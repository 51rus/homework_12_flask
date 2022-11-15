import logging
from json import JSONDecodeError
from flask import Blueprint, render_template, request
from functions import get_posts_by_word

# Здесь блюпринт для показывания фото (картинок)
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    """
    Вывод формы на главной странице при обращении к "/"
    """
    return render_template('index.html')


@main_blueprint.route('/search/')
def search_page():
    search_query = request.args.get('s', '')
    # лог info
    logging.info('Выполняю поиск')
    try:
        posts = get_posts_by_word(search_query)
    except FileNotFoundError:
        # лог error
        logging.error('Файл не найден')
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Невалидный файл'
    return render_template('post_list.html', query=search_query, posts=posts)