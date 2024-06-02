import win32com.client

print("HI, MYSELF SPEAKING ROBO, I WILL HELP YOU !")
print("USING ME IS PREETY EASY")

speaker = win32com.client.Dispatch("SAPI.SpVoice")

while True:
    choice_1 = input("ENTER 1. TO START AND 2.QUIT[1,2]")
    if choice_1 == "1":
        choice_2 = input("ENTER WHAT YOU WANT TO SPEAK!")
        speaker.Speak(choice_2)
    else:
      print("THANKYOU FOR VISITING")