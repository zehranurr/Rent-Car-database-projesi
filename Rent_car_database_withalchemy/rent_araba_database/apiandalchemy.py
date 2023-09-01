from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import traceback

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = "change your url"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define your database models here (Arabalar, aboutus, Customer)
class Arabalar(db.Model):
    __tablename__ = 'Arabalar'

    id = db.Column(db.Integer, primary_key=True)
    marka = db.Column(db.String(255))
    model = db.Column(db.String(255))
    fiyat = db.Column(db.String(15)) 
    
    is_active = db.Column(db.Boolean)
    resim = db.Column(db.String(255))

# ...

@app.route('/arabalar', methods=['GET'])
def arabalar():
    
    # Replace this with code to fetch cars from your Arabalar database
    cars = Arabalar.query.all()
    print(cars)
    car_list = [{'id': car.id, 'marka': car.marka, 'model': car.model, 'fiyat': car.fiyat} for car in cars]
    return jsonify({'cars':car_list})

@app.route('/arabalar',methods=['POST'])
def arabaekle():

        

        # Create a new Arabalar object and add it to the datab
        new_araba = Arabalar(
            resim="yeni",
            marka="yeni",
            fiyat="456",
            model="marka_model",
            is_active =True)
        

        db.session.add(new_araba)
        db.session.commit()
    
        return jsonify({'message': 'Araba başarıyla eklendi'})




@app.route('/arabalar/<int:id>', methods=['DELETE'])
def gorev_sil(id):
    try:
        Arabalar.query.filter_by(id=id).delete()
        db.session.commit()
        return jsonify({'message': 'Araba silindi!'}), 200
    except Exception as e:
        # Hata izleme ve hata mesajını döndürme
        traceback.print_exc()


@app.route('/arabalar/<int:id>', methods=['PUT'])
def gorev_guncelle(id):

            araba = Arabalar.query.get(id)
            araba.model = "Şahin"
            araba.marka = "Tofaş"
            araba.fiyat = "150000"
            araba.resim = "aaaaaaa"
            db.session.commit()

            return jsonify({"id": araba.id, "marka": araba.marka, "model": araba.model, "fiyat": araba.fiyat, "resim":araba.resim})        









# You can add more API endpoints for creating, updating, and deleting cars as needed

if __name__ == '__main__':
    app.run(debug=True)
