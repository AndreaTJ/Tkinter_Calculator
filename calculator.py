from tkinter import *
from tkinter import ttk


normal_buttons = [
    {
        "text": "1",
        "col": 0,
        "row": 4,
    },
    {
        "text": "2",
        "col": 1,
        "row": 4,
    },
    {
        "text": "3",
        "col": 2,
        "row": 4,
    },
    {
        "text": "+",
        "col": 3,
        "row": 4,
    },
    {
        "text": "4",
        "col": 0,
        "row": 3,
    },
    {
        "text": "5",
        "col": 1,
        "row": 3,
    },
    {
        "text": "6",
        "col": 2,
        "row": 3,
    },
    {
        "text": "-",
        "col": 3,
        "row": 3,
    },
    {
        "text": "7",
        "col": 0,
        "row": 2,
    },
    {
        "text": "8",
        "col": 1,
        "row": 2,
    },
    {
        "text": "9",
        "col": 2,
        "row": 2,
    },
    {
        "text": "x",
        "col": 3,
        "row": 2,
    },
    {
        "text": "C",
        "col": 1,
        "row": 1,
    },
    {
        "text": "+/-",
        "col": 2,
        "row": 1,
    },
    {
        "text": "÷",
        "col": 3,
        "row": 1,
    },
    {
        "text": "0",
        "col": 0,
        "row": 5, 
        "W": 2,
    },
    {
        "text": ",",
        "col": 2,
        "row": 5,
    },
    {
        "text": "=",
        "col": 3,
        "row": 5,
    }
]

roman_buttons = [
    {
        "text": "=",
        "col": 0,
        "row": 5,
        "W": 4
    },
    {
        "text": "I",
        "col": 0,
        "row": 4,
    },
    {
        "text": "V",
        "col": 1,
        "row": 4,
    },
    {
        "text": "X",
        "col": 0,
        "row": 3,
    },
    {
        "text": "L",
        "col": 1,
        "row": 3,
    },
    {
        "text": "C",
        "col": 0,
        "row": 2,
    },
    {
        "text": "D",
        "col": 1,
        "row": 2,
    },
    {
        "text": "M",
        "col": 2,
        "row": 2,
        "H": 3
    },
    {
        "text": "AC",
        "col": 1,
        "row": 1,
        "W": 2
    },
    {
        "text": "÷",
        "col": 3,
        "row": 1,
    },
    {
        "text": "x",
        "col": 3,
        "row": 2,
    },
    {
        "text": "-",
        "col": 3,
        "row": 3,
    },
    {
        "text": "+",
        "col": 3,
        "row": 4,
    }
]

def pinta(valor):
    print(valor)
    return valor

class Controlator(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=272, height=300)
        self.reset()
        self.status = "N"

        self.display = Display(self)
        self.display.grid(column=0, row=0)

        self.keyboard = Keyboard(self, self.set_operation, self.status)
        self.keyboard.grid(column=0, row=1)

        self.selector = Selector (self.keyboard, self.change_status, self.status)
        self.selector.grid(column=0, row=1)




    def reset(self):
        self.op1 = None
        self.op2 = None
        self.operation = ''
        self.dispValue = '0'
        self.signo_recien_pulsado = False
        self.pulse_equal = False 


    def to_float(self, valor):
        if "," in valor: 
            return float(valor.replace(',', '.'))
        else: 
            return round(float(valor))


    def to_str(self, valor):
        return str(valor).replace('.', ',')

    def calculate(self):
        if self.operation == '+':
            return self.op1 + self.op2
        elif self.operation == '-':
            return self.op1 - self.op2
        elif self.operation == 'x':
            return self.op1 * self.op2
        elif self.operation == '÷':
            return self.op1 / self.op2

        return self.op2

    def set_operation(self, algo):
        if self.status == "R": 
            message = "under development"
            print ("Roman Number Calculator under development ")
            self.dispValue = message
            
        if algo.isdigit():
            if self.dispValue == "0" or self.signo_recien_pulsado:
                self.op1 = self.to_float(self.dispValue)
                self.op2 = None
                self.dispValue = algo
                self.signo_recien_pulsado: False
            elif self.pulse_equal: 
                self.op1 = self.to_float(self.dispValue)
                self.op2 = None
                self.operation = ''
                self.dispValue = algo
                self.signo_recien_pulsado = False
                self.pulse_equal = False        
            else:
                self.dispValue += str(algo)
        
        if algo == 'C':
            self.reset()

        if algo == '+/-' and self.dispValue != '0':
            if self.dispValue[0] == '-':
                self.dispValue = self.dispValue[1:]
            else:
                self.dispValue = '-' + self.dispValue

        if algo == ',' and ',' not in self.dispValue:
            self.dispValue += str(algo)

        if algo == '+' or algo == '-' or algo =='x' or algo =='÷':
            if not self.op1:
                self.op1 = self.to_float(self.dispValue)
                self.operation = algo
            elif not self.op2:
                self.op2 = self.to_float(self.dispValue)
                res = self.calculate()
                self.dispValue = self.to_str(res)
                self.operation = algo
            else: 
                self.op1 = self.to_float(self.dispValue)
                self.op2 = None
                self.operation = algo
            self.signo_recien_pulsado = True
        else:
            self.signo_recien_pulsado = False

        if algo == '=':
            if self.op1 and not self.op2:
                self.op2 = self.to_float(self.dispValue)
                res = self.calculate()
                self.dispValue = self.to_str(res)
                self.pulse_equal = True 

            elif self.op1 and self.op2:
                self.op1 = self.to_float(self.dispValue)
                res = self.calculate()
                self.dispValue = self.to_str(res)
                self.pulse_equal = True 


        self.display.paint(self.dispValue)

    def change_status (self, status): 
        self.status = status 
        self.keyboard.status = status 
        self.reset() 

class Display(ttk.Frame):
    value = "0"
    
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=272, height=50)
        self.pack_propagate(0)

        s = ttk.Style()
        s.theme_use('alt')
        s.configure('my.TLabel', font='Helvetica 36', background='black', foreground='white')

        self.lbl = ttk.Label(self, text=self.value, anchor=E, style='my.TLabel')
        self.lbl.pack(side=TOP, fill=BOTH, expand=True)

    def paint(self, algo):
        self.value = algo
        self.lbl.config(text=algo)

        
class Selector(ttk.Frame):
    def __init__(self, parent, command, status="N"):
        ttk.Frame.__init__(self, parent, width=68, height=50)
        self.status = status
        self.__value = StringVar()
        self.__value.set(self.status)
        self.command = command 

        radiob1 = ttk.Radiobutton(self, text="N", value="N", name="rbtn_normal", variable=self.__value, command=self.__click)
        radiob1.place(x=0, y=5)
        radiob2 = ttk.Radiobutton(self, text="R", value="R", name="rbtn_romano", variable=self.__value, command=self.__click)
        radiob2.place(x=0, y=30)

    def __click(self):
        self.status = self.__value.get()
        self.command(self.status)


class Keyboard(ttk.Frame):
    def __init__(self, parent,command,  status="N"):
        ttk.Frame.__init__(self, parent, height=250, width=272)
        self.__status = status
        self.listaBRomanos = []
        self.listaBNormales = []
        self.command = command 
        
        if self.__status == "N":
            self.pintaNormal()
        else:
            self.pintaRomano()

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, valor):
        self.__status = valor
        if valor == 'N':
            self.pintaNormal()
        else:
            self.pintaRomano()

    def pintaNormal(self):
        if len(self.listaBNormales) == 0:
            for properties in normal_buttons:
                btn = CalcButton(self, properties['text'], self.command, properties.get("W", 1), properties.get("H", 1))
                self.listaBNormales.append((btn, properties))
                btn.grid(column=properties['col'], row=properties['row'], columnspan=properties.get("W", 1), rowspan=properties.get("H", 1))
        else:
            for btn, properties in self.listaBNormales: 
                 btn.grid(column=properties['col'], row=properties['row'], columnspan=properties.get("W", 1), rowspan=properties.get("H", 1))

        for borra, properties in self.listaBRomanos:
            borra.grid_forget()

    def pintaRomano(self):
        if len(self.listaBRomanos) == 0:
            for properties in roman_buttons:
                btn = CalcButton(self, properties['text'], self.command, properties.get("W", 1), properties.get("H", 1))
                self.listaBRomanos.append((btn, properties))
                btn.grid(column=properties['col'], row=properties['row'], columnspan=properties.get("W", 1), rowspan=properties.get("H", 1))
        else:
            for btn, properties in self.listaBRomanos:
                btn.grid(column=properties['col'], row=properties['row'], columnspan=properties.get("W", 1), rowspan=properties.get("H", 1))

        for borra, properties in self.listaBNormales:
            borra.grid_forget()



class CalcButton(ttk.Frame):
    def __init__(self, parent, value, command, width=1, height=1):
        ttk.Frame.__init__(self, parent, width=68*width, height=50*height)
        self.pack_propagate(0)

        btn = ttk.Button(self, text=value, command=lambda: command(value))
        btn.pack(side=TOP, fill=BOTH, expand=True)

