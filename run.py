import mypackage

#mathutils module
sum=mypackage.add(1,2)
print(sum)

sum=mypackage.subtract(1,2)
print(sum)

sum=mypackage.multiply(1,2)
print(sum)

sum=mypackage.divide(1,2)
print(sum)

sum=mypackage.power(1,2)
print(sum)

#datetimeutils module
date=mypackage.get_current_date()
print(date)

time=mypackage.get_current_time()
print(time)

datetime=mypackage.get_current_datetime()
print(datetime)

#stringutils module
count=mypackage.count_vowels("hello world")
print(count)

capital=mypackage.capitalize_words("hello world")
print(capital)

string=mypackage.is_palindrome("hello world")
print(string)

string=mypackage.reverse("hello world")
print(string)

string=mypackage.replace_substring("hello world", "hello", "hi")
print(string)

string=mypackage.split_string("hello world", " ")
print(string)

string=mypackage.strip_string("hello world", "h")
print(string)

#fileutils module

mypackage.write_file("hello.txt", "Happy New Year ")
file=mypackage.read_file("hello.txt")
print(file)                             

mypackage.append_to_file("hello.txt", "2025")
file=mypackage.read_file("hello.txt")
print(file)




