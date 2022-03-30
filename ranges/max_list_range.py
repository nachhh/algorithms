"""Given a list of integers find the maximum subset of elements which form
an ordered consecutive range when sorted (find a max range).
For example, for:
input: [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
{1, 0, 3, 5, 2, 4, 7, 6} is such a subset, because when ordered we get
[0, 1,.., 7]
and there is no greater subset.

For the output just return the first and last elements of the range, i.e.
[0, 7] for the example above.  
"""
import unittest


def max_list_range(A):
    """ O(n) time/space solution
    """
    max_range = 0
    h_map = {i:1 for i in A}
    left = right = None

    for x in h_map.keys():
        r = x + 1
        while r in h_map.keys():
            next = h_map.get(r)
            r += 1
            if next > 1:
                h_map[x] += next
                break
            else:
                h_map[x] += 1

        if h_map[x] > max_range:
            max_range = h_map[x]
            if h_map.get(x + max_range - 1, None):
                right = x + max_range - 1
                left = x
            else:
                right = x
                left = x - max_range - 1
    return [left, right]


class MaxListRangeTests(unittest.TestCase):

    def test_random(self):
        l1 = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
        self.assertEqual(max_list_range(l1), [0, 7])

        l2 = [15, 14, 3, 5, 4, 13, 12, 11]
        self.assertEqual(max_list_range(l2), [11, 15])

    def test_ordered(self):
        l3 = [1, 2, 3, 4, 7, 8, 9, 10, 11]
        self.assertEqual(max_list_range(l3), [7, 11])

        l4 = [1, 2, 3, 4, 5, 8, 9, 10, 11]
        self.assertEqual(max_list_range(l4), [1, 5])

    def test_duplicated(self):
        l5 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 3, 3, 4, 4, 4]
        self.assertEqual(max_list_range(l5), [2, 4])

    def test_single(self):
        l6 = [1, 3, 5, 7]
        self.assertEqual(max_list_range(l6), [1, 1])

    def test_empty(self):
        l7 = []
        self.assertEqual(max_list_range(l7), [None, None])

    def test_negatives(self):
        l = [2, 6, 8, 15, 3, 1, 0, 17, -1, -2]
        self.assertEqual(max_list_range(l), [-2, 3])