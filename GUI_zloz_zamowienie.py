from tkinter import *


class Application(Frame):
    """Aplikacja z GUI, w której użytkownik wybiera potrawy z menu,
       a na koniec dostaje końćowy rachunek.
    """

    def __init__(self, master):
        """Inicjalizuj ramkę"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Widżety potrzebne do pokazania menu. """

        # etykieta z powitaniem w restauracji
        Label(self,
              text="Witamy w restauracji 'Złoty Dzwon'."
              ).grid(row=0, column=1, columnspan=2, sticky=W)

        # etykieta do wybrania dania
        Label(self,
              text="Dania do wboru w naszej restauracji."
              ).grid(row=1, column=0, sticky=W)

        # pola wyboru dań
        self.choose_burger = BooleanVar()
        Checkbutton(self,
                    text="Burger",
                    variable = self.choose_burger,
                    command = self.update_text
                    ).grid(row=2, column=0, sticky=W)

        self.choose_pizza = BooleanVar()
        Checkbutton(self,
                    text="Pizza",
                    variable=self.choose_pizza,
                    command=self.update_text
                    ).grid(row=2, column=1, sticky=W)

        self.choose_hot_dog = BooleanVar()
        Checkbutton(self,
                    text="Hot-Dog",
                    variable=self.choose_hot_dog,
                    command=self.update_text
                    ).grid(row=2, column=2, sticky=W)

        self.choose_fries = BooleanVar()
        Checkbutton(self,
                    text="Frytki",
                    variable=self.choose_fries,
                    command=self.update_text
                    ).grid(row=3, column=0, sticky=W)

        self.choose_kebab = BooleanVar()
        Checkbutton(self,
                    text="Kebab",
                    variable=self.choose_kebab,
                    command=self.update_text
                    ).grid(row=3, column=1, sticky=W)

        self.choose_burito = BooleanVar()
        Checkbutton(self,
                    text="Burito",
                    variable=self.choose_burito,
                    command=self.update_text
                    ).grid(row=3, column=2, sticky=W)

        Label(self,
              text="Napoje do wyboru."
              ).grid(row=4, column=0, sticky=W)

        self.choose_coffee = BooleanVar()
        Checkbutton(self,
                    text="Kawa",
                    variable=self.choose_coffee,
                    command=self.update_text
                    ).grid(row=5, column=0, sticky=W)

        self.choose_tea = BooleanVar()        
        Checkbutton(self,
                    text="Herbata",
                    variable=self.choose_tea,
                    command=self.update_text
                    ).grid(row=5, column=1, sticky=W)

        self.choose_water = BooleanVar()
        Checkbutton(self,
                    text="Woda",
                    variable=self.choose_water,
                    command=self.update_text
                    ).grid(row=5, column=2, sticky=W)

        self.choose_juice = BooleanVar()
        Checkbutton(self,
                    text="Sok",
                    variable=self.choose_juice,
                    command=self.update_text
                    ).grid(row=6, column=0, sticky=W)

        self.choose_cola = BooleanVar()
        Checkbutton(self,
                    text="Cola",
                    variable=self.choose_cola,
                    command=self.update_text
                    ).grid(row=6, column=1, sticky=W)

        self.choose_beer = BooleanVar()
        Checkbutton(self,
                    text="Piwo",
                    variable=self.choose_beer,
                    command=self.update_text
                    ).grid(row=6, column=2, sticky=W)

        Button(self,
               text="Akceptuj swój wybór.",
               command=self.check_bill
               ).grid(row=7, column=0, sticky=W)

        self.update_bill = Text(self, width=75, height=10, wrap=WORD)
        self.update_bill.grid(row=8, column=0, columnspan=4)

    def update_text(self):
        """ Zaktualizuj wybór i cene po wyborze jedzenia i picia. """

        self.choose = ""
        self.bill = 0

        if self.choose_burger.get():
            self.choose += "burgera "
            self.bill += 22

        if self.choose_pizza.get():
            self.choose += "pizze "
            self.bill += 30

        if self.choose_hot_dog.get():
            self.choose += "hot doga "
            self.bill += 8

        if self.choose_fries.get():
            self.choose += "frytki "
            self.bill += 5

        if self.choose_kebab.get():
            self.choose += "kebaba "
            self.bill += 17

        if self.choose_burito.get():
            self.choose += "burito "
            self.bill += 12

        if self.choose_coffee.get():
            self.choose += "kawę "
            self.bill += 6

        if self.choose_tea.get():
            self.choose += "herbate "
            self.bill += 4

        if self.choose_water.get():
            self.choose += "wode "
            self.bill += 2

        if self.choose_juice.get():
            self.choose += "sok "
            self.bill += 3

        if self.choose_cola.get():
            self.choose += "cole "
            self.bill += 5

        if self.choose_beer.get():
            self.choose += "piwo "
            self.bill += 8

    def check_bill(self):
        """Zaktualizuj pole tekstowe o cene i wybrane jedzenie. """

        order = "Wybrałeś: " + self.choose
        order += "\nRachunek wynosi: " + str(self.bill) + "zł"

        self.update_bill.delete(0.0, END)
        self.update_bill.insert(0.0, order)


# część głowna
root = Tk()
root.title("Restauracja")
app = Application(root)
root.mainloop()
