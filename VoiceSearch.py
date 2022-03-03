#Voice Google Search
import speech_recognition as spr
import webbrowser as web

if __name__ =="__main__":

    #path_engine = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe %s"
    #C:\Users\Acer\AppData\Local\Google\Chrome\Application\chrome.exe

    #ff_path = web.get("C:\Users\Acer\AppData\Local\Google\Chrome\Application\chrome.exe")
    #ff = web.get(ff_path)
    #web.register('Google_Chrome',None, ff)

    r = spr.Recognizer()
    with spr.Microphone() as scr2:
        print("Wait for initialization")
        r.adjust_for_ambient_noise(scr2,duration=2)
        print("You May speak now")

        audio = r.listen(scr2)

        print("Recognizing now!")

        try:
            destination = r.recognize_google(audio)
            print("Did you mean go to : ",destination)
            path_url = "https://www.google.com/search?q=" + destination
            web.open_new_tab(path_url)
        except Exception as e:#Expection is the common error
            print("Error : "+ str(e))



        

