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
