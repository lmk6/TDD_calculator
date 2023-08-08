import unittest.runner

from MVC_tests.ControllerTests import ControllerTest
from MVC_tests.ModelTests import ModelTest

if __name__ == "__main__":
    loader = unittest.TestLoader()

    # Create test suites for ControllerTest and ModelTest
    controller_suite = loader.loadTestsFromTestCase(ControllerTest)
    model_suite = loader.loadTestsFromTestCase(ModelTest)

    # Combine the test suites
    combined_suite = unittest.TestSuite([controller_suite, model_suite])

    # Run the combined test suite
    unittest.TextTestRunner().run(combined_suite)
