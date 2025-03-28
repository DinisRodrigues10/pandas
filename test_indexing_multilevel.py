import pandas as pd
import numpy as np
import datetime as dt
import unittest

class TestDatetimeTypeConversion(unittest.TestCase):
    def setUp(self):
        # Create a DataFrame with date objects in the index
        dates = [dt.datetime(2019, 8, 1).date(), dt.datetime(2019, 8, 1).date(), dt.datetime(2019, 8, 2).date()]
        t1 = ["A", "B", "C"]
        t2 = ["C", "D", "E"]
        vals = [0.1, 0.2, 0.3]  # Fixed values for deterministic tests
        self.df = pd.DataFrame(data=np.array([dates, t1, t2, vals]).T, columns=["dates", "t1", "t2", "vals"])
        self.df.set_index(["dates", "t1", "t2"], inplace=True)
        self.date_np = np.datetime64("2019-08-01")
        self.date_py = dt.date(2019, 8, 1)
        
    def test_partial_indexing_with_numpy_datetime64(self):
        """Test partial indexing using numpy.datetime64 with date objects in index"""
        # Should return only the first row
        result_a = self.df.loc[(self.date_np, 'A')]
        print(result_a)
        self.assertEqual(len(result_a), 1)
        self.assertEqual(result_a.index[0], 'C')
        
        # Should return only the second row
        result_b = self.df.loc[(self.date_np, 'B')]
        self.assertEqual(len(result_b), 1)
        self.assertEqual(result_b.index[0], 'D')
        
        # Should raise KeyError - no entry with C on 2019-08-01
        with self.assertRaises(KeyError):
            self.df.loc[(self.date_np, 'C')]

if __name__ == "__main__":
    unittest.main()