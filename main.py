from app.engine import create_flask

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+Shift+B to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # https://flask-docs-kr.readthedocs.io/ko/latest/errorhandling.html
    flask_app = create_flask()
    flask_app.run(debug=True, use_debugger=True, use_reloader=False)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
