def is_palindrome(string):
    original_string=string.lower()
    new_string=''
    for i in original_string:
        if ord(i)>=97 and ord(i)<=122:
            new_string+=i 
    mirror_string=new_string[::-1]
    return new_string==mirror_string

print(is_palindrome('Madam'))
print(is_palindrome('Hello World'))
print(is_palindrome('Go hang a salami, I\'m a lasagna hog.'))