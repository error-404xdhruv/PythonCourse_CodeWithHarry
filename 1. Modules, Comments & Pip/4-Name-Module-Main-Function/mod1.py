def greet(name):
    print(f"Good Morning, {name}.")

if __name__ == "__main__":
    name = input("Enter a name: ")
    greet(name)

# yrr dekho if __name__ == "__main__": is line ka seedha sa mtlb hain ki agar main is the name then uske aage ka code execute kro nhi to nhi, jb apan koi module kahi use krte hain na to uska name badal jaata hain aur file k name pr rkha jaata hain