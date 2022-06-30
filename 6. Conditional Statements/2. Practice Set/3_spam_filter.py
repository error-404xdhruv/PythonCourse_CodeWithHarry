spam1 = "buy now"
spam2 = "make a lot of money"
spam3 = "subscribe now"
spam4 = "click this"

comment = input()
if (spam1 in comment or spam2 in comment or spam3 in comment or spam4 in comment):
    print("Spam")
else:
    print("Ok Checked !")