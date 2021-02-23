from load_dictionary import load

word_list = load("2of4brif.txt") + load("dictionary.txt") + load("dictionary2.txt")
word_list = list(dict.fromkeys(word_list)) #no duplicates

def findAnagrams(userInput):
    targetWord = sorted(userInput)
    anagrams = []

    # print("wordlist: ", word_list)
    for word in word_list:
        if( sorted(word.lower()) == targetWord and word != userInput):
            anagrams.append(word)
    if(len(anagrams) == 0):
        print("Need a larger dictionary or choose a different word")
    else:
        print("Anagrams of {}: \n {}".format(userInput, anagrams))


def main():
    while(True):
        userInput = (input("Please enter a word: ") ).lower()
        if(userInput == 'exit'):
            break
        findAnagrams(userInput)

if __name__ == "__main__":
    main()