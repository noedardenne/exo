## commande de lancement ===> $ venv/scripts/activate

## commande de fermeture ===> $ deactivate

# Création de l'application web
from flask import Flask, render_template
app = Flask(__name__)

noms=[]

@app.route('/')
def accueil():
    return render_template("index.html")
@app.route('/open-source')
def open_source():
    return render_template("open-source.html")

@app.route('/cybersecurite')
def cybersecurite():
    return render_template("cybersecurite.html")



@app.route('/capitales/add/<pays>/<capitale>')
def capital(pays, capitale):
    noms.append((pays, capitale))
    return render_template("capitales/add.html", pays=pays, capitale=capitale, noms=noms)
@app.route('/capitales/remove/<pays>/<capitale>')
def remove_capitale(pays, capitale):
    couple = (pays, capitale)
    if couple in noms:
        noms.remove(couple)
        message = f"{pays} / {capitale} a été retiré."
    else:
        message = f"{pays} / {capitale} n'était pas dans la liste."

    return render_template("capitales/remove.html", message=message, noms=noms,)



# Démarrage de notre application web
if __name__ == '__main__':
    app.run(debug=True)
