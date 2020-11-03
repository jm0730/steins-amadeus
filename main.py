import tkinter as tk
import sys
from playsound import playsound
import speech_recognition as sr
import time
import webbrowser
import os.path
import os
from fontTools.ttLib import TTFont
font = TTFont('ImcreSoojin.ttf')
font.save(self, file, reorderTables=True)
def h():
    webbrowser.open('wiki.amadeuspython.ml')

def amadeusclick():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        label.configure(text='한국어로 말하세요')
        audio = r.listen(source)
    try:
        label.configure(text="당신은 말했습니다.: " + r.recognize_google(audio, language="ko-KR"))

        if '안녕' in r.recognize_google(audio, language="ko-KR"):
            label.configure(text="Hello")
            playsound('./sound\hello.mp3')

        elif "무엇을 할 수 있" in r.recognize_google(audio, language="ko-KR"):
            label.configure(text="무엇이든 물어봐 주세요. 가능한 범위에서 대답해드릴테니까요.")
            playsound('./sound\askmewhatever.mp3')

        elif '기분 좋' in r.recognize_google(audio, language="ko-KR"):
            label.configure(text="그래요?")
            playsound('./sound\you_sure.mp3')

        elif "크리스티나" in r.recognize_google(audio, language="ko-KR"):
            label.configure(text="크리스티나?")
            playsound('./sound\christina.mp3')

        elif "전화 걸어" in r.recognize_google(audio, language="ko-KR"):
            label.configure(text="(전화연결음...)")
            playsound('./sound\christina.mp3')

        elif "나무위키" in r.recognize_google(audio, language="ko-KR"):
            label.configure(text="나무위키에 접속합니다.")
            webbrowser.open('https://namu.wiki')

        elif '너는 이미 죽어 있다' in r.recognize_google(audio, language="ko-KR"):
            label.configure(text="예? 왜요?")
            playsound('./sound\huh_why_say.mp3')

        elif "타임머신은 가능" in r.recognize_google(audio, language="ko-KR"):
            label.configure(text="그렇네요 결론부터 말하자면 타임머신은 가능하지 않아...")
            playsound('./sound\tm_not_possible.mp3')

        elif "누구" in r.recognize_google(audio, language="ko-KR"):
            label.configure(text="그러고보니 제대로 자기소개도 하지 않았네요. 저는 마키세 크리스. 잘 부탁해요.")
            playsound('./sound\pleased_to_meet_you.mp3')

        elif "크롬" in r.recognize_google(audio, language="ko-KR"):
            chromepath = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
            if os.path.isfile(chromepath):
                print("크롬을 실행합니다.")
                playsound('./sound\you_sure.mp3')
                os.startfile(chromepath)

            else:
                print('크롬 브라우저가 설치되지 않았거나 지정된 경로에 없습니다.')
                playsound('./sound\sorry.mp3')

        else:
            webbrowser.open("http://www.google.com/search?q=" + r.recognize_google(audio, language="ko-KR"))

    except sr.UnknownValueError:
        print("질문을 이해할 수 없습니다.")
        playsound('./sound\sorry.mp3')


root = tk.Tk()
root.title('아마데우스')

kurisu = 'kurisu_normal1.png'
img = tk.PhotoImage(file=kurisu)

kurisu_button = tk.Button(root, image=img, command=amadeusclick)
kurisu_button.pack()

h_button = tk.Button(root, text='커맨드', command=h)
h_button.pack()

label = tk.Label(root, text='말하려면 크리스를 클릭하세요.', font=("ImcreSoojin", 30))
label.pack()

root.mainloop()
