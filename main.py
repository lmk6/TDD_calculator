import unittest.runner

import MVC_tests.ModelTests as ModelTest
import MVC_tests.ControllerTests as ControllerTest

if __name__ == "__main__":
    unittest.main(module=ModelTest)
    unittest.main(module=ControllerTest)
