from app.app import create_flask

if __name__ == '__main__':
    # https://flask-docs-kr.readthedocs.io/ko/latest/errorhandling.html
    flask_app = create_flask()
    flask_app.run(debug=True, use_debugger=True, use_reloader=False)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
