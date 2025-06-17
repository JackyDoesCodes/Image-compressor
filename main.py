# Copyright: Joaquín Andrés Baigorria

from PIL import Image
import os
from tkinter import Tk, Label, Button, Entry

title = ('French Script MT', 36, 'bold')
subtitle = ('Lora', 10, 'bold')
text = ('Arial', 11)
blue = '#2b547e'
light_blue = '#b6cfde'
green = '#aaffbb'
window = Tk()

user = os.getlogin()
try:
    directory_loc = os.listdir('files-go-here')
except FileNotFoundError:
    os.mkdir('./files-go-here')


def open_explorer():
    os.startfile(f"C:/Users/{user}/Downloads")


class Program:
    """UI elements"""

    def __init__(self):
        self.window = window
        self.window.title('BlueJay')
        self.window.config(padx=20, pady=20, bg=blue)
        self.window.resizable(False, False)
        self.window.geometry('800x500')

        self.title_label = Label()
        self.subtitle_label = Label()
        self.mb_label = Label()
        self.quality_label = Label()
        self.open_explorer_btn = Button()
        self.start_compression_btn = Button()
        self.threshold_entry = Entry(name='threshold_entry',
                                     bg=light_blue,
                                     borderwidth=2,
                                     font=text,
                                     relief='flat'
                                     )
        self.quality_entry = Entry(name='quality_entry',
                                   bg=light_blue,
                                   borderwidth=2,
                                   font=text,
                                   relief='flat'
                                   )

    def load_ui_elements(self):
        """Graphics of ui elements. Used to configure widgets attributes"""
        # Labels
        self.title_label.config(text='BlueJay',
                                font=title,
                                background=blue,
                                foreground='white'
                                )
        self.title_label.grid(column=0, row=0, pady=(0, 10), columnspan=3)

        self.subtitle_label = Label(text="Image Compressor",
                                    font=subtitle,
                                    background=blue,
                                    foreground='white'
                                    )
        self.subtitle_label.grid(column=0, row=1, pady=(0, 20), columnspan=3)

        self.mb_label.config(text="MB",
                             font=text,
                             background=blue,
                             foreground='white'
                             )
        self.mb_label.grid(column=2, row=2)

        self.quality_label.config(text="%",
                                  font=text,
                                  background=blue,
                                  foreground='white'
                                  )
        self.quality_label.grid(column=2, row=3)

        # Buttons
        self.open_explorer_btn.config(text='Open\nexplorer',
                                      fg='black',
                                      bg=light_blue,
                                      font=text,
                                      highlightthickness=0,
                                      width=14,
                                      height=1,
                                      command=open_explorer)
        self.open_explorer_btn.config(padx=10, pady=20, bd=0)
        self.open_explorer_btn.grid(column=0, row=2, sticky="nsew", padx=100, pady=10, rowspan=2)

        self.start_compression_btn.config(text='Start compression',
                                          fg='black',
                                          bg=light_blue,
                                          font=text,
                                          highlightthickness=0,
                                          width=14,
                                          height=1,
                                          command=self.compress)
        self.start_compression_btn.grid(column=1, row=5, sticky="nsew", padx=20, pady=10)
        self.start_compression_btn.config(padx=33, pady=20, bd=0)

        # Entries
        self.threshold_entry.insert(index=0, string='2000000')
        self.threshold_entry.grid(column=1, row=2)

        self.quality_entry.insert(index=0, string='90')
        self.quality_entry.grid(column=1, row=3)

    def compress(self):
        compressing_label = Label(text="Compressing...",
                                  font=text,
                                  background=blue,
                                  foreground='grey'
                                  )
        compressing_label.grid(column=1, row=6, pady=(5, 20))
        compressing_label.update()

        try:
            os.listdir('output')
        except FileNotFoundError:
            os.mkdir('./output')

        files_analysed = 0
        files_compressed = 0
        for file in directory_loc:
            file_stats = os.stat(f'files-go-here/{file}')
            file_size = file_stats.st_size

            if '(1)' in file:
                print(f'File "{file}" is duplicated. Leaving it on root folder')
                files_analysed += 1
                pass

            elif 'png' in file or 'jpg' in file:
                threshold = int(self.threshold_entry.get())
                quality = int(self.quality_entry.get())
                if file_size > threshold:
                    img = Image.open(f'files-go-here/{file}')
                    img = img.convert(mode='RGB')
                    img.save(f'files-go-here/{file}', 'JPEG', quality=quality)

                    os.replace(f'files-go-here/{file}', f'output/{file}')
                    print(f'Successfully COMPRESSED: "{file}"')
                    files_analysed += 1
                    files_compressed += 1

                else:
                    os.replace(f'files-go-here/{file}', f'output/{file}')
                    print(f'Successfully MOVED: "{file}"')
                    files_analysed += 1

            else:
                os.replace(f'files-go-here/{file}', f'output/{file}')
                print(f'Successfully MOVED gif or video: "{file}"')
                files_analysed += 1

        if files_compressed == 1:
            print(f'Process finished. {files_analysed} files analyzed. {files_compressed} file compressed')
            compressing_label.config(text=f'{files_analysed} files analyzed.\n{files_compressed} image compressed.',
                                     foreground=green)
        else:
            print(f'Process finished. {files_analysed} files analyzed. {files_compressed} files compressed')
            compressing_label.config(text=f'{files_analysed} files analyzed.\n{files_compressed} images compressed.',
                                     foreground=green)


ui = Program()

ui.load_ui_elements()

window.mainloop()
