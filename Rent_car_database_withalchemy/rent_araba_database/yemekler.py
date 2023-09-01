from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import traceback
from sqlalchemy import create_engine, Column, Integer, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



app = Flask(__name__ )
app.config['SQLALCHEMY_DATABASE_URI'] = 'change your url'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Yemekler(db.Model):
    __tablename__='Yemekler'
    id = db.Column(db.Integer, primary_key=True)
    yemek_adı = db.Column(db.String(255))
    
    fiyat = db.Column(db.Double(255)) 
    kategori= db.Column(db.String(255))
    
    aciklama = db.Column(db.String(255))
    resim = db.Column(db.String(255))



@app.route('/yemekler',methods=['GET'])
def yemeks():
    yemeks=Yemekler.query.all()

    return jsonify  ([{'id': yemek.id, 'yemek_adı': yemek.yemek_adı, 'fiyat': yemek.fiyat, 'kategori': yemek.kategori,'aciklama':yemek.aciklama,'resim':yemek.resim} for yemek in yemeks])





@app.route('/yemekler/<int:id>', methods=['GET'])
def gorevget(id):
    yemeks = Yemekler.query.get(id)
    
    return jsonify  ([{'id': yemek.id, 'yemek_adı': yemek.yemek_adı, 'fiyat': yemek.fiyat, 'kategori': yemek.kategori,'aciklama':yemek.aciklama,'resim':yemek.resim} for yemek in yemeks])


    

if __name__ == '__main__':
    app.run(debug=True)


