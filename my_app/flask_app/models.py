from . import db


class Message(db.Model):  # type: ignore
    """An example model that represents a message."""

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Message {self.id}>"
