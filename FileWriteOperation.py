list_names=["Aarav Sharma", "Priya Nair", "Rohan Mehta"]
with open("new_names.txt","w") as f:
    for name in list_names:
        f.write(name + "\n")

with open("new_names.txt","a") as f:
    f.write("Hello")