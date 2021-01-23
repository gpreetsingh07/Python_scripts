cars = ["Alto","Swift","Zen","Brezza"]
with open("/Users/gps/IdeaProjects/Python_scripts/writeme.txt",'w') as writef:
    for i in cars:
        writef.write(i)
        writef.write("\n")
print("File updated")