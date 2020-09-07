def make_division_by(n):
    """This closure returns a function that returns the division
       of an x number by n 
    """
    def divide(m):
        return m//n

    return divide


def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))  # The expected output is 6

    division_by_5 = make_division_by(5)
    print(division_by_5(100))  # The expected output is 20

    division_by_18 = make_division_by(18)
    print(division_by_18(54))  # The expected output is 3


if __name__ == '__main__':
    import unittest

    class ClosureSuite(unittest.TestCase):
        def setUp(self):
            self.tests = {
                3: (18, 6),
                5: (100, 20),
                18: (54, 3)
            }

        def test_closure_make_division_by(self):
            for key, value in self.tests.items():
                division_function = make_division_by(key)
                self.assertEqual(division_function(value[0]), value[1])

        def tearDown(self):
            del(self.tests)

    #unittest.main()

    run()
