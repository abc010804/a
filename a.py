
# 喜乐 4.14 3.59

file = open ("new_file.txt" , "w")
file.write(input("Please enter the txt:\n\n"))
file.close()

with open("new_file.txt") as f:
    text = f.read()
    
with open("new_file.txt") as b:
    text_two = b.read()
    
a = str(input("\nPlease enter characters:\n\n"))

def count_char(text,char):
    count = 0
    for i in text:
        if i == char:
            count += 1
    return count

for i in a:
    pear = 100*count_char(text_two,a) / len(text)

print("\n" + " In txt all characters: " + str(len(text))  + "个") 
    
print ("“" + a + "”" + " in the txt appear: " + str(count_char(text,a)) + "次") 

print ("“{0}” In the txt Proportion: {1}%".format(a,round(pear,2)))

