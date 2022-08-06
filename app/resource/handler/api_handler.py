from flask import render_template

from app.resource import api_blueprint


@api_blueprint.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404
