from datetime import datetime
def check():
    try:
        with open("text cleaner_sample.txt","r",encoding="utf-8") as sample_text:
            exe=["is", "the", "a", "of", "to"]
            clean=[]
            execlean=[]
            j=0
            for lines in sample_text:
                words=lines.split()
                for word in words:
                    word=word.lower()
                    if word not in exe:
                            clean.append(word)
                    else:
                            execlean.append(word)
                            j+=1
                            
        with open("text_cleaner.txt","w",encoding="utf-8") as clean_text:
            cleaned_text = " ".join(clean)
            clean_text.write(cleaned_text+"\n\n")
            unexee=" ".join(execlean)
            clean_text.write(unexee+"\n")
            print(f"Number of removed words: {j} and checked time is{datetime.now()}")


    except Exception as e:
        print(f"the error is {e}")
check()

