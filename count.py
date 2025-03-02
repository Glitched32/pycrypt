def number_counter(Numbers):
    count = 0
    while Numbers != 0:
        Numbers = Numbers // 10
        count = count + 1
    return count
def letter_counter(letters):
    count = len(letters)
    return count
    