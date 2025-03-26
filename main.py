from PIL import Image
import os
from tkinter import Tk, Label, Button, Toplevel

title = ('French Script MT', 36, 'bold')
subtitle = ('Lora', 12, 'bold')
text = ('Arial', 12)
blue = '#2b547e'
light_blue = '#b6cfde'
green = '#aaffbb'
window = Tk()

THRESHOLD = 2
QUALITY = 90

user = os.getlogin()
try:
    directory_loc = os.listdir('files-go-here')
except FileNotFoundError:
    os.mkdir('./files-go-here')

files_target = 0
for file in directory_loc:
    files_target += 1


def compress():
    compressing_label = Label(text="Compressing",
                              font=text,
                              background=blue,
                              foreground='grey'
                              )
    compressing_label.grid(column=1, row=4, pady=(5, 20))
    compressing_label.update()

    files_analysed = 0
    try:
        os.listdir('output')
    except FileNotFoundError:
        os.mkdir('./output')

    for file in directory_loc:
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

                os.replace(f'files-go-here/{file}', f'output/{file}')
                print(f'Successfully COMPRESSED: "{file}"')
                files_analysed += 1

            else:
                os.replace(f'files-go-here/{file}', f'output/{file}')
                print(f'Successfully MOVED: "{file}"')
                files_analysed += 1

        else:
            os.replace(f'files-go-here/{file}', f'output/{file}')
            print(f'Successfully MOVED gif or video: "{file}"')
            files_analysed += 1
    print(f'Process finished. {files_analysed} files processed.')

    compressing_label.config(text='Finished',
                             foreground=green)


def open_explorer():
    os.startfile(f"C:/Users/{user}/Downloads")


def main_window():
    window.iconbitmap('res/bluejay.ico')
    window.title('BlueJay')
    window.config(padx=128, pady=125, bg=blue)
    window.resizable(False, False)
    window.geometry('500x500')

    title_label = Label(text='BlueJay',
                        font=title,
                        background=blue,
                        foreground='white'
                        )
    title_label.grid(column=1, row=0, pady=(0, 20))

    subtitle_label = Label(text="Image Compressor",
                           font=subtitle,
                           background=blue,
                           foreground='white'
                           )
    subtitle_label.grid(column=1, row=1, pady=(5, 20))

    open_folder_btn = Button(text='Open explorer',
                             fg='black',
                             bg=light_blue,
                             font=text,
                             highlightthickness=0,
                             width=14,
                             height=1,
                             command=open_explorer)
    open_folder_btn.grid(column=1, row=2, sticky="nsew", padx=20, pady=10)
    open_folder_btn.config(padx=20, pady=20, bd=0)

    start_compression_btn = Button(text='Start compression',
                                   fg='black',
                                   bg=light_blue,
                                   font=text,
                                   highlightthickness=0,
                                   width=14,
                                   height=1,
                                   command=compress)
    start_compression_btn.grid(column=1, row=3, sticky="nsew", padx=20, pady=10)
    start_compression_btn.config(padx=20, pady=20, bd=0)


main_window()
window.mainloop()
