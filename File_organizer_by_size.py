import os,shutil,send2trash

def make_dir():
    all_files = os.listdir(os.getcwd())
    if not os.path.isfile(os.path.basename(__file__)):
        raise Exception("Please make sure the terminal set in current working directory")    
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

    os.makedirs(f'Organized_folder\\{biggest_file}MB-{(biggest_file-avg)/2}MB')
    os.makedirs(f'Organized_folder\\{(biggest_file-avg)/2}MB-{avg}MB')
    os.makedirs(f'Organized_folder\\{avg}MB-{(avg)/2}MB')
    os.makedirs(f'Organized_folder\\{avg/2}MB-{0}MB')
    move_file(biggest_file1,avg,all_files)

    
    
def move_file(biggest_file,avg,all_files):
    for i in all_files:
        size = (os.path.getsize(i))/(1000000)
        try:
            if 0<size<avg/2:
                shutil.copy(i,f'Organized_folder\\{avg/2}MB-{0}MB')
            elif avg/2<size<avg:
                shutil.copy(i,f'Organized_folder\\{avg}MB-{(avg)/2}MB')
            elif avg<size<(biggest_file-avg)/2:
                shutil.copy(i,f'Organized_folder\\{(biggest_file-avg)/2}MB-{avg}MB')
            elif (biggest_file-avg)/2<size<biggest_file:
                shutil.copy(i,f'Organized_folder\\{biggest_file}MB-{(biggest_file-avg)/2}MB')
        except:
            continue
make_dir()

