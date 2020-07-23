import unittest
import pandas as pd

from DataFetcher.DataFetcher import DataFetcher


class Routes_Tests(unittest.TestCase):

    def testGetCompaniesNone(self):
        p = DataFetcher.get_countries(None)
        self.assertIsNotNone(p)
        self.assertIsInstance(p, pd.DataFrame)
        self.assertEqual(p.shape, (249, 16))


if __name__ == '__main__':
    unittest.main()
