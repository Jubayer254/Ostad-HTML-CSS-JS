# If Else 
marks = 80
result = ''


if marks < 33:
    result = "Failed"
elif marks >= 80:
    result = "A+"
else:
    result = "Passed"

print(result)

# Match 
vowel = 'x'

match vowel:
    case 'a' : print("It is a Vowel")
    case 'e' : print("It is a Vowel")
    case 'i' : print("It is a Vowel")
    case 'o' : print("It is a Vowel")
    case 'u' : print("It is a Vowel")
    case _: print("It is a Consonant")

# Loop 
i = 1
while(i<=3):
    print(i)
    i += 1

words = ["One", "Two", "Three", "Four"]

for x in words:
    print (x)

x = words[0]
print(x)
