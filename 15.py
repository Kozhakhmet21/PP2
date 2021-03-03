import os
def show_file_and_dirs(dir_path:str):
    with os.scandir(dir_path) as a:
        for x in a:
            if x.is_file():
                print(x)

show_file_and_dirs('/Users/kozhahmet/PP 2/Week 6')