from flask import Flask, json

__author__ = 'Alisson Tenorio Pinto'
__email__ = 'alisson@nti.ufal.br'


class Load:
    app = Flask(__name__)
    jsonfilename = "data.json"

    @staticmethod
    def search(url):
        jsondata = Load.load_json()

        if jsondata is not None:
            for p in jsondata:
                if url.lower() == p['name'].lower():
                    return p['url']
        return None

    @staticmethod
    def load_json():
        url = Load.app.root_path + "/" + Load.jsonfilename
        with open(url) as jsonfile:
            try:
                data = json.load(jsonfile)
            except:
                data = None
        return data

