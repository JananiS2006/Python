a="me"
b="myself"
c=a+b #"memyself"
d=a+" "+b #"me myself"
silly=a*3 #"mememe"
#YOU TRY
b=":"
c=")"
s1=b+2c #":))"
f="a"
g1="b"
s2=(f+g)*int(h) #"ababab"
# length of the string
len(s2)
len(s1)
#String slicing
s="abcdefgh"
s[3:6] #def
s[3:6:2] #df
s[:] #abcdefgh
s[::-1] #hgfedcba
s[4:1:-2] #ec

s ='ABC d3f ghi'
[3:len(s)-1])
(s[4:0:-1])
(s[6::3])
#Printing
a = "the"
b = 3
c = "musketeer"
print(a, b, c)  #the 3 musketeer

print(a + str(b) + c)  #the3musketeer

# Input
text = input("Type anything: ")  #Type anything: howdy
print(5 * text)  # howdyhowdyhowdyhowdyhowdy

# input as int
num1 = int(input("Type a number: "))  #Type a number: 3
print(5 * num1)  # Output: 33333

num2 = int(input("Type a number: "))  #Type a number: 5
print(5 * num2)  #15
#You try
question = input('Choose a verb ')  # Choose a verb:run
print('I can', question, 'better than you!')  #I can run better than you!
print(question * 5)  #runrunrun

#You try
secret_number = 3
guess = int(input("What is your guess: "))
if secret_number > guess:
    print("Your guess is low")
elif secret_number == guess:
    print('Your guess is correct')
elif secret_number < guess:
    print("Your guess is high")