from translate import Translator
from tkinter import *



window= Tk()
window.title("Language Translator")
window.config(bg="pink")
# window.geometry("500x450")
title_label =Label(window, text="language Translator")
title_label.pack(pady=(10,0), fill=X)
lang1 =StringVar()
lang2= StringVar()
choices = ['English', 'Chinese', 'French', 'German', 'Nepali', 'Hindi']
lang1.set('English')
lang2.set('Nepali')

lang1_menu = OptionMenu(window, lang1, *choices)
lang1_menu.config(font=('Helvectica', 20))
lang1_menu.pack(side = LEFT, padx=(100,0), pady=(0,150))


lang2_menu = OptionMenu(window, lang2, *choices)
lang2_menu.config(font=('Helvectica', 20))
lang2_menu.pack(side = RIGHT, padx=(0,100), pady=(0,150))

textbox1 = Text(window, height=8, width=30, font=('verdanna', 10))
textbox1.place(in_=lang1_menu, relx=0, x=-60, rely=1.5)

textbox2 = Text(window, height=8, width=30, font=('verdanna', 10))
textbox2.place(in_=lang2_menu, relx=0, x=-60, rely=1.5)

def translate():
    textbox2.delete("1.0", "end")
    var1 = textbox1.get("1.0","end-1c")
    translator = Translator(from_lang = lang1.get(), to_lang = lang2.get())
    translation = translator.translate(str(var1))
    textbox2.insert(END, translation)

translete_btn= Button(window, text="Translate", width=10, font=('Agency Fb', 20) , command=translate)
translete_btn.pack(pady=(10,0), side=BOTTOM)








window.mainloop()








