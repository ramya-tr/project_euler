import time

number_in_words_dict = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
    10: 'ten', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety',
    100: 'hundred', 1000: 'thousand'
}

def get_number_in_letters(num):
    end_with_zero_flag = 1 if num % 10 == 0 else 0

    if num in (100, 1000):
        return 'One' + " " + number_in_words_dict[num]

    if num in number_in_words_dict:
        return number_in_words_dict[num]

    number_in_words = ''
    and_ = ''
    original_number = num

    while num > 0:
        if num in number_in_words_dict:
            number_in_words += and_ + number_in_words_dict[num]
            break

        len_of_number = len(str(num))
        lowest_tens = pow(10, (len_of_number-1))

        quotient = num // lowest_tens
        reminder = num % lowest_tens

        if quotient == 0:
            if reminder == 0:
                break

            num = reminder
            continue

        if len_of_number == 2:
            number_in_words += and_ + number_in_words_dict[quotient *  lowest_tens] + " " + number_in_words_dict[reminder]
            break

        else:
            number_in_words += and_ + number_in_words_dict[quotient] + " " + number_in_words_dict[lowest_tens]

        and_ = ' and '
        num = reminder

    number_in_words_dict[original_number] = number_in_words

    return  number_in_words


def number_letter_counts():
    max_num = 1000
    length_ = 0

    for i in range (1, max_num + 1):
        # print(get_number_in_letters(i) , "  ", len(get_number_in_letters(i).replace(' ', '')))
        length_ += len(get_number_in_letters(i).replace(' ', ''))

    print(length_)


start_time = time.time()
number_letter_counts()
print("--- %s seconds ---" % (time.time() - start_time))
