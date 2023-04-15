from utils.db import db

class Enunciado2 (db.Model):
    __tablename__ = 'enunciado2'

    index           = db.Column(db.BigInteger, primary_key=True)
    customer_id     = db.Column(db.BigInteger) 
    customer_fname  = db.Column(db.Text) 
    customer_lname  = db.Column(db.Text) 
    order_qty       = db.Column(db.BigInteger)

    def to_dict(self):
        return {
            "id": self.customer_id,
            "customer_fname": self.customer_fname,
            "customer_lname" : self.customer_lname,            
            "order_qty": self.order_qty            
        }
