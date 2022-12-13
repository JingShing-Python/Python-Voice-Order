# tkinter toolkit
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import filedialog

# order bot
from order_bot import Order_Bot

class Gui_helper_main:
    def __init__(self):
        self.root = Tk()
        self.frame = None
        self.frame_index = 0
        self.root.geometry('300x100')
        self.root.title('Order Bot')
        self.root.protocol("WM_DELETE_WINDOW", self.quit)
        # maker info
        self.maker_name = Label(self.root, text="Maker: JingShing")
        self.maker_name.grid(column=0, row=3, sticky=N+W)
        
        self.frames = [page_module(self)]
        self.switch_frame(0)
        
    def switch_frame(self, index):
        if self.frame is not None:
            self.frame.grid_forget()
        self.frame_index = index
        self.frame = self.frames[self.frame_index]
        self.frame.grid(column=0, row=0, sticky=N+W)

    def run(self):
        self.root.mainloop()

    def quit(self):
        if messagebox.askyesno('Confirm','Are you sure you want to quit?'):
            self.root.quit()

class page_module(Frame):
    def __init__(self, master):
        Frame.__init__(self, master = master.root)
        self.main = master
        self.master = master.root
        
        # order bot
        self.order_bot = Order_Bot('text')

        # display last order
        self.last_order = StringVar()
        self.last_order = Label(self, textvariable=self.last_order)
        self.last_order.grid(column=0, row=0, sticky=N+W)
        
        # input box
        self.enter_label = Label(self, text='Order:')
        self.enter_label.grid(column=0, row=1)
        self.order_enter_box = Entry(self)
        self.order_enter_box.grid(column=1, row=1)
        
        self.order_button = Button(self, text='order', command=self.order)
        self.order_button.grid(column=2, row=1)

    def update_string_var(self):
        self.last_order.set(self.order_bot.last_order)

    def order(self):
        order_command = self.order_enter_box.get()
        
if __name__ == '__main__':
    main = Gui_helper_main()
    main.run()