from flask_restx import fields

world = {
    "world_id": fields.String(required=True, description="The world identifier"),
    "name": fields.String(required=True, description="The world name"),
}
