def main():
    plate = input("plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")



def is_valid(s):
    if 6 >= len(s) >= 2 and s[0:2].isalpha() and s.isalnum():
        if s.isalpha():
            return True
        for char in s:
            if char.isdigit():
                index = s.index(char)
                if s[index:].isdigit() and int(char)!=0:
                    return True
                else:
                    return False
                return False




main()










