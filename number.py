from tkinter import *

top_window = Tk()
top_window.title("Number Conversion")
#top_window.geometry("1000x1000")

top_window['background']= "#05786F"

bases = [
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31",
    "32",
    "33",
    "34",
    "35",
    "36"
]

list_1 = StringVar(top_window)
list_1.set(bases[8])
list_2 = StringVar(top_window)
list_2.set(bases[0])

option_1 = OptionMenu(top_window, list_1, *bases).grid(column = 0, row = 0)
option_2 = OptionMenu(top_window, list_2, *bases).grid(column = 2, row = 0)

user = Text(top_window, height = 1, width = 35)
user.grid(column = 0, row = 1)
show = Text(top_window, height = 1, width = 35)
show.grid(column = 2, row = 1)
show['state'] = 'disabled'

input = Label(top_window, text = "Input").grid(column = 0, row = 2)
output = Label(top_window, text = "Output").grid(column = 2, row = 2)


def base1_to_base2():

    show['state'] = 'normal'
    show.delete("1.0", "end")
    ans = ""

    given_input = user.get("1.0", "end")
    given_input = given_input[:len(given_input) - 1]



    char_to_value = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
        "G": 16,
        "H": 17,
        "I": 18,
        "J": 19,
        "K": 20,
        "L": 21,
        "M": 22,
        "N": 23,
        "O": 24,
        "P": 25,
        "Q": 26,
        "R": 27,
        "S": 28,
        "T": 29,
        "U": 30,
        "V": 31,
        "W": 32,
        "Y": 34,
        "Z": 35,
    }

    value_to_char = {}
    for key, value in char_to_value.items() :
        value_to_char[value] = key

    num = 0
    base_from = int(list_1.get())
    base_to = int(list_2.get())


    for item in given_input:
    
        if item not in char_to_value.keys() :
            ans = "Invalid character for this code"
            show.insert("1.0", ans)
            show['state'] = 'disabled'
            return
        
        else :
            
            value = char_to_value[item]
            if value >= base_from :
                ans = "Invalid character for base " + str(base_from)
                show.insert("1.0", ans)
                show['state'] = 'disabled'
                return
        
        value = char_to_value[item]
        num  = num * base_from
        num = num + value

    
    if num == 0 :

        ans = "0"
        show.insert("1.0", ans[: : -1])
        show['state'] = 'disabled'

    else :

        ans = ""
        while num != 0 :
            ans = ans + value_to_char[(num % base_to)]
            num = num // base_to

        show.insert("1.0", ans[: : -1])
        show['state'] = 'disabled'
        


convert = Button(top_window, text = "Convert", command = base1_to_base2).grid(column = 1, row = 2)


top_window.mainloop()
