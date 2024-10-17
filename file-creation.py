import os
if os.path.exists("file.sh"):
  print("File is exist")
else:
  file=open("file.sh", "x")
  print("new file created")

exit()



#write = input("You want to append the file type 'Yes'",)
