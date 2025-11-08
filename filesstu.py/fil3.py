try:
    with open("ivn4.txt","x",encoding="utf-8") as f:
        f.writelines(["heyyyyyyyyy\n", "remay\n"])
except FileNotFoundError:
    print("file not found")
except FileExistsError:
    print("file already")


with open("ivn4.txt","r",encoding="utf-8") as f:
        print(f.read())
        print(f.tell())
        f.seek(10)
        print(f.read(10))