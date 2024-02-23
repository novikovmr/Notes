from datetime import datetime

import idCounter


class Note:
    def __init__(self, id = str(idCounter.counter()), title='текст', content='текст',
                 date=str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = id
        self.title = title
        self.content = content
        self.date = date

        def get_id(note):
            return note.id

        def get_title(note):
            return note.title

        def get_content(note):
            return note.content

        def get_date(note):
            return note.date

        def set_id(note):
            note.id = str(idCounter.counter())

        def set_title(note):
            note.title = note

        def set_content(note):
            note.content = note

        def set_date(note):
            note.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

        def to_string(note):
            return note.id + ';' + note.title + ';' + note.content + ';' + note.date

        def map_note(note):
            return '\nID: ' + note.id + '\n' + 'Заголовок: ' + note.title + '\n' + 'Описание: ' + note.content + '\n' + 'Дата публикации: ' + note.date