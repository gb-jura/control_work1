import json
import datetime

class Note:
    def __init__(self, id, title, body, timestamp):
        self.id = id
        self.title = title
        self.body = body
        self.timestamp = timestamp


class NotesManager:
    def __init__(self):
        self.notes = []
        self.load_notes()

    def load_notes(self):
        try:
            with open("notes.json", "r") as file:
                data = json.load(file)
                for note_data in data:
                    note = Note(note_data['id'], note_data['title'], note_data['body'], note_data['timestamp'])
                    self.notes.append(note)
        except FileNotFoundError:
            # Если файл не найден, создаем новый список заметок
            self.notes = []

    def save_notes(self):
        data = []
        for note in self.notes:
            data.append({
                'id': note.id,
                'title': note.title,
                'body': note.body,
                'timestamp': note.timestamp
            })
        with open("notes.json", "w") as file:
            json.dump(data, file)

    def add_note(self, title, body):
        id = len(self.notes) + 1
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        note = Note(id, title, body, timestamp)
        self.notes.append(note)
        self.save_notes()
        print("Заметка добавлена.")

    def delete_note(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                self.notes.remove(note)
                self.save_notes()
                print("Заметка удалена.")
                return
        print("Заметка с таким ID не найдена.")

    def edit_note(self, note_id, title, body):
        for note in self.notes:
            if note.id == note_id:
                note.title = title
                note.body = body
                note.timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.save_notes()
                print("Заметка отредактирована.")
                return
        print("Заметка с таким ID не найдена.")

    def print_notes(self):
        for note in self.notes:
            print(f"ID: {note.id}")
            print(f"Заголовок: {note.title}")
            print(f"Тело заметки: {note.body}")
            print(f"Дата/время создания или последнего изменения: {note.timestamp}")
            print("\n")


# Создаем объект NotesManager и загружаем заметки
notes_manager = NotesManager()

while True:
    print("1. Добавить заметку")
    print("2. Удалить заметку")
    print("3. Редактировать заметку")
    print("4. Вывести список заметок")
    print("0. Выход")

    choice = input("Выберите действие: ")

    if choice == '1':
        title = input("Введите заголовок заметки: ")
        body = input("Введите текст заметки: ")
        notes_manager.add_note(title, body)

    elif choice == '2':
        note_id = int(input("Введите ID заметки для удаления: "))
        notes_manager.delete_note(note_id)

    elif choice == '3':
        note_id = int(input("Введите ID заметки для редактирования: "))
        title = input("Введите новый заголовок заметки: ")
        body = input("Введите новый текст заметки: ")
        notes_manager.edit_note(note_id, title, body)

    elif choice == '4':
        notes_manager.print_notes()

    elif choice == '0':
        break
