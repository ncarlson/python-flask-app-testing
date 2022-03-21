from flask import request, jsonify
from flask import Flask


class App(object):

    def __init__(self):
        print('noop')

        # Create real service if not mocking
        # if not mail_service:
        #     from example_libs.mail_service import MailService
        #     mail_service = MailService()
        # self.mail_service = mail_service

    def create_app(self):
        app = Flask(__name__)
        app.app_context().push()

        @app.route("/health", methods=["GET"])
        def health():
            summary = {
                "mail_service": "not_found",
            }
            return jsonify(summary)


        @app.route("/hello", methods=["GET"])
        def hello():
            return "<p>hello, world</p>"


        @app.route("/fizz", methods=["GET"])
        def fizz():
            return "<p>fuzz</p>"


        @app.route("/throw-exception", methods=["PUT"])
        def error():
            raise Exception("An error has occurred")

        return app

if __name__ == "__main__":
    App().create_app().run(host="0.0.0.0")