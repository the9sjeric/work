from random import sample
password_list = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k',
                 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a',
                 '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                 '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=',
                 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
length = 8
password = "".join(sample(password_list, length)).replace(' ', '')
print(password)


