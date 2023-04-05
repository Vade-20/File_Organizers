import os,shutil,send2trash

def make_dir():
    path = os.getcwd()
    print("Current working directory is :",path)
    ch = input("Do you want to change it (Y/N):")
    if ch.lower().startswith('y'):
        path = os.path.join(input("Enter the folder absolute path:").strip('"'))
        while not os.path.isabs(path):
            path = os.path.join(input("Enter the folder absolute path:").strip('"'))
        os.chdir(path)
    all_files = os.listdir(path)  
    if 'Organized_folder'  in all_files:
        send2trash.send2trash('Organized_folder')
        os.makedirs('Organized_folder')
    else:
        os.makedirs('Organized_folder')
    sum_file = 0
    biggest_file = 0
    for i in all_files:
        sum_file += (os.path.getsize(i))/(1000000)
        if (os.path.getsize(i))/(1000000) > biggest_file:
            biggest_file = (os.path.getsize(i))/(1000000)
    biggest_file1 = biggest_file
    if round(sum_file/len(all_files),2)!=0.0:
        avg = round(sum_file/len(all_files),2)
    else:
        avg = sum_file/len(all_files)

    os.makedirs(f'Organized_folder\\{round(biggest_file,2)}MB-{round(biggest_file-avg/2,2)}MB')
    os.makedirs(f'Organized_folder\\{round((biggest_file-avg)/2,2)}MB-{round(avg,2)}MB')
    os.makedirs(f'Organized_folder\\{round(avg,2)}MB-{round((avg)/2,2)}MB')
    os.makedirs(f'Organized_folder\\{round(avg/2,2)}MB-{0}MB')
    move_file(biggest_file1,avg,all_files)

    
    
def move_file(biggest_file,avg,all_files):
    for i in all_files:
        size = (os.path.getsize(i))/(1000000)
        try:
            if 0<=size<=avg/2:
                shutil.copy(i,f'Organized_folder\\{round(avg/2,2)}MB-{0}MB')
            elif avg/2<size<=avg:
                shutil.copy(i,f'Organized_folder\\{round(avg,2)}MB-{round((avg)/2,2)}MB')
            elif avg<size<=(biggest_file-avg)/2:
                shutil.copy(i,f'Organized_folder\\{round((biggest_file-avg)/2,2)}MB-{round(avg,2)}MB')
            elif (biggest_file-avg)/2<size<=biggest_file:
                shutil.copy(i,f'Organized_folder\\{round(biggest_file,2)}MB-{round(biggest_file-avg/2,2)}MB')
        except:
            continue
make_dir()

