from markovwordchain import MarkovWordChain 
import random 

def get_word_list(sentence_list):
    words = []
    for sentence in sentence_list: 
        word_list = sentence.split()
        for word in word_list:
            words.append(word)
    return words

def get_starter_words(sentence_list, power):
    starter_words = [] 
    for sentence in sentence_list: 
        word_list = sentence.split() 
        start_slice = word_list[0:power]
        start_word = ' '.join(start_slice)
        starter_words.append(start_word)
    return starter_words

def get_ending_words(sentence_list):
    ending_words = [] 
    for sentence in sentence_list:
        word_list = sentence.split()
        if len (word_list) == 0:
            continue
        ending_words.append(word_list[-1])
    return ending_words

def get_new_starter_word(old_stater_word, picked_word, power):
    temp_phrase = old_stater_word + " " + picked_word 
    word_list = temp_phrase.split() 
    new_starter = ' '.join(word_list[-power:])
    return new_starter

class SentenceGenerator: 
    def __init__(self, sentence_list, power): 
        self.power = power
        self.starter_word_list = get_starter_words(sentence_list,power)
        self.end_word_list = get_ending_words(sentence_list)
        self.markov_chain = MarkovWordChain(get_word_list(sentence_list), power)

    def generate_sentence(self, sentence_length):
        starter_word = random.choice(self.starter_word_list)
        sentence = starter_word + " "
        for i in range(sentence_length):
            picked_word = self.markov_chain.next_word(starter_word)

            if picked_word == None:
                break

            sentence = sentence + picked_word + " "
            
            if picked_word in self.end_word_list:
                will_continue = random.randint(0,1)
                if will_continue == 1 and len(sentence.split()) >= 8: 
                    break 

            starter_word = get_new_starter_word(starter_word, picked_word, self.power)
        
        return sentence


        