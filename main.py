from tkinter import *
from tkinter import filedialog as fd
from gtts import gTTS
from PyPDF2 import PdfReader

# ---------- Variables ---------#
FONT = "Times 16 bold"

# ---------- Globals ---------#
FILENAME = ''

# ---------- Tkinter Setup ---------#
window = Tk()
window.title("PDF to Audiobook Converter")
window.geometry("800x600")
window.columnconfigure([1,2], weight=1)


# ---------- Functions ---------#
def select_file():
    global FILENAME
    f_types = [('PDF Files', '*.pdf')]
    FILENAME = fd.askopenfilename(title='Open a file', filetypes=f_types)
    result.config(text=f"You've selected:\n{FILENAME.split('/')[-1]}", fg='green', font=FONT)
    result.grid(column=1, row=3)


def convert_file():
    # Extract text from pdf
    global FILENAME
    text_content = ''
    reader = PdfReader(FILENAME)
    number_of_pages = len(reader.pages)
    for n in range(number_of_pages):
        page = reader.pages[n]
        text_content += page.extract_text()

    # Convert to Audiobook
    save_types = [('MP3 Files', '*.mp3')]
    save_folder = fd.asksaveasfilename(title="Where do you want to save the Audiobook?", filetypes=save_types,
                                   defaultextension= save_types)
    tts = gTTS(text=text_content, lang='en', tld='com')
    tts.save(save_folder)
    result.config(text=f'Your Audiobook is Ready :)', fg='green', font=FONT)
    result.grid(column=2, row=3)



# GUI
canvas = Canvas(window, width=700, height=200, border=2, relief=RIDGE)

label = Label(window, text="Choose the pdf file you would like to convert in a Audiobook!", font=FONT)
label.grid(column=1, row=0, pady=(50, 50), columnspan=2)
upload_button = Button(window, text="Choose File", command=select_file, width=30)
upload_button.grid(column=1, row=2)
convert_button = Button(window, text="Convert to Audiobook", command=convert_file, width=30)
convert_button.grid(column=2, row=2)
result = Label(window, text='')


# Main Loop
window.mainloop()