## commande de lancement ===> venv/scripts/activate

## commande de fermeture ===> deactivate

# Création de l'application web
from flask import Flask
app = Flask(__name__)

# Notre première route
@app.route('/')
def index():
    return "<h1>Bonjour la classe !</h1>"

@app.route('/Team')
def Team():
    return "<h6>!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!</h6>"

# Démarrage de notre application web
if __name__ == '__main__':
    app.run(debug=True)
