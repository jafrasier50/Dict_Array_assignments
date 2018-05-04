while True:
    print("<<<|Palindrome Detector 9000|>>>")
    word = str(input("----Please Enter Word Here: "))

    def palindrom_detect():
        if word == word[::-1]:
            print("____Palindrome____")
        else:
            print("____Not a Palindrome____")
            return
    palindrom_detect()

    while True:
        command = str(input("---|Run Again? (y/n): "))
        if command in ("y","n"):
            break
        print("---|Invalid Input.")
    if command == "y":
        continue
    else:
        print("-------|| Goodbye ||-------")
        break


# vvvvvvv below was class example vvvvvvv
# word = input("Enter ya palindrome word homie: ")
# reversed_word =""
#
# print(len(word))
#
# for index in range(len(word)-1,-1,-1):
#     print(f"reversed_word = {reversed_word} and word[index] = {word[index]}")
#     reversed_word += word[index]
# if word == reversed_word:
#     print("PALINDROME SON")
# else:
#     print("WRONG FOOL!")
