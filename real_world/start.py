class newwindow(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        self.wn = window
        self.wn.title('Terminal')
        self.new_frame = Frame(self.wn)
        self.new_frame.grid(row=1, column=0)
        global text
        text = StringVar()
        self.text = Text(self.new_frame, textvariable=text)
        self.text.grid(row=1, column=0)
        self.back_btn = Button(self.new_frame, image=image.backimage(self), command=self.Home)

        self.back_btn.place(x=545, y=0)
        self.button = Button(self.wn, text='ATTACK', command=lambda: terminal.run(ap, fil, func))
        self.button.place(x=250, y=430)

    old_stdout = sys.stdout

    sys.stdout = terminal.Redirect(text)

    # - after close window -

    sys.stdout = old_stdout

    def Home(self):
        self.wn.switch_frame(Home)
        self.new_frame.destroy()