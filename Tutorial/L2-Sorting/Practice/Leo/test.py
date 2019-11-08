# import test case
import sort 

# import test framework
import unittest


array1 = [2,5,1];
array2 = [4,8,6,5,9,7];

class Test(unittest.TestCase):
    def test_swap(self):
        self.assertEqual(sort._swap_helper(array1, 0, 1), [5,2,1])

    def test_selection_sort(self):
        self.assertEqual(sort.selection_sort_alg(array1), array1.sort())
        self.assertEqual(sort.selection_sort_alg(array2), array2.sort())
        # self.assertEqual(sort.insertion_sort_alg(array2), array2.sort())

if __name__ == '__main__':
    unittest.main()