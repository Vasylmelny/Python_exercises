# program is not finished!
program CheckDic(string):
    string = input("Enter a string: ")
    for i in string:
        for j in range(10):
            if i == j:
                print("String contains nubers")
                return True
                break
