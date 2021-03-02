#!/usr/bin/python3

import unittest
from flask import url_for
from flask_testing import TestCase
from application import app

class Testbase(TestCase):
    def create_app(self):
        return app

class TestCreate(Testbase):
    def test_player(self):
        for _ in range(8):
            response=self.client.get(url_for("nationality"))
            self.assertEqual(response.status_code,200)
            self.assertIn(response.data, [b"English", b"French", b"German", b"Italian", b"Portuguese", b"American", b"Spanish"])