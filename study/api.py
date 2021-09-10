from flask import Flask

class Api:
  def apiStudy1():

    # print()

    app = Flask (__name__)
    
    @app.route('/')
    def hello_world():
        return 'Hello, World!'
    
    if __name__ == "__main__":
        app.run()