from tkinter import Tk, messagebox, simpledialog


def get_task():
    task = simpledialog.askstring('Task', 'Do you want to Encrypt or decrypt?')
    return task


def get_message():
    message = simpledialog.askstring('Message', 'Enter the Secret Message: ')
    return message


def is_even(number):
    return number % 2 == 0


def get_even_letters(message):
    even_letters = []
    for counter in range(0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters


def get_odd_letters(message):
    odd_letters = []
    for counter in range(0, len(message)):
        if(not is_even(counter)):
            odd_letters.append(message[counter])
    return odd_letters


def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message = message+'x'

    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)

    for counter in range(0, int(len(message)/2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])

    new_message = ''.join(letter_list)
    return new_message


root = Tk()
root.title("Encrypt_Decrypt_Msg")
root.config(background='light sea green')

while True:
    task = get_task()
    if task == 'encrypt':
        message = get_message()
        encrypted = swap_letters(message)
        messagebox.showinfo('Ciphered text of Secret Message is: ', encrypted)
    elif task == 'decrypt':
        message = get_message()
        decrypted = swap_letters(message)
        messagebox.showinfo('Plaintext of the secret message is: ', decrypted)
    else:
        break


root.mainloop()
