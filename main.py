# Task nr.2:
# Create a program , which takes 3 differnt sentences(ne maziau). The input should have all 
# error checking in mind. The program then should create a dictionary of whith key values 
# corresponding to words `long` (more than 9 letters in a words) `medium`(7 letters)
# `short` (5 words)(Short < 35% , medium: 25% , long 10%). Then the pgrogram should create a new sentences (if 3 provided, 3 new sentences should be returned) 
# with following rules attached:
# All sentences should have same (or less) words amount as entered one;
# The most frequent letter from the sentence (from input) should be dominated in a new sentence as well.

# The program should return new sentences with statitstics of ratio how many words was used from all sections 
# (as for exmpale: long 25%,medium 45%, short 30%)

def three_sentences_input_into_dict():
    word_dict = {"long":[], "medium": [], "short": []}
    three_sentences_string = input("Please enter three sentences: ")
    words_string = three_sentences_string.lower().replace(",", "").replace(".", "")
    three_sentences_with_no_dots = words_string.split(" ")
    for word in three_sentences_with_no_dots:
        if len(word) < 6:
            word_dict["short"].append(word)
        elif 5 < len(word) < 8:
            word_dict["medium"].append(word)
        else:
            word_dict["long"].append(word)
        return word_dict
print(three_sentences_input())


# There is no play with fiiiiiire. Stop talking and open your book. You always want to play games or get attention from me while I’m studying or busy at work.
