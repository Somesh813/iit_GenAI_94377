sentence=input("Please enter a sentence: ")
number_of_characters=len(sentence)
print("Number of characters=",number_of_characters)

words=sentence.split()
num_words=len(words)
print("Number of words:",num_words)  

vowels="aeiouAEIOU"
num_vowels=0
for char in sentence:
    if char in vowels:
        num_vowels+=1  
print("Number of vowels:",num_vowels)