from flask import Flask, json
import requests

__author__ = 'Alisson Tenorio Pinto'
__email__ = 'alisson@nti.ufal.br'


class Load:
    app = Flask(__name__)
    json_filename = "data.json"
    json_url = "https://nti.ufal.br/glpizabbix/unidades"
    url_part1 = "https://nti.ufal.br/servicedesk/front/ticket.php?is_deleted=0&criteria%5B0%5D%5Bfield%5D=83&criteria%5B0%5D%5Bsearchtype%5D=under&criteria%5B0%5D%5Bvalue%5D="
                #"60"
    url_part2 = "&criteria%5B1%5D%5Blink%5D=AND&criteria%5B1%5D%5Bfield%5D=8&criteria%5B1%5D%5Bsearchtype%5D=equals&criteria%5B1%5D%5Bvalue%5D=mygroups&criteria%5B2%5D%5Blink%5D=AND&criteria%5B2%5D%5Bfield%5D=12&criteria%5B2%5D%5Bsearchtype%5D=equals&criteria%5B2%5D%5Bvalue%5D=notold&search=Pesquisar&itemtype=Ticket&start=0&_glpi_csrf_token=7762574fbfdbbca2ecad73d4356ed7cf"

    @staticmethod
    def get_headers():
        return {'content-type': 'application/json'}

    def search_test(self, url):
        #print(self.json_url)
        r = requests.get(self.json_url, self.get_headers(), verify=False)

        print(r.json())
        if r is not None and r.json() is not None:
            for k in r.json():
                if url.lower() == r.json()[str(k)].lower():
                    #print(r.json()[str(k)])
                    return self.url_part1 + str(k) + self.url_part2
        return None

    #@staticmethod
    #def search(url):
    #    jsondata = Load.load_json()

    #    if jsondata is not None:
    #        for p in jsondata:
    #            if url.lower() == p['name'].lower():
    #                return p['url']
    #    return None

    #@staticmethod
    #def load_json():
    #    url = Load.app.root_path + "/" + Load.json_filename
    #    with open(url) as jsonfile:
    #        try:
    #            data = json.load(jsonfile)
    #        except:
    #            data = None
    #    return data

