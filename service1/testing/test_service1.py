from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_player(self):
        with patch("requests.get") as g:
            with patch("requests.post") as r:
                g.return_value.text = "English"
                r.return_value.text = "-Silky- and plays for Manchester United"

                response = self.client.get(url_for("index"))
                self.assertIn(b"English English that has the quality -Silky- and plays for Manchester United", response.data)

