from app.entity.users_entity import UsersEntity
from app.extension import db
from app.resource import api_blueprint
from app.resource.data.ressponse_utils import to_ok, to_error


@api_blueprint.route('/user/<int:id>', methods=['GET'])
def get_user():
    item = db.session.get(UsersEntity, id)
    if item is not None:
        return to_ok(item.as_dict())
    else:
        return to_error("1000", "no item")
