from tkinter import Tk, messagebox, simpledialog

root = Tk()
root.title("Encrypt_Decrypt_Msg")
task = simpledialog.askstring('Task', 'Do you want to encrypt or decrypt?')
root.mainloop()
