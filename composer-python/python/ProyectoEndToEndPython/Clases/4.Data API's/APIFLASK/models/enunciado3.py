from utils.db import db

class Enunciado3 (db.Model):
    __tablename__ = 'enunciado3'
    # index = db.Column(db.Integer, primary_key=True)
    # customer_city = db.Column(db.Text)
    # category_name = db.Column(db.Text)

    index = db.Column(db.BigInteger, primary_key=True) 
    Month = db.Column(db.BigInteger) 
    order_qty = db.Column(db.BigInteger)
    
    def to_dict(self):
        return {            
            "Month": self.Month,
            "order_qty": self.order_qty
        }

