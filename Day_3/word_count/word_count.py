
def words(value):
    """
       this function Counts the occurrences or characters in a word
    """
    # separates the input into different characters
    
    value = value.strip().split()

    #initialize a dict words

    words = {}

    # a forloop that initializes a character and increments the count
    for word in value:
        try:
            word = int(word)
        except ValueError:
            pass
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
    return words
print(words('here i am i'))


