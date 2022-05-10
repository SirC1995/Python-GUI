import random
from tkinter import *


class Application(Frame):
    """Aplikacja z GUI, w której zgadujemy liczbę wybraną przez komputer."""

    def __init__(self, master):
        """Inicjalizuj ramkę"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.draw_number()

    def create_widgets(self):
        """Widżety potrzebne do gry"""

        # etykieta z instrukcją
        Label(self,
              text="Zgadnij liczbę którą wylosował komputer"
              ).grid(row=0, column=0, columnspan=2, sticky=W)

        # przycisk losujący liczbę w kolejnych grach
        Button(self,
               text="Wylosuj liczbę dla komputera",
               command=self.draw_number
               ).grid(row=2, column=0, sticky=W)

        # miejsce wpisania zgadywanej liczby
        Label(self,
              text="Podaj liczbę: "
              ).grid(row=1, column=0, sticky=W)
        self.number_ent = Entry(self)
        self.number_ent.grid(row=1, column=1, sticky=W)

        # przycisk sprawdzający
        Button(self,
               text="Kliknij, aby sprawdzić czy trafiłeś",
               command=self.check_number
               ).grid(row=2, column=1, sticky=W)

        self.answer_txt = Text(self, width=75, height=10, wrap=WORD)
        self.answer_txt.grid(row=3, column=0, columnspan=4)

    def draw_number(self):
        """Wylosuj liczbę dla komputera"""
        self.number = random.randint(1, 100)

    def check_number(self):
        """Wpisz w pole tekstowe odpowiedź czy gracz 
           wybrał taką samą liczbę jak komputer
        """

        number_ent = self.number_ent.get()

        if int(number_ent) > self.number:
            answer = "Za dużo!"

        elif int(number_ent) < self.number:
            answer = "Za mało!"

        elif int(number_ent) == self.number:
            answer = "Gratulacje poprawna odpowiedź "
            answer += "Poprawna liczba to: " + str(self.number)

        self.answer_txt.delete(0.0, END)
        self.answer_txt.insert(0.0, answer)


# część główna
root = Tk()
root.title("Jaka to liczba?")
app = Application(root)
root.mainloop()
