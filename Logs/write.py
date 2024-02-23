import Notes


def read_file():
    try:
        array=[]
        file = open("notes.csv", "r", encoding='utf-8')
        notes = file.read().strip().split("\n")
        for n in notes:
            split_n = n.split(';')
            note = Notes.Note(id=split_n[0], title=split_n[1], content=split_n[2], date=split_n[3])
            array.append(note)
    except Exception:
        print('журнал пустой')
    finally:
        return array
