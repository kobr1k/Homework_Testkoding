my_list = ["самолёт", "машина", "поезд","автобус"]
language = "ru" 
my_strings = {}
my_strings["введите  0 , 1 "] = "нажмите 0 чтобы выйти или нажмите 1 чтобы сыграть ещё раз "
#my_strings["введите букву"] = "enter a letter  " 
my_strings["введите букву "] = "введите букву  " 
my_strings["вы проиграли "] = "вы проиграли "
my_strings["оставшихся ошибок "] = "оставшихся ошибок "
my_strings["вы выиграли "] = "вы выиграли "
def set_language (lang):
    global my_strings
    global language
    global my_list 
    language = lang
    if lang == "en":
        my_strings["введите  0 , 1 "] = "press 0 to exit or  1 to play game "
        my_strings["введите букву "] = "enter a letter  "  
        my_strings["вы проиграли "] = "you loos "
        my_strings["оставшихся ошибок "] = "erors left "
        my_strings["вы выиграли "] = "you win "
        my_list = ["plain", "car", "trein", "bus"]
    if lang == "ua":
        my_strings["введите  0 , 1 "] = "натисніть 0 щоб вийти чи 1 щоб грати ще раз "
        my_strings["введите букву "] = "введіть літеру  "  
        my_strings["вы проиграли "] = "ви програли "
        my_strings["оставшихся ошибок "] = "залишилося помилок "
        my_strings["вы выиграли "] = "ви виграли "
        my_list = ["літак", "машина", "потяг"]
      

