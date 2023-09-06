#Remove all the lines that contain the character `a' in a file and write it to another file.
with open("test1.txt","r") as f:
 lines = f.readlines() #saved lines
 print("Original file is :")
 print(lines)
with open("test3.txt","w") as e:
 f=open("test1.txt","w") # file containing lines without 'a'
 for line in lines:
  if 'a' in line or 'A' in line:
   e.write(line)
  else:        
   f.write(line)

f.close()   

with open("test1.txt","r") as f:
 lines=f.readlines()

 with open("test3.txt","r") as e:
  lines1=e.readlines()

  print("\n")

  print("Files without letter a:")
  print(lines)
  print("\n")

  print("Files with letter a:")
  print(lines1)
