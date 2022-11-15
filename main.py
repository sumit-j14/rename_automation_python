import os
if __name__ == '__main__':
    # changing current working directory to where files are present
    print(os.chdir("/home/sumit/Desktop/automate_test"))
    # print(os.getcwd())
    for file in os.listdir():
        old_path = os.path.join(os.getcwd(), file)
        new_path = os.path.join(os.getcwd(), (file[2]+"_"+file[0]+'.txt'))
        # print(new_path)
        # print(old_path)
        os.rename(old_path, new_path)
