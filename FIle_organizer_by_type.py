import os,shutil,send2trash

def make_dir():
    path = os.getcwd()
    print("Current directory is:",path)
    ch = input("Do you want to change it (Y/N):")
    if ch.lower().startswith('y'):
        path = os.path.join(input("Enter the folder absolute path:").strip('"'))
        while not os.path.isabs(path):
            path = os.path.join(input("Enter the folder absolute path:").strip('"'))
        os.chdir(path)
    all_files = os.listdir(path)
    types_set = set()
    if 'Organized_folder__'  in all_files:
        send2trash.send2trash('Organized_folder__')
        os.makedirs('Organized_folder__')
    else:
        os.makedirs('Organized_folder__')

    for i in all_files:
        type = os.path.splitext(i)[1][1:]
        types_set.add(type)
    for i in types_set:
        if i !='':
            paths = path+f'\\Organized_folder__\\{i}'
            os.makedirs(paths)
    move_file(path)
    
def move_file(path):
    all_files = os.listdir(path)
    for i in all_files:
        if i != 'Organized_folder__':
            try:
                shutil.copy(i,f'Organized_folder__\\{os.path.splitext(i)[1][1:]}')
            except:
                continue


 

make_dir()
