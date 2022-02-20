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


def typing_time(start_time, stop_time):
    """ all time using in typing example sentence """
    using_time = stop_time - start_time
    return using_time


def typing_speed(word, times):
    """ calculate word per minute """
    num_word = len(word.split())
    minute_time = times/60
    speed = num_word/minute_time
    speed = round(speed, 2)
    return speed


# ------------------------------------- Terminal test -------------------------------------

example_sentence = "This is typing speed test program"
print("Type this:- '", example_sentence, "'")

# listening to input ENTER to start count time
input("press ENTER when you are ready!")

# recording time for input
stime = time()
user_input = input()
etime = time()

# gather all the information returned from functions
error = typing_error(example=example_sentence, user=user_input)
speed = typing_speed(word=example_sentence, times=typing_time(stime, etime))
time = typing_time(stime, etime)

# printing all the required data
print("Total Time elapsed : ", time, "s")
print("Your Average Typing Speed was : ", speed, "words / minute")
print("With a total of : ", error, "errors")



