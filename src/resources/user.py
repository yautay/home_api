import sqlite3
from flask_restful import Resource, reqparse
from models.usermodel import UserModel


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("username",
                        type=str,
                        required=True,
                        help="This field can not be blank!"
                        )
    parser.add_argument("password",
                        type=str,
                        required=True,
                        help="This field can not be blank!")

    @classmethod
    def post(cls):
        data = cls.parser.parse_args()
        if UserModel.find_by_username(data["username"]) is None:
            new_user = UserModel(_id=None, username=data["username"], password=data["password"])
            new_user.insert()
        else:
            return {"message": "User with that name already exists"}, 400
        return {"message": "User created successfully"}, 201
