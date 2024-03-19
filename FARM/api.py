from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/gazdak', methods=['GET'])
def get_gazdak():
    gazdak = [
        {'id': 1, 'nev': 'Gazda 1'},
        {'id': 2, 'nev': 'Gazda 2'},
        {'id': 3, 'nev': 'Gazda 3'}
    ]
    return jsonify(gazdak)

@app.route('/hazi_allatok', methods=['GET'])
def get_hazi_allatok():
    return jsonify({'message': 'Ez a hazi_allatok endpont'})

if __name__ == '__main__':
    app.run(debug=True)


app = Flask(__name__)


class Gazda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nev = db.Column(db.String(100), nullable=False)
    


@app.route('/gazdak', methods=['GET'])
def get_gazdak():
    gazdak = Gazda.query.all()
    return jsonify([gazda.serialize() for gazda in gazdak])


@app.route('/gazdak/<int:id>', methods=['GET'])
def get_gazda(id):
    
    return jsonify(gazda.serialize())


@app.route('/gazdak', methods=['POST'])
def create_gazda():
    data = request.json
    gazda = Gazda(nev=data['nev'])
   
    return jsonify(gazda.serialize()), 201


@app.route('/gazdak/<int:id>', methods=['PUT'])
def update_gazda(id):
    gazda = Gazda.query.get_or_404(id)
    data = request.json
    gazda.nev = data['nev']
    db.session.commit()
    return jsonify(gazda.serialize())


@app.route('/gazdak/<int:id>', methods=['DELETE'])
def delete_gazda(id):
    gazda = Gazda.query.get_or_404(id)
    db.session.delete(gazda)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
