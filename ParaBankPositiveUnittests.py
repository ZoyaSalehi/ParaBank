import unittest
import para_bank_methods as pbm
import para_bank_locatotrs as pb

class ParaBankPositiveUnittests(unittest.TestCase):

    @staticmethod
    def test_registration():
        pbm.setUp()
        pbm.register()
        pbm.log_out()
        pbm.log_in(pb.new_username, pb.new_password)
        pbm.create_new_account()
        pbm.check_account_activity()
        pbm.log_out()
        pbm.tearDown()