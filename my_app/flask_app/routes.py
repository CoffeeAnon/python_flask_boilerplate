from flask_restx import Resource, fields, Namespace
from typing import List, Dict

api: Namespace = Namespace("hello_world", description="The Hello World namespace")

world: Dict[str, fields.String] = api.model(
    "World",
    {
        "world_id": fields.String(required=True, description="The world identifier"),
        "name": fields.String(required=True, description="The world name"),
    },
)

WORLDS: List[Dict[str, str]] = [
    {"world_id": "home", "name": "Earth"},
]


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
        return WORLDS


@api.route("/<world_id>")
@api.param("world_id", "The world identifier")
@api.response(404, "World not found")
class World(Resource):
    """Resource representing a single world"""

    @api.doc("get_world")
    @api.marshal_with(world)
    def get(self, world_id: str) -> Dict[str, str]:
        """Fetch a world given its identifier"""
        for entry in WORLDS:
            if entry["world_id"] == world_id:
                return entry
        api.abort(404)
        return {}
