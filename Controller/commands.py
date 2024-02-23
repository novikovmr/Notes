import Notes


def add_note():
    title = input("Введите заголовок:\n")
    content = input ("Введите содержимое заметки: \n")
    note = Notes.Note(title=title, content=content)
    