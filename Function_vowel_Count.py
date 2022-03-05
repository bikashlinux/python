def vowel_count(string):
    vowels = 0
    vowel = set("aeiouAEIOU")
    for alphabet in str:
        if alphabet in vowel:
            vowels += 1
    print("No. of vowels :", vowels)


str = input("Enter a string \n")
vowel_count(str)
