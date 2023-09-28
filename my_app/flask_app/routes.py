from flask_restx import Resource, fields, Namespace
from typing import List, Dict
from flask import current_app
from flask_sqlalchemy.query import Query

from flask_restx import Resource
from .database import db
from .models import World
from .serializers import world_fields

api: Namespace = Namespace("hello_world", description="The Hello World namespace")
world: Dict[str, fields.String] = api.model("World", world_fields)


@api.route("/hello_world")
class HelloWorld(Resource):
    """Resource representing the 'hello_world' endpoint"""

    @api.doc("hello_world")
    def get(self) -> Dict[str, str]:
        return {"hello": "world"}


@api.route("/hello_all_worlds")
class WorldList(Resource):
    """Resource representing the 'hello_all_worlds' endpoint"""

    @api.doc("list_worlds")
    @api.marshal_list_with(world)
    def get(self) -> List[Dict[str, str]]:
        """List all worlds"""
        with current_app.app_context():
            worlds: Query = db.session.query(World).all()
            return [
                {"world_id": world.world_id, "name": world.name} for world in worlds
            ]


@api.route("/<world_id>")
@api.param("world_id", "The world identifier")
@api.response(404, "World not found")
class HelloWorldId(Resource):
    """Resource representing a single world"""

    @api.doc("get_world")
    @api.marshal_with(world)
    def get(self, world_id: str) -> Dict[str, str]:
        """Fetch a world given its identifier"""
        worlds: Query = db.session.query(World).all()
        for entry in worlds:
            if entry.world_id == world_id:
                return entry
        api.abort(404)
        return {}
