# -*- coding: utf-8 -*-

from tkinter import BOTH, Tk, W, E, N, S, Canvas, NW, messagebox
from tkinter.ttk import Frame, Style, Label, Entry, Button, Combobox

from PIL import Image, ImageTk, ImageFilter

max_h = 500
max_w = 900


class Okno(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.initialization()

    def load_image(self):
        path = self.o.get()
        try:
            self.image = Image.open(path)
            self.fbtn.config(state="normal")
            self.sbtn.config(state="normal")
            self.pbtn.config(state="normal")
            self.original_image = self.image
            self.load_image_again()
        except FileNotFoundError:
            messagebox.showerror("Błąd", "Plik nie istnieje!")
        except OSError:
            messagebox.showerror("Błąd", "Plik nie jest obrazem!")
        except Exception:
            messagebox.showerror("Błąd", "Upssss ;-(")

    def load_image_again(self):
        self.im = ImageTk.PhotoImage(self.image)
        self.base.create_image(0, 0, image=self.im, anchor=NW)

    def restore_image(self):
        self.image = self.original_image
        self.load_image_again()

    def initialization(self):
        self.parent.title("Tkinter")
        self.style = Style()
        self.style.theme_use("winnative")
        self.pack(fill=BOTH, expand=1)

        lbl = Label(self, text="Path to file: ")
        lbl.grid(sticky=W, pady=4, padx=5)

        self.o = Entry(self)
        self.o.grid(row=1, column=0, columnspan=2, rowspan=1, padx=5, pady=4, sticky=N + S + W + E)

        self.z = Entry(self)
        self.z.grid(row=2, column=0, columnspan=2, rowspan=1, padx=5, pady=4, sticky=N + S + W + E)

        open_btn = Button(self, text="Open", compound=self.load_image)
        open_btn.grid(row=1, column=3)

        save_btn = Button(self, text="Save")
        save_btn.grid(row=2, column=3)
        save_btn.config(state="disabled")

        self.sbox = Combobox(self, values=["0.1", "0.2", "0.3", "0.4"])
        self.sbox.grid(row=3, column=0, padx=5, pady=4, sticky=W + N)

        self.fbox = Combobox(self, values=["BLUR", "CONTOUR", "EMBOSS"])
        self.fbox.grid(row=4, column=0, padx=5, pady=4, sticky=W + N)

        self.sbtn = Button(self, text='Skaluj')
        self.sbtn.grid(row=3, column=1, padx=5, pady=4, sticky=W + N)
        self.sbtn.config(state="disabled")

        self.fbtn = Button(self, text='Filtruj')
        self.fbtn.grid(row=4, column=1, padx=5, pady=4, sticky=W + N)
        self.fbtn.config(state="disabled")

        self.base = Canvas(self, width=max_w, height=max_h)
        self.base.grid(row=5, column=0, padx=5, pady=4, sticky=W + N)

        self.pbtn = Button(self, text='Przywróć')
        self.pbtn.grid(row=5, column=3, padx=5, pady=4, sticky=W + N)


def main():
    gui = Tk()
    gui.geometry("1000x700")
    app = Okno(gui)
    gui.mainloop()


if __name__ == '__main__':
    main()
