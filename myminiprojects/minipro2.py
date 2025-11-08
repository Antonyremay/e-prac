def val():
    try:
        filename = input("enter the filename: ")
        word = input("enter the word to search: ")
        tot = 0
        with open(filename, "r") as f:
            for line in f:
                tot += line.split().count(word)
        print(f"The word '{word}' appears {tot} times in the file")
    except FileNotFoundError:
        print(f"The file {filename} doesn't exist")
    except Exception as e:
        print(f"Error: {str(e)}")

val()
