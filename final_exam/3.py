openFile = input('Please input file name: ')
openFile = open(openFile)
numberOfVowels = 0
nuberOfConsonants = 0
vowels = ('a','e','i','o','u','A','E','I','O','U')

consonants =('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z')
lines = openFile.readlines()
for line in lines:
    for word in line:
        if word in vowels:
            numberOfVowels += 1
        if word in consonants:
            nuberOfConsonants += 1
