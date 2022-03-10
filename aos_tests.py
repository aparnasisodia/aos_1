import unittest
import moodle_locators as locators
import aos_methods as methods

class aosAppPostiveTestCases(unittest.TestCase):

    @staticmethod   # single to units test that this is a static method
    def test_create_new_user():
        methods.setUp()
        methods.create_new_user()
        methods.sign_out()
        methods.log_in(locators.admin_username, locators.admin_password)
        methods.teardown()