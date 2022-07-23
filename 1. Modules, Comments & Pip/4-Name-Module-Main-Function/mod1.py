def greet(name):
    print(f"Good Morning, {name}.")

if __name__ == "__main__":
    name = input("Enter a name: ")
    greet(name)

# yrr dekho if __name__ == "__main__": is line ka seedha sa mtlb hain ki agar main is the name then uske aage ka code execute kro nhi to nhi, jb apan koi module kahi use krte hain na to uska name badal jaata hain aur file k name pr rkha jaata hain

# __name__ evaluates to the name of the module in Python from where the program is ran. If the module is being run directly from the command line then the __name__ is set to string __main__. Thus this behaviour is used to check whether the module is run directly or imported to another file.