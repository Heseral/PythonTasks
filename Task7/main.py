import re

from flask import Flask, render_template
import xml.dom.minidom
import urllib.request

app = Flask(__name__)


@app.route('/')
def index():
    main_node = XMLHandler.get_main_node("http://www.cbr.ru/scripts/XML_daily.asp")
    valutes = []
    for raw_valute in main_node.getElementsByTagName("Valute"):
        valutes.append(Valute(
            raw_valute.getElementsByTagName("Name")[0].firstChild.data,
            raw_valute.getElementsByTagName("CharCode")[0].firstChild.data,
            raw_valute.getElementsByTagName("Nominal")[0].firstChild.data,
            raw_valute.getElementsByTagName("Value")[0].firstChild.data
        ))
    return render_template(
        'index.html',
        valutes=valutes
    )


class XMLHandler(object):
    @staticmethod
    def get_main_node(url):
        try:
            http_response = urllib.request.urlopen(url)
        except:
            http_response = url

        return xml.dom.minidom.parse(http_response).documentElement

    @staticmethod
    def get_humanreadable_data(nodelist, result):
        for node in nodelist.childNodes:
            if node.childNodes is not None and len(node.childNodes) > 0:
                return result.append(XMLHandler.get_humanreadable_data(node.childNodes))


class Valute(object):
    def __init__(self, name, char_code, nominal, value):
        self.name = name
        self.char_code = char_code
        self.value = float(re.sub(",", ".", value)) / float(re.sub(",", ".", nominal))


if __name__ == "__main__":
    if __name__ == "__main__":
        app.run(debug=True)
