from init import db
from shopyo.api.models import PkModel



class Note(PkModel):

    __tablename__ = 'notes'

    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)