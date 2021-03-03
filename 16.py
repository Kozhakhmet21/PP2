import os
def show_file_and_dirs(dir_path:str): #Myna jerde str bolyp tur sebeby, biz outputta '/Users/kozhahmet/PP 2/Week 6' osylai stroka retynde bolgan son, adeiy solai jazylgan.
    with os.scandir(dir_path) as a:
        for x in a:
            if x.is_dir():
                print(x)

show_file_and_dirs('/Users/kozhahmet/PP 2/Week 6')