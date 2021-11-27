def my_change(file_where, encoding_where,file_what_result ,encoding_what ) :
    with open(file_where , 'r+' , buffering = -1 , encoding = encoding_where) as file :
        file_where = file.read()

    with open(file_what_result , 'w' , encoding = encoding_what) as file :
        file_what = file.write(file_where)
    print("работа завершина ")

def  main ():
    
    file_where = "C:/python/Git/Homework_Testkoding/new_utf/text.txt"
    encoding_where = "utf-8"
    file_what_result = "C:/python/Git/Homework_Testkoding/new_utf/text_result.txt"
    encoding_what = "utf-16"
    my_change(file_where, encoding_where,file_what_result ,encoding_what ) 

    
if __name__ == '__main__':
    main()


