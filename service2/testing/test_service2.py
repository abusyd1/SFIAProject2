#!/usr/bin/python3

import unittest
from flask import url_for
from flask_testing import TestCase

from application import app

class Testbase(TestCase):
    def create_app(self):
        return app

class TestCreate(Testbase):
    def test_char(self):
        for _ in range(5):
            response=self.client.get(url_for("position"))
            self.assertEqual(response.status_code,200)
            self.assertIn(response.data, [b'Goalkeeper',b"Defender", b"Midfielder", b"Striker"])
