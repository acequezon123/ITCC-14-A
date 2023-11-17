from flask import Flask, jsonify, request

app = Flask(__name__)

# Shoe array acts as the database for the api
shoeData = []


# Get method for getting all the shoe data
@app.route('/shoes', methods=['GET'])
def findShoe():
    return jsonify({'shoes': shoeData})

#
# Get method for getting the shoe by id
@app.route('/shoes/<int:shoeId>', methods=['GET'])
def findShoeById(shoeId):
    shoe = next((item for item in shoeData if item['id'] == shoeId), None)
    if shoe:
        return jsonify({'shoe': shoe})
    else:
        return jsonify({'Error': 'Shoe not found'}), 404


# Post method for posting the data of the shoe
@app.route('/shoes', methods=['POST'])
def postShoe():
    data = request.get_json()

    new_shoe = {
        'id': data['id'],
        'shoeName': data['shoeName'],
        'brandName': data['brandName'],
        'releaseDate': data['releaseDate'],
        'deadStockDate': data['deadStockDate']
    }

    shoeData.append(new_shoe)
    return jsonify({'created': 'created'}), 201


# Get method that uses a filter to search shoe by releaseDate
@app.route('/shoes/filter', methods=['GET'])
def findShoeByReleaseDate():
    realeaseDate = request.args.get('releaseDate')

    if realeaseDate:
        filteredShoe = [shoe for shoe in shoeData if shoe.get('releaseDate') == realeaseDate]
        return jsonify({'shoes': filteredShoe})
    else:
        return jsonify(), 400


# Get method for searching a shoe by brandName
@app.route('/shoes/search', methods=['GET'])
def findShoeByBrand():
    brandName = request.args.get('brandName')

    if brandName:
        brandShoes = [shoe for shoe in shoeData if shoe.get('brandName') == brandName]
        return jsonify({'shoes': brandShoes})
    else:
        return jsonify(), 400


# Put method for updating shoe by id
@app.route('/shoes/<int:shoeId>', methods=['PUT'])
def updateShoe(shoeId):
    data = request.get_json()

    shoe = next((item for item in shoeData if item.get('id') == shoeId), None)

    if shoe:

        shoe.update({
            'shoeName': data['shoeName'],
            'brandName': data['brandName'],
            'releaseDate': data['releaseDate'],
            'deadStockDate': data['deadStockDate']
        })
        return jsonify({'ok': 'ok'}), 200
    else:
        return jsonify({'Error': 'Shoe not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
