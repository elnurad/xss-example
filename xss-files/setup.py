from model import db, Message 

db.connect()
db.create_tables([Message])
