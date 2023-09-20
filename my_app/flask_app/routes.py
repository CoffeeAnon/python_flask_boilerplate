from flask_restx import Resource, fields, Namespace
from typing import List, Dict

api: Namespace = Namespace("hello_world", description="The Hello World namespace")

world: Dict[str, fields.String] = api.model(
    "World",
    {
        "id": fields.String(required=True, description="The world identifier"),
        "name": fields.String(required=True, description="The world name"),
    },
)

WORLDS: List[Dict[str, str]] = [
    {"id": "home", "name": "Earth"},
]


@api.route("/hello_world")
class HelloWorld(Resource):
    @api.doc("hello_world")
    def get(self) -> Dict[str, str]:
        return {"hello": "world"}


@api.route("/hello_all_worlds")
class WorldList(Resource):
    @api.doc("list_worlds")
    @api.marshal_list_with(world)
    def get(self) -> List[Dict[str, str]]:
        """List all worlds"""
        return WORLDS


@api.route("/<id>")
@api.param("id", "The world identifier")
@api.response(404, "World not found")
class World(Resource):
    @api.doc("get_world")
    @api.marshal_with(world)
    def get(self, id: str) -> Dict[str, str]:
        """Fetch a world given its identifier"""
        for world in WORLDS:
            if world["id"] == id:
                return world
        api.abort(404)
        return {}
