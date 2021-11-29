import os
os.chdir("C:/python/Git/Homework_Testkoding/new_utf")
from typing import Text
bufer_size = 1024 * 1024 * 8 
def my_change(file_where, encoding_where,file_what_result ,encoding_what ) :
    with open(file_where , 'r' , buffering = 2 , encoding = encoding_where) as file :
        file_where = file.read(bufer_size)

    with open(file_what_result , 'w' , encoding = encoding_what) as file :
        file_what = file.write(file_where)
    print("работа завершина ")

def  main ():
    
    file_where = input("введите изночальный файл  ")#"text.txt"
    # file_where ="C:\python\Git\Homework_Testkoding\new_utf\text.txt"
    encoding_where =input("введите изначальную кодировку ")
    file_what_result = input("введите название  конечного файла ") #text_result.txt
    #file_what_result = "C:/python/Git/Homework_Testkoding/new_utf/text_result.txt"
    encoding_what = input("введите конечную кодировку ")
    my_change(file_where, encoding_where,file_what_result ,encoding_what ) 

    
if __name__ == '__main__':
    main()


