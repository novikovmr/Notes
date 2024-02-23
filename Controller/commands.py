import Notes
import Logs.load as load
import Logs.write as write


def add_note():
    title = input("Введите заголовок:\n")
    content = input ("Введите содержимое заметки: \n")
    note = Notes.Note(title=title, content=content)
    notes_arr = load.read_file()
    for i in notes_arr:
        if Notes.Note.get_id(note) == Notes.Note.get_id(i):
            Notes.Note.set_id(note)

    notes_arr.append(note)
    write.write_file(notes_arr, 'a')
    print('Заметка добавлена')


def print_note(txt):
    notes_arr = load.read_file()

    if notes_arr:
        if txt == "all":
            print("Журнал заметок:")
            for i in notes_arr:
                print(Notes.Note.map_note(i))

        elif txt == "ID":
            for i in notes_arr:
                print("ID: ", Notes.Note.get_id(i))
            id = input("\nВведите id заметки: ")
            flag = True
            for i in notes_arr:
                if id == Notes.Note.get_id(i):
                    print(Notes.Note.map_note(i))
                    flag = False
            if flag:
                print("Нет такого id")

        elif txt == "date":
            date = input("Введите дату в формате: dd.mm.yyyy: ")
            flag = True
            for i in notes_arr:
                date_note = str(Notes.Note.get_date(i))
                if date == date_note[:10]:
                    print(Notes.Note.map_note(i))
                    flag = False
            if flag:
                print("Нет такой даты")
        else:
            print("Журнал заметок пустой!")

def delete_notes():
    id = input("Введите ID удаляемой заметки: ")
    notes_arr = load.read_file()
    flag = False

    for i in notes_arr:
        if id == Notes.Note.get_id(i):
            notes_arr.remove(i)
            flag = True

    if flag:
        write.write_file(notes_arr, 'a')
        print("Заметка с id: ", id, " успешно удалена!")
    else:
        print("нет такого id")

def change_note():
    id = input("Введите ID изменяемой заметки: ")
    notes_arr = load.read_file()
    flag = True
    notes_arr_new = []
    for i in notes_arr:
        if id == Notes.Note.get_id(i):
            i.title = input("измените  заголовок:\n")
            i.body = input("измените  описание:\n")
            Notes.Note.set_date(i)
            logic = False
        notes_arr_new .append(i)

    if flag:
        write.write_file(notes_arr_new , 'a')
        print("Заметка с id: ", id, " успешно изменена!")
    else:
        print("нет такого id")