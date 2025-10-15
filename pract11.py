#Write a python program to implement simple chatbot 



#Python Code:
print ("Simple Question and Answering Program")
print ("=================================")
print ("You may ask any one of these questions")
print ("Hi")
print ("How are you")
print ("Are you working?")
print ("What did you do yesterday?")
print ("What is your name?")
print ("Enter your name?")
print ("Quit")

while True:
    question = input("Enter one question from above list: ")
    question = question.lower()
    if question in ["hi"]:
        print ("Hello")
    elif question in ["how are you", "how do you do"]:
        print ("I am fine")
    elif question in ["are you working", "are you doing any job?"]:
        print ("Yes, I'm working in NASA")
    elif question in ["what is your name?"]:
        print ("My name is Mr. Stark")
    elif question in ["enter your name?"]:
        name = input("Enter your name? ")
    elif question in ["what did you do yesterday?"]:
        print ("I made my own Robots")
    elif question in ["quit"]:
        break
    else:
        print ("I don't understand what you said")