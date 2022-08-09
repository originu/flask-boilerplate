import base64

from flask_jwt_extended import create_access_token, create_refresh_token, unset_jwt_cookies, get_jwt_identity

from app.extension import bcrypt
from app.resource import api_blueprint
from app.resource.data.ressponse_utils import to_ok


@api_blueprint.route('/auth/signup', methods=['GET'])
def sign_up():
    user_id = "kevin"
    plain_user_password = "kevin"
    encrypted_user_password = base64.b64encode(bcrypt.generate_password_hash(plain_user_password))
    return to_ok()


@api_blueprint.route('/auth/signin', methods=['GET'])
def sign_in():
    user_id = "kevin"
    plain_user_password = "kevin"

    encrypted_user_password = base64.b64encode(bcrypt.generate_password_hash(plain_user_password))
    bcrypt.check_password_hash(base64.b64decode(encrypted_user_password), plain_user_password)

    additional_claims = {
        "app": "jedivin"
    }
    _access_token = create_access_token(identity=user_id, additional_claims=additional_claims, fresh=True)
    _refresh_token = create_refresh_token(identity=user_id, additional_claims=additional_claims)
    return to_ok({
        "access_token": _access_token,
        "refresh_token": _refresh_token
    })


@api_blueprint.route('/auth/signout', methods=['GET'])
def sign_out():
    res = to_ok({
        "message": "logout successful"
    })
    unset_jwt_cookies(res)
    return res


@api_blueprint.route('/auth/protected', methods=['GET'])
def protected():
    identity_user_id = get_jwt_identity()
    return to_ok({
        "logged_in_as": identity_user_id
    })
