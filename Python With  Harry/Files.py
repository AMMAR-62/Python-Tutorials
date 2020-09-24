# File I/O Basics
# Two types of Memories 
# HardDisk and RAM
# "r" - Open File for Reading
# "w" - Open File in Write Mode
# "x" - Exclusive Creation
# "a" - Add more Content to a file
# "t" - Text Mode
# "b" - Binary Mode
# "+" - Read and Write
# Question of the day


    # # -------Reading and Writing a File ----------
    # f = open("Ammar.txt","r") 
    # for i in range(1,10):
    #     f.write("I am Ammar I am Awesome\n")
    # f.close()
    # f = open("Ammar.txt")
    # content = f.read() 
    # print(content)
    # f.close()


# ------Append and Write --------
    # f= open("Ammar.txt","a")
    # for i in range(5):
    #     a= f.write("\nTu Bhai Phodke rahega")
    # f.close()

# ----------Handle read and write ---------
        # f = open("Ammar.txt","r+")
        # print(f.read())
        # f.write("Thank  You")

# -------- F.tell(), f.seek()----------
        # f = open("Ammar.txt")
        # print(f.readline())
        # # print(f.tell())
        # f.seek(10)
        # print(f.readline())
        # # print(f.tell())
        # f.seek(10)
        # print(f.readline())
        # # print(f.tell())
        # f.seek(10)
        # f.close()
with open("Ammar.txt") as f:
    a = f.read(4)
    print(a)


