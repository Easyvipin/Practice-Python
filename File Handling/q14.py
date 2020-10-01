# 14.Remove all the lines that start with character `I&#39; or ‘i’ in a file and write it
# to another file.

with open("dummy.txt","r+") as file:
    lines = file.readlines()
    with open("newfile.txt","r+") as file_2:
        writer = []
        for line in lines:
            if line[0].lower() != "i":
                writer.append(line)

        file_2.write(writer)
                 
