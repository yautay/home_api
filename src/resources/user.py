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
        try:
            user = UserModel.find_by_username(data["username"])
        except:
            return {"message": "An error occurred searching for user"}, 500

        if user:
            return {"message": "An user with name '{}' already exists.".format(data["username"])}, 400
        else:
            user = UserModel(**data)
            try:
                user.save_to_db()
                return {"message": "User created successfully"}, 201
            except:
                return {"message": "An error occurred inserting user"}, 500


