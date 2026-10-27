def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
            
    return count
message = input("enter any text massage")
print(count_vowels(message))  

