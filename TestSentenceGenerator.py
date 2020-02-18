from markovwordchain import generate_map 
import unittest 

class TestWordMatrix(unittest.TestCase):
    def test_empty_list_power_1(self): 
        power_test = 1 
        words = [] 
        word_matrix = generate_map(words = words, power = power_test)

        expected_map = {}

        self.assertEqual(word_matrix, expected_map, "Generated not expected")

    def test_empty_list_power_2(self):
        power_test = 2 
        words = [] 
        word_matrix = generate_map(words = words, power = power_test)

        expected_map = {} 

        self.assertEqual(word_matrix, expected_map, "Generated not expected")
   
    def test_word_list_length_same_as_power(self):
        power_test = 2 
        words = ["one","two"]
        word_matrix = generate_map(words = words, power = power_test)

        expected_map = {} 

        self.assertEqual(word_matrix, expected_map, "Generated not expected")

    def test_three_words_power_2(self):
        power_test = 2 
        words = ["one", "two", "three"]
        word_matrix = generate_map(words = words, power = power_test)

        expected_map = {"one two":["three"]} 

        self.assertEqual(word_matrix, expected_map, "Generated not expected")

    def test_word_list_nonrepeating_power_2(self):
        power_test = 2 
        words = ["I", "am", "the", "King", "of", "the", "person"]
        word_matrix = generate_map(words = words, power = power_test)

        expected_map = {"I am": ["the"], "am the": ["King"], "the King":["of"], "King of":["the"], "of the":["person"]}
        
        self.assertEqual(word_matrix, expected_map, "Genratred not expected")

    def test_word_list_repeating_power_2(self):
        power_test = 2 
        words = ["no", "no", "yes", "no", "no", "yes", "no"]
        word_matrix = generate_map(words = words, power = power_test)

        expected_map = {"no no":["yes", "yes"], "no yes":["no","no"], "yes no": ["no"]}

        self.assertEqual(word_matrix, expected_map, "Generated not expected")
    
    def test_word_list_all_repeating_power_2(self):
        power_test = 2 
        words = ["no", "no", "no", "no", "no"]
        word_matrix = generate_map(words = words, power = power_test)
        
        expected_map = {"no no": ["no","no","no"]}

        self.assertEqual(word_matrix, expected_map, "Generated not expected")


if __name__ == '__main__':
    unittest.main()