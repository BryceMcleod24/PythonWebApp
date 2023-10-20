"""
Author: Bryce McLeod

This Flask application allows users to manage items by adding, editing, or deleting them in a Firebase database.
Each item contains a name, description, price, and an image which is stored and retrieved from Firebase Storage.
"""
from flask import Flask, render_template, request, redirect
import firebase_admin
from firebase_admin import credentials, firestore, storage
from werkzeug.utils import secure_filename

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'webapp-project-9fe5e.appspot.com'
})
db = firestore.client()
bucket = storage.bucket()

app = Flask(__name__)

def upload_image(file):
    if file:
        filename = secure_filename(file.filename)
        blob = bucket.blob(filename)
        blob.upload_from_file(file)
        blob.make_public()
        return blob.public_url
    return None

class Item:
    def __init__(self, id, name, description, image_url, price):
        self.id = id
        self.name = name
        self.description = description
        self.image_url = image_url
        self.price = price

@app.route('/')
def home():
    sort_by = request.args.get('sort_by', 'id')
    search_keyword = request.args.get('search')
    search_id = request.args.get('search_id')
    items_ref = db.collection('items')
    items = []

    for doc in items_ref.stream():
        doc_dict = doc.to_dict()
        items.append(Item(id=doc.id,
                          name=doc_dict['name'],
                          description=doc_dict['description'],
                          image_url=doc_dict['image_url'],
                          price=doc_dict['price']))

    if search_id:
        items = [item for item in items if item.id == search_id]
    if search_keyword:
        items = [item for item in items if search_keyword.lower() in item.name.lower()]
    if sort_by in ['name', 'description']:
        items.sort(key=lambda x: getattr(x, sort_by))

    return render_template('homepage.html', items=items)

# Add
@app.route('/add_item', methods=['POST'])
def add_item():
    data = request.form
    image = request.files['gameImage']
    image_url = upload_image(image)

    if image_url:
        item_data = {
            'name': data.get('gameName'),
            'description': data.get('gameDescription'),
            'image_url': image_url,
            'price': data.get('gamePrice')
        }
        db.collection('items').add(item_data)
    return redirect('/')

# Edit
@app.route('/edit_item/<string:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    print("Editing item with ID:", item_id)  # Debugging line to print the item ID
    if request.method == 'POST':
        data = request.form
        image = request.files['gameImage']

        item_ref = db.collection('items').document(item_id)
        item_data = {
            'name': data.get('gameName'),
            'description': data.get('gameDescription'),
            'price': data.get('gamePrice')
        }

        if image.filename != '':
            image_url = upload_image(image)
            if image_url:
                item_data['image_url'] = image_url

        item_ref.update(item_data)
        return redirect('/')
    else:
        item = db.collection('items').document(item_id).get().to_dict()
        item['price'] = float(item['price'])
        return render_template('edit_item.html', item=item)

#Delete
@app.route('/delete_item/<string:item_id>')
def delete_item(item_id):
    db.collection('items').document(item_id).delete()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)