from flask import Flask, render_template, request, redirect, url_for
import logging

import formatting
import ide

app = Flask(__name__, template_folder='templates', static_folder='static')

# logging.getLogger('werkzeug').setLevel(logging.ERROR)


@app.route("/")
def main_page():
    return render_template("main.html")


@app.route("/api/on_key_pressed")
def on_key_pressed():
    ide.key_pressed(request.args['k'])
    return current_state()


@app.route('/api/current_state')
def current_state():
    return {'html': formatting.ide_text_list_to_html(ide.TEXT_LIST), 'caret_position': ide.CARET_POS}


def run():
    app.run(port=25003, debug=False)
    pass
