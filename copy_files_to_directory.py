import shutil,os
if not os.path.isfile(os.path.basename(__file__)):
    raise Exception("Please change the directory in the terimanl to the one where the file is")

if os.path.isdir("All_the_files"):
    shutil.rmtree("All_the_files")
    os.makedirs('All_the_files')
else:
    os.makedirs("All_the_files")
    
path = os.getcwd()+os.path.join('\\All_the_files')
for root,subfolder,files in os.walk(os.getcwd()):
    p = os.chdir(root)
    for i in files:
            try:
                shutil.copy(i,path)
            except:
                 continue
