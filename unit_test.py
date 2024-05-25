import unittest
from utils import VisitorAnalyticsUtils

class TestProject(unittest.TestCase):

    def testLoadDataFile(self):
        utilities = VisitorAnalyticsUtils()
        df = utilities.loadDataFile()
        print("Number of Columns")
        print(len(df.columns))
        self.assertEqual(len(df.columns), 34)
        print("\nNumber of Rows")
        print(len(df.index))
        self.assertEqual(len(df.index), 479)

unittest.main()

