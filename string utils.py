def reverse(s):
    return s[::-1]                                                  # Reverse the input string.

def count_vowels(s):
    vowels = "aeiouAEIOU"  
    sum=0
    for char in vowels:
        if char in s:
            sum+=1
    return sum 

def is_palindrome(s):
    def is_palindrome(s):
        s = s.lower()                                                   # Convert the string to lowercase
        s = s.replace(" ","")                                         # Remove spaces from the string
        reversed_s = ""
        for char in s:
            reversed_s = char + reversed_s                           # Reverse the string
        if s == reversed_s:
            return True 
        else:
            return False  



def capitalize_words(s):                                        # Capitalize the first letter and lowercase others for each word in the input string
    words = []  
    word_list = s.split()  
    for word in word_list:
        capitalized_word = word[0].upper() + word[1:].lower()
        words.append(capitalized_word)
    string = " ".join(words)                                     # Join elements in a list,tuple or any with strings into a string
    return string
    

def replace_substring(s, old, new):                           # Replace all occurrences of 'old' substring with 'new' substring.

    s = s.replace(old, new)
    return s                                   
def split_string(s, delimiter):
    split_string = s.split(delimiter)
    return  split_string            

def strip_string(s,char):                                      # Remove given characters from the input string
    stripped_string = s.strip(char)
    return stripped_string