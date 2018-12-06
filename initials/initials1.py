def get_initials(fullname):
    init = ""
    name_list = fullname.upper()
    name_list = name_list.split()  
    
    for name in name_list:
        init = init + name[0]
    return init

def main():
    fullname = input ("What is your name?")
        get_initials(fullname)
    print ("init")
    
if __name__ == "__main__":
    main()
    """ Given a person's name, returns the person's initials (uppercase) """
    # TODO your code here