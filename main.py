from PIL import Image
import os
from tkinter import Tk, Label, Button

user = os.getlogin()
try:
    directory_loc = os.listdir('files-go-here')
except FileNotFoundError:
    os.mkdir('./files-go-here')

THRESHOLD = 3000000  # 3mb
QUALITY = 90

main_font = ('Arial', 12)
secondary_font = ('Lora', 24, 'bold')


def compress():
    file_amount = 0
    files_analysed = 0
    for file in directory_loc:
        file_amount += 1

    for file in directory_loc:
        progress = 0
        file_stats = os.stat(f'files-go-here/{file}')
        file_size = file_stats.st_size

        if '(1)' in file:
            print(f'File "{file}" is duplicated. Leaving it on root folder')
            files_analysed += 1
            pass

        elif 'png' in file or 'jpg' in file:
            if file_size > THRESHOLD:
                img = Image.open(f'files-go-here/{file}')
                img = img.convert(mode='RGB')
                img.save(f'files-go-here/{file}', 'JPEG', quality=QUALITY)

                os.replace(f'files-go-here/{file}', f'Output/{file}')
                print(f'Successfully COMPRESSED: "{file}"')
                progress += 1
                files_analysed += 1

            else:
                os.replace(f'files-go-here/{file}', f'Output/{file}')
                print(f'Successfully MOVED: "{file}"')
                progress += 1
                files_analysed += 1

        else:
            os.replace(f'files-go-here/{file}', f'Output/{file}')
            print(f'Successfully MOVED GIF OR VIDEO: "{file}"')
            progress += 1
            files_analysed += 1

    print(f'Process finished. {files_analysed} files processed.')


def open_explorer():
    os.startfile(f"C:/Users/{user}/")


# _______________ UI ________________
window = Tk()
window.title('Image compressor')
window.config(padx=100, pady=50, bg='grey')
window.resizable(False, False)
window.geometry('600x500')

label = Label(text="Image Compressor",
              font=secondary_font,
              background='grey',
              foreground='white')
label.grid(column=1, row=0)
label.config(padx=10, pady=50)

open_folder_btn = Button(text='Open explorer',
                         fg='white',
                         bg='black',
                         font=main_font,
                         highlightthickness=0,
                         width=14,
                         height=1,
                         command=open_explorer)
open_folder_btn.grid(column=1, row=1, sticky="nsew")
open_folder_btn.config(padx=20, pady=20, bd=0)

empty_zone = Label(background='grey')
empty_zone.grid(column=1, row=2)

start_compression_btn = Button(text='Start compression',
                               fg='white',
                               bg='black',
                               font=main_font,
                               highlightthickness=0,
                               width=14,
                               height=1,
                               command=compress)
start_compression_btn.grid(column=1, row=3, sticky="nsew")
start_compression_btn.config(padx=20, pady=20, bd=0)

window.mainloop()
