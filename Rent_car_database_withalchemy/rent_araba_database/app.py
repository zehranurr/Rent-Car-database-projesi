from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "change your url"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)




class araba(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    model=db.Column(db.String(200))
    fiyat=db.Column(db.Float)
    marka=db.Column(db.String(200))




    def __repr__(self):
        return f'<araba: {self.model}>'

class Arabalar(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    model=db.Column(db.String(200))
    fiyat=db.Column(db.Float)
    marka=db.Column(db.String(200))
    yıl=db.Column(db.Integer)
    fiyat=db.Column(db.Float)
    resim=db.Column(db.String(250))

    def __repr__(self):
        return f'<Arabalar: {self.model}>'
    







if __name__ == '__main__': # Create the database tables within the Flask application contex
    with app.app_context():
    # Now you can safely perform database queries
        results = Arabalar.query.all()
        for result in results:
            print(result)   
    app.run(debug=True)