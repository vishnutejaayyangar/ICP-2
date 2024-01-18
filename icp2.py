
def Full_name(first_name="first name",last_name='last name'): # Here i have created Full name method by passing arguments first name and last name
    return first_name+' '+last_name  # Here i have concatinated both first name and last name which i have returned it as a string to the function

first_name=input("Enter your first name:/n")# Used input function to accept a string from the user and stored in a variable
last_name=input("Enter your last name:/n")
full_name=Full_name(first_name,last_name)#passed variables to the function
print(full_name)

def string_alternative(string):
    o=''
    for i in range(0,len(string)):#Here i am iterating the string from 0 to the lenght of the string
        if(i%2==0):#Here i am taking each character and doing modulus with and equating to 0 so that we can get the all the alternate characters in the string
            o=o+string[i]# Here i am adding empty string to the list of characters according the index so that we can return the string and then print it.
    return o
string_alternative('Good evening')#called the function by passing "Good Evening" as a string.

with open('input_file.txt','r') as ipf:#created a file named input_file and used read and split functions to read the file and split the words into several words as per the question
    line=ipf.read()
    word=line.split()
    with open('output_file.txt','w') as opf:
        for i in word: # Here i have iterated through word variable where the split of words are returned
            opf.write(i+':'+str(word.count(i))+'\n')
opf=open('output_file.txt','r')
print(opf.read())

# Nested interactive loop
heights=[]# Empty List

while True:
    x=float(input())
    if(x<=0):
        break
    heights.append(x)#this is in inches

output=[x*2.54 for x in heights]
print(output)#this is in cm
