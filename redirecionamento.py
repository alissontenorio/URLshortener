from flask import Flask, redirect, json

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/load")
def loadJson():
    url = app.root_path+'/static/data.json'
    with open(url) as jsonfile:
        data = json.load(jsonfile)
    return data

@app.route("/cied")
def redirecionamentoCIED():
    return redirect(
        "https://nti.ufal.br/servicedesk/front/ticket.php?is_deleted=0&criteria%5B0%5D%5Bfield%5D=83&criteria%5B0%5D%5Bsearchtype%5D=equals&criteria%5B0%5D%5Bvalue%5D=44&search=Pesquisar&itemtype=Ticket&start=0&_glpi_csrf_token=4e4c1b74629ffd57e41da184467c5340",
        code=302)


if __name__ == "__main__":
    app.run()
