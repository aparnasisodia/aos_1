import unittest
import aos_locators as locators
import aos_methods as methods

class aosAppPostiveTestCases(unittest.TestCase):

    @staticmethod   # single to units test that this is a static method
    def test_create_new_user():
        methods.setUp()
        methods.create_new_user()
        methods.sign_out()
        methods.log_in(locators.new_username, locators.new_password)
        methods.teardown()
