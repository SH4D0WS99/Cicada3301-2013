file1=open("gematria-primus.txt", "w")
file1.write("Artificial Intelligence is a method of learning new data.\n Artificial Intelligence covers three types of tasks:\n 1. Mundane Tasks\t 2. Formal Tasks\t 3. Expert Tasks")
file1=open("gematria-primus.txt", "r")
filename=input("Enter the filename: ")
with open(filename) as file:
    text=file.read()
    count_tab=0
    count_space=0
    count_newline=0
    for char in text:
        if char=='\t':
            count_tab+=1
        if char==' ':
            count_space+=1
        if char=='\n':
            count_newline+=1
print("How many Tabs are present in these file? ", count_tab)
print("How many Spaces are present in these file? ", count_space)
print("How many Newlines are present in these file? ", count_newline)