import time
from  random import choice
from difflib import SequenceMatcher
sentence = [
            "Python is a powerful programing language" ,
            "Python is a Easiest Language in the world"  ,
            "Python is a Popular Language",
            "Python was release in 1991"
            ]

highest_wpm = 0
highest_accuracy = 0 

while True:     
    selected_sentence = choice(sentence)
    print(selected_sentence)

    text = "3...\n2...\n1...\nStart!\n"
    for i in text:
        print(i,end="", flush= True)
        time.sleep(0.1)
    start_time = time.time()
    
    typed_words = input("\nEnter Sentence here : ")
    print("")

    end_time = time.time()
    total_time = end_time - start_time

    words = len(typed_words.split())


    if not typed_words.strip():
        print("Please write something")
        continue
    WPM = words / (total_time / 60)

    accuracy = SequenceMatcher(None, selected_sentence, typed_words ).ratio()*100


    if accuracy >=95 :
        print("Well done! All perfect \n")
    elif accuracy>= 90 : 
        print("Excellent!")
    elif accuracy >= 85 :
        print("Good ! but you need mor practice")

    else: 
        print("Need more practice\n")
    
    if WPM > highest_wpm:
        highest_wpm = WPM

    if accuracy > highest_accuracy :
        highest_accuracy = accuracy

    print(f"Accuracy : {accuracy:.0f}%\n")

    print(f"Time Taken: {total_time:.0f} Seconds\n")

    print(f"Words Written : {words}\n")

    print(f"Speed : { WPM :.0f} WPM\n")


    again = input("Do you want to continue(yes or NO) :")
    if again.lower() == "no" : 
        print(f"Highest WPM : {highest_wpm:.0f}\n")  
        print(f"Highest Accuracy : {highest_accuracy:.0f}\n")
        break
    else:
        continue