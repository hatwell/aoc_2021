import unittest
from unittest import result


def read_input(path):
    file = open(path)
    return file
    
def clean_data(data):
    return int(data.replace('\n', ''))

def get_depths(input):
    depths = []
    file = read_input(input)
    for line in file:
        line = clean_data(line)
        depths.append(line)
    file.close()
    return depths

def find_differences(values_list):
    counter = 0
    for i, l in enumerate(values_list[0:-1]):
            if values_list[i+1] > values_list[i]:
                counter = counter +1
    return counter

def get_sliding_sums(values_list, interval):
    sums=[]
    for i, value in enumerate(values_list[0:-2]):
        window = [value,values_list[i+1], values_list[i+2]]
        sums.append(sum(window))
    return sums

class TestAdvent(unittest.TestCase):        
    def test_clean_depths(self):
        depths = get_depths('test.txt')
        self.assertEqual([1,2,3,4,5], depths)
        
    def test_with_real_file(self):
        depths = get_depths('day_1_input.txt')
        self.assertTrue(type(depths[0])== int)
        
    def test_find_differences(self):
        values = [1,2,3,4,3]
        result = find_differences(values)
        self.assertEqual(result, 3)
        
    def test_real_thing(self):
        depths = get_depths('day_1_input.txt')
        result = find_differences(depths)
        self.assertEqual(1583, result)
        
    def test_get_sliding_sum(self):
        result = get_sliding_sums([1,2,3,4], 3)
        self.assertEqual(result, [6, 9])
        
    def test_get_all_sums(self):
        depths = get_depths('day_1_input.txt')
        sums = get_sliding_sums(depths,3)
        diffs = find_differences(sums)
        self.assertEqual(diffs, 0)
        
if __name__ == "__main__":
    unittest.main()