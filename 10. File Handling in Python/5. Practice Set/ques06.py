# search for the line number in which the word 'python' is present in log_file.txt
content = True
bool_flag = False
i = 1
with open("log_file.txt", "r") as file:
    while (content):
        content = file.readline()
        if 'python' in content.lower():
            bool_flag = True
            print("Line Desc.:", content, end="")
            print(f"Yes Python is present in line No. {i}.")
            i += 1

if (bool_flag == False):
    print("No, Python was not present in the file.")