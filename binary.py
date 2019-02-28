def binary_to_decimal(number):
    len_number = len(number)
    sum_total = 0
    power = len_number -1
    for i in number:
        a = 2**(power) * int(i)
        sum_total += a
        power -=1
        print(a)
    return sum_total


def decimal_to_binary(number):

    number = int(number)
    output = ""
    while number > 0:
        if number % 2 == 0:
                value = 0
                number = number / 2
        else:
                value = 1
                number = number - number % 2
                number = number / 2
        output += str(value)
    output = output[::-1]

    return output

def main():
    user_input = input("Put number and system: ")
    user_input_list = user_input.split(" ")

    if user_input_list[1] == "2":
        output = binary_to_decimal(user_input_list[0])
        output_system = "10"

    elif user_input_list[1] == "10":
        output = decimal_to_binary(user_input_list[0])
        output_system = "2"
    
    print("{} {}".format(output, output_system))

if __name__ == "__main__":
    main()