import unittest
from signin_tests import SignInTest

sign_in_tests = unittest.defaultTestLoader.loadTestsFromTestCase(SignInTest)

smoke_tests = unittest.TestSuite([sign_in_tests])

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(smoke_tests)
