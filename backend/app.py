from flask import Flask, jsonify, request
from flask_cors import CORS
from models import db, Produit, Client, Commande

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
CORS(app)  # autorise le frontend Reflex à appeler l'API

with app.app_context():
    db.create_all()


# ---------- PRODUITS ----------

@app.route("/api/produits", methods=["GET"])
def get_produits():
    produits = Produit.query.all()
    return jsonify([p.to_dict() for p in produits])


@app.route("/api/produits/<int:produit_id>", methods=["GET"])
def get_produit(produit_id):
    produit = Produit.query.get_or_404(produit_id)
    return jsonify(produit.to_dict())


@app.route("/api/produits", methods=["POST"])
def create_produit():
    data = request.get_json()
    produit = Produit(
        nom=data["nom"],
        description=data.get("description"),
        prix=data["prix"],
        stock=data.get("stock", 0),
    )
    db.session.add(produit)
    db.session.commit()
    return jsonify(produit.to_dict()), 201


@app.route("/api/produits/<int:produit_id>", methods=["PUT"])
def update_produit(produit_id):
    produit = Produit.query.get_or_404(produit_id)
    data = request.get_json()
    produit.nom = data.get("nom", produit.nom)
    produit.description = data.get("description", produit.description)
    produit.prix = data.get("prix", produit.prix)
    produit.stock = data.get("stock", produit.stock)
    db.session.commit()
    return jsonify(produit.to_dict())


@app.route("/api/produits/<int:produit_id>", methods=["DELETE"])
def delete_produit(produit_id):
    produit = Produit.query.get_or_404(produit_id)
    db.session.delete(produit)
    db.session.commit()
    return jsonify({"message": "Produit supprimé"})


# ---------- CLIENTS ----------

@app.route("/api/clients", methods=["GET"])
def get_clients():
    clients = Client.query.all()
    return jsonify([c.to_dict() for c in clients])


@app.route("/api/clients/<int:client_id>", methods=["GET"])
def get_client(client_id):
    client = Client.query.get_or_404(client_id)
    return jsonify(client.to_dict())


@app.route("/api/clients", methods=["POST"])
def create_client():
    data = request.get_json()
    client = Client(
        nom=data["nom"],
        email=data.get("email"),
        telephone=data.get("telephone"),
    )
    db.session.add(client)
    db.session.commit()
    return jsonify(client.to_dict()), 201


@app.route("/api/clients/<int:client_id>", methods=["PUT"])
def update_client(client_id):
    client = Client.query.get_or_404(client_id)
    data = request.get_json()
    client.nom = data.get("nom", client.nom)
    client.email = data.get("email", client.email)
    client.telephone = data.get("telephone", client.telephone)
    db.session.commit()
    return jsonify(client.to_dict())


@app.route("/api/clients/<int:client_id>", methods=["DELETE"])
def delete_client(client_id):
    client = Client.query.get_or_404(client_id)
    db.session.delete(client)
    db.session.commit()
    return jsonify({"message": "Client supprimé"})


# ---------- COMMANDES ----------

@app.route("/api/commandes", methods=["GET"])
def get_commandes():
    commandes = Commande.query.all()
    return jsonify([c.to_dict() for c in commandes])


@app.route("/api/commandes/<int:commande_id>", methods=["GET"])
def get_commande(commande_id):
    commande = Commande.query.get_or_404(commande_id)
    return jsonify(commande.to_dict())


@app.route("/api/commandes", methods=["POST"])
def create_commande():
    data = request.get_json()

    produit = Produit.query.get_or_404(data["produit_id"])
    quantite = data.get("quantite", 1)

    if produit.stock < quantite:
        return jsonify({"error": "Stock insuffisant"}), 400

    total = produit.prix * quantite

    commande = Commande(
        client_id=data["client_id"],
        produit_id=data["produit_id"],
        quantite=quantite,
        total=total,
    )

    # mise à jour du stock
    produit.stock -= quantite

    db.session.add(commande)
    db.session.commit()
    return jsonify(commande.to_dict()), 201


@app.route("/api/commandes/<int:commande_id>", methods=["PUT"])
def update_commande(commande_id):
    commande = Commande.query.get_or_404(commande_id)
    data = request.get_json()

    nouvelle_quantite = data.get("quantite", commande.quantite)
    produit = commande.produit

    difference = nouvelle_quantite - commande.quantite

    if difference > 0 and produit.stock < difference:
        return jsonify({"error": "Stock insuffisant pour cette modification"}), 400

    produit.stock -= difference
    commande.quantite = nouvelle_quantite
    commande.total = produit.prix * nouvelle_quantite

    db.session.commit()
    return jsonify(commande.to_dict())


@app.route("/api/commandes/<int:commande_id>", methods=["DELETE"])
def delete_commande(commande_id):
    commande = Commande.query.get_or_404(commande_id)
    db.session.delete(commande)
    db.session.commit()
    return jsonify({"message": "Commande supprimée"})


# ---------- STATISTIQUES ----------

@app.route("/api/stats", methods=["GET"])
def get_stats():
    total_ventes = db.session.query(db.func.sum(Commande.total)).scalar() or 0
    nb_commandes = Commande.query.count()
    nb_clients = Client.query.count()
    nb_produits = Produit.query.count()

    return jsonify({
        "total_ventes": total_ventes,
        "nb_commandes": nb_commandes,
        "nb_clients": nb_clients,
        "nb_produits": nb_produits,
    })


@app.route("/api/stats/ventes-par-produit", methods=["GET"])
def get_ventes_par_produit():
    resultats = (
        db.session.query(Produit.nom, db.func.sum(Commande.total).label("total"))
        .join(Commande, Commande.produit_id == Produit.id)
        .group_by(Produit.nom)
        .all()
    )
    return jsonify([{"produit": r.nom, "total": r.total} for r in resultats])


if __name__ == "__main__":
    app.run(debug=True, port=5001)