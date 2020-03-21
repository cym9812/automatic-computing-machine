import tkinter


def main():
    root = tkinter.Tk()
    root.geometry("750x200+30+10")
    '''
    root.config(background="light slate gray")
    #root.geometry("1024x768+100+30")
    hello = tkinter.Label(root, text="hello")
    font_config = ("微软雅黑", "200", "bold")
    hello.config(bg="red", fg="blue", font=font_config)
    hello.pack()
    root.mainloop()
    '''
    labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    number_config = ("微软雅黑", "100")
    for i in range(len(labels)):
        if i < 3:
            number_label = tkinter.Label(root, text=str(labels[i]))
            number_label.grid(row=0, column=i)
        elif i < 6:
            number_label = tkinter.Label(root, text=str(labels[i]))
            number_label.grid(row=1, column=(i - 3))
        else:
            number_label = tkinter.Label(root, text=str(labels[i]))
            number_label.grid(row=3, column=(i - 6))
        number_label.config(font=number_config)
    root.mainloop()

main()
