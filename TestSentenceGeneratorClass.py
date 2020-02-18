import unittest 
from sentencegenerator import get_new_starter_word 

class TestSentenceGenerator(unittest.TestCase):
    def test_get_starter_word(self): 
        starter_word = "who"
        picked_word = "is"
        power = 1 

        actual_starter_word = get_new_starter_word(starter_word, picked_word, power)

        expected = "is"
        self.assertEqual(actual_starter_word, expected, "Error")
    
    def test_get_start_word_power_2(self):
        starter_word = "Who is"
        picked_word = "the"
        power = 2 

        new_stater_word = get_new_starter_word(starter_word, picked_word, power) 

        expected = "is the"
        self.assertEqual(new_stater_word, expected, "Error")

    def test_get_start_word_power_3(self): 
        starter_word = "Who is the"
        picked_word = "king"
        power = 3 

        actual_starter_word = get_new_starter_word(starter_word, picked_word, power) 

        expected = "is the king"
        self.assertEqual(actual_starter_word, expected, "Error")


if __name__ == "__main__":
    unittest.main()