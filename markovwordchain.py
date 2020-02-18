import random 

def generate_map(words,power):
    word_matrix = {} 

    for i in range(0, len(words)-power,1):
        current_word = get_word(words, power, i)
        next_word = words[i+power] 

        if current_word in word_matrix:
            word_list = word_matrix[current_word]
            word_list.append(next_word)
            word_matrix[current_word] = word_list 
        else:
            word_list = [next_word]
            word_matrix[current_word] = word_list
    
    return word_matrix

def get_word(words, power, index):
    key = ""
    for i in range(index, index+power, 1):
        key = key + words[i] + " "
    return key.strip() 

class MarkovWordChain: 

    def __init__(self, word_list, power):
        self.word_list = word_list
        self.word_map = self.train(word_list, power)

    def train(self, word_list, power):
        word_map = generate_map(word_list, power)
        return word_map
    
    def next_word(self, keyword):
        if keyword in self.word_map:
            word_list = self.word_map[keyword]
            return random.choice(word_list)
        else: 
            return None 