from agent import train, eval

print("Hello Mustafa Ghoneim Snake Agent")
op = input("Do you want to train or to eval? (1. train - 2. evaluate): ")

c = 0
while int(op) != 1 and int(op) != 2:
    print(int(op))

    if c == 5:
        exit()
    op = input("WRONG INPUT!!\nDo you want to train or to eval? (1. train - 2. evaluate): " if c < 3 else "anta zah2tny 3lafekra!!\nDo you want to train or to eval? (1. train - 2. evaluate): " if  c < 4 else "kfaya keda 25er mara!!\nDo you want to train or to eval? (1. train - 2. evaluate): ")
    c += 1
filename = input("Please enter the save/load model filename. enter 0 for default:'model.pth': ")
if int(op) == 1:
    if filename == "" or filename == " " or filename == "0" or filename is None:
        train()
    else:
        train(filename)
elif int(op) == 2:
    if filename == "" or filename == " " or filename == "0" or filename is None:
        eval()
    else:
        eval(filename)