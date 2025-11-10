import string
from collections import Counter
def analyz():
    try:
        
        with open("speech.txt","r",encoding="utf-8") as fil:
            text = fil.read().lower().strip()
            count={}
            clean_text="".join(ch.lower()for ch in text if ch not in string.punctuation)
            data=clean_text.split()
            for i in data:
                count[i]=count.get(i,0)+1
            top_words=Counter(count).most_common(10)
        with open("summary.txt","w",encoding="utf-8") as summary:
            for word, freq in top_words:
                summary.write(f"{word}: {freq}\n")
        print("data loaded")

    except Exception as e:
        print(f"the error is{e}")
analyz()