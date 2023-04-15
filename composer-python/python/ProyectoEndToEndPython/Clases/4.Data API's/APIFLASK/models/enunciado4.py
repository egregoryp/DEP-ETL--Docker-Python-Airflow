from utils.db import db

class Enunciado4 (db.Model):
    __tablename__ = 'enunciado4'
    # index = db.Column(db.Integer, primary_key=True)
    # customer_city = db.Column(db.Text)
    # product_name = db.Column(db.Text)
    # quantity = db.Column(db.BigInteger)
    # total = db.Column(db.Float)
     
    index           = db.Column(db.BigInteger, primary_key=True)
    customer_id     = db.Column(db.BigInteger)
    customer_fname  = db.Column(db.Text) 
    customer_lname  = db.Column(db.Text) 
    purchases_total = db.Column(db.BigInteger)
    
    def to_dict(self):
        return {
            "id": self.customer_id,
            "customer_fname": self.customer_fname,
            "customer_lname" : self.customer_lname,            
            "purchases_total": self.purchases_total            
        }

