from app.app import create_app
from app.config import DefaultConfig

"""
https://flask-docs-kr.readthedocs.io/ko/latest
"""
if __name__ == '__main__':
    app = create_app(DefaultConfig)
    app.run(debug=True, use_debugger=True, use_reloader=False)
