﻿""" Импортирование библиотеки для работы с Flask и запусков субпроцессов. """

import subprocess
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def welcome():
    """ Эта функция запускает и отвечает за процесс возврата результата index.html. """

    return render_template('index.html')


@app.route("/error")
def error():
    """Эта функция запускает и отвечает за процесс возврата результата oopss.html."""
    return render_template('oopss.html')


@app.route("/runallure")
def run_allure():
    """ Эта функция запускает и отвечает за генерацию отчета allure. """

    cmd = ["powershell", "./scriptsh/runallure.ps1"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)


@app.route("/run_ui")
def run_ui():
    """ Эта функция запускает и отвечает за тесты страницы /example. """

    cmd = ["powershell", "./scriptsh/run_ui.ps1"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)


if __name__ == "__main__":
    app.run(debug=True)
