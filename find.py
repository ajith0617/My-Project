sample = input("Please Enter the word: ").lower()
vowels = ['a','e','i','o']
list1 = []
for sam in sample:
    if sam in vowels:
        list1.append(sam)
print(f"Total Count of vowels is {len(list1)}")
