import shutil,os,send2trash
path = os.getcwd()
print("Current working directory is :",path)
ch = input("Do you want to change it (Y/N):")
if ch.lower().startswith('y'):
    path = os.path.join(input("Enter the folder absolute path:").strip('"'))
    while not os.path.isabs(path):
        path = os.path.join(input("Enter the folder absolute path:").strip('"'))
    os.chdir(path)

if os.path.isdir("All_the_files"):
    send2trash.send2trash("All_the_files")
    os.makedirs('All_the_files')
else:
    os.makedirs("All_the_files")
    
paths = os.getcwd()+os.path.join('\\All_the_files')
for root,subfolder,files in os.walk(os.getcwd()):
    p = os.chdir(root)
    for i in files:
            try:
                shutil.copy(i,paths)
            except:
                 continue
