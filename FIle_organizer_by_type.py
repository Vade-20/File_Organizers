import os,shutil,send2trash

def make_dir():
    all_files = os.listdir(os.getcwd())
    types_set = set()
    if not os.path.isfile(os.path.basename(__file__)):
        raise Exception("Please make sure the terminal set in current working directory")    
    if 'Organized_folder'  in all_files:
        send2trash.send2trash('Organized_folder')
        os.makedirs('Organized_folder')
    else:
        os.makedirs('Organized_folder')

    for i in all_files:
        type = os.path.splitext(i)[1][1:]
        types_set.add(type)
    for i in types_set:
        if i !='':
            path = os.getcwd()+f'\\Organized_folder\\{i}'
            os.makedirs(path)
    
def move_file():
    all_files = os.listdir(os.getcwd())
    for i in all_files:
        if i != 'Organized_folder':
            shutil.copy(i,f'Organized_folder\\{os.path.splitext(i)[1][1:]}')


 

make_dir()
move_file()