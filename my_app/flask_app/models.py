from .database import db, BaseModel


class Message(BaseModel):
    """An example model that represents a message."""

    __tablename__ = "messages"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Message {self.id}>"


class World(BaseModel):
    """Model representing a world"""

    __tablename__ = "worlds"
    world_id: str = db.Column(db.String(50), primary_key=True)
    name: str = db.Column(db.String(50), nullable=False)

    def __repr__(self) -> str:
        return f"<World {self.world_id}>"
