final_list=[]
with open("names.txt","r") as f:
    for line in f:
        splitted  = line.strip()
        result = splitted.split(" ")

        final_list.extend(result)

print(final_list)