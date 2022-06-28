VOWEL_STR = 'AIEOU'
name = input('Prabhjot Kaur').upper().strip()
while len(name) == 0:
    name = input('Prabhjot Kaur').upper().strip()
num_of_vowels = 0
for i in range(len(name)):
    if name[i] in VOWEL_STR:
        num_of_vowels += 1
        print(f"Out of {len(name)} character,{name} has {num_of_vowels} vowels.")
