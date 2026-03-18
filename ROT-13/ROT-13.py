string = input("Enter the text to encode: ")
n = 13

upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
output=""

lst=list(string)
for i in range(len(string)):
    letter=lst[i]
    if letter in upper:
        uindex=(upper.index(letter)+n)%26
        output+=upper[uindex]
    elif letter in lower:
        lindex=(lower.index(letter)+n)%26
        output+=lower[lindex]
    else:
        output+=letter
print(output)