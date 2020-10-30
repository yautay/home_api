from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from models.localizationmodel import LocalizationModel


class Localization(Resource):

    @jwt_required()
    def get(self, name):
        try:
            localization = LocalizationModel.find_by_name(name)
        except:
            return {"message": "An error occurred searching for localization"}, 500
        if localization:
            return localization.json()
        else:
            return {"message": "Localization not found"}, 404

    @jwt_required()
    def post(self, name):
        try:
            if LocalizationModel.find_by_name(name):
                return {"message": "An localization with name '{}' already exists.".format(name)}, 400
        except:
            return {"message": "An error occurred searching for localization"}, 500

        localization = LocalizationModel(name=name)
        try:
            localization.save_to_db()
        except:
            return {"message": "An error occurred inserting the localization"}, 500

        return localization.json(), 201

    @jwt_required()
    def delete(self, name):
        try:
            localization = LocalizationModel.find_by_name(name)
        except:
            return {"message": "An error occurred searching for localization"}, 500
        if localization is not None:
            try:
                localization.delete_from_db()
                return {"message": "Localization deleted"}
            except:
                return {"message": "An error occurred deleting localization"}, 500
        else:
            return {"message": "An localization with name '{}' does not exists.".format(name)}, 404


class LocalizationList(Resource):

    @jwt_required()
    def get(self):
        return {"localizations": [localization.json() for localization in LocalizationModel.query.all()]}
        # return {"relays": list(map(lambda x: x.json, RelayModel.query.all()))}
