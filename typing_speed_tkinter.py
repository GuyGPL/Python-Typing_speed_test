from tkinter import *
from tkinter import messagebox
from time import time


def typing_error(example, user):
    """ error count letter by letter (but if user missing word in example it will cause Index error) """
    e_word = example.split()
    u_word = user.split()
    errors = 0

    for i in range(len(e_word)):
        # word match
        if e_word[i] == u_word[i]:
            continue
        # not match check how many letter
        else:
            e_list = list(e_word[i])
            u_list = list(u_word[i])
            print(e_list)
            print(u_list)
        # check how many letter mismatch if user type equal or more than example
            if len(u_list) >= len(e_list):
                for index in range(len(u_list)):
                    try:
                        if e_list[index] == u_list[index]:
                            continue
                        else:
                            errors += 1
                    except IndexError:
                        errors += 1
        # check how many missing letter if user type less than example and count as error
            elif len(u_list) < len(e_list):
                for index2 in range(len(e_list)):
                    try:
                        if e_list[index2] == u_list[index2]:
                            continue
                        else:
                            errors += 1
                    except IndexError:
                        errors += 1

    # print(f'This is example: {e_word}')
    # print(f'This is user input: {u_word}')
    # print(f'This user error: {errors}')
    return errors


def typing_time(start_time):
    """ all time using in typing example sentence """
    using_time = time() - start_time
    return using_time


def typing_speed(word, times):
    """ calculate word per minute """
    num_word = len(word.split())
    minute_time = times/60
    speed = num_word/minute_time
    speed = round(speed, 2)
    return speed


def typing_test(sentence_user, start_time):
    """ make it easy for call all 3 functions above in Tkinter by mixing those 3 functions"""
    error = typing_error(example=example_sentence, user=sentence_user)
    time = typing_time(start_time=start_time)
    speed = typing_speed(word=example_sentence, times=time)
    messagebox.showinfo(title="Results", message=f"Total Time elapsed : {time} s \nYour Average Typing Speed was : {speed} words / minute\nWith a total of : {error} errors")


def time_count():
    """ make entry state back to normal (user can type) and start counting time """
    global time_counting
    user_entry.config(state="normal")
    time_counting = time()

# ------------------------------------- Terminal test -------------------------------------

# example_sentence = "This is typing speed test program"
# print("Type this:- '", example_sentence, "'")
#
# # listening to input ENTER to start count time
# input("press ENTER when you are ready!")
#
# # recording time for input
# stime = time()
# user_input = input()
# etime = time()
#
# # gather all the information returned from functions
# error = typing_error(example=example_sentence, user=user_input)
# speed = typing_speed(word=example_sentence, times=typing_time(stime, etime))
# time = typing_time(stime, etime)
#
# # printing all the required data
# print("Total Time elapsed : ", time, "s")
# print("Your Average Typing Speed was : ", speed, "words / minute")
# print("With a total of : ", error, "errors")

# ------------------------------------- GUI part -------------------------------------
time_counting = None
example_sentence = "This is typing speed test program"

root = Tk()
root.title("Typing Speed Test")
root.geometry("1080x540")
root.configure(bg='#74959A')

type_this_label = Label(text=" Type this sentence:", font=("Courier", 24, "bold"), background="#98B4AA", fg="white")
type_this_label.grid(column=1, row=1, padx=50, pady=30,)

example_label = Label(text=f'"{example_sentence}"', font=("Courier", 24, "bold"), background="#98B4AA", fg="white")
example_label.grid(column=1, row=2, padx=30, pady=0,)

user_entry = Entry(font=("Courier", 24, "bold"), width=53, state="disabled")
user_entry.grid(column=1, row=3, padx=30, pady=40)

start_button = Button(text="Start", font=("Courier", 24, "bold"), background="#495371", fg="white", width=10, command=time_count)
start_button.grid(column=1, row=4)

submit_button = Button(text="Submit", font=("Courier", 24, "bold"), background="#495371", fg="white", width=10, command=lambda: typing_test(sentence_user=user_entry.get(), start_time=time_counting))
submit_button.grid(column=1, row=5, padx=30, pady=5)



root.mainloop()