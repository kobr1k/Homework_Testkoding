def my_change(file_danux, coding_danux,file_result ,coding_result ) :
    with open(file_danux , 'r+' , encoding = coding_danux) as file :
        s1 = file.read()

    with open(file_result , 'w' , encoding = coding_result) as file :
        s2 = file.write(s1)
    print("работа завершина ")

def  main ():
   # file_danux = input("Введите имя файла данных ")
   # coding_danux = input("Введите кодировку файла данных ")#utf-8
    #file_result = input("Введите имя файла result ")
    #coding_result = input("Введите кодировку файла result ")#utf-16
    file_danux = "C:/python/Git/Homework_Testkoding/new_utf/text.txt"
    coding_danux = "utf-8"
    file_result = "C:/python/Git/Homework_Testkoding/new_utf/text_result.txt"
    coding_result = "utf-16"
    my_change(file_danux, coding_danux,file_result ,coding_result ) 

    
if __name__ == '__main__':
    main()


