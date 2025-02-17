# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.

from datetime import datetime

class Note:
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

    def __init__(self, code: str, title: str, text: str, importance: str):
        self.code = code
        self.title = title
        self.text = text
        self.importance = importance
        self.creation_date = datetime.now()
        self.tags = []

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        return f"Date: {self.creation_date}\n{self.title}: {self.text}"


class Notebook:
    def __init__(self):
        self.notes = []

    def add_note (self, title: str, text: str, importance: str)-> int:
        code = len(self.notes) + 1
        note = Note(str(code), title, text, importance)
        self.notes.append(note)

        return code

    def delete_note(self, code: int):
        self.notes = [note for note in self.notes if note.code != str(code)]

    def important_notes(self):
        return [note for note in self.notes if note.importance in [Note.HIGH, Note.MEDIUM]]

    def notes_by_tag(self, tag: str):
        return [note for note in self.notes if tag in note.tags]

    def tag_with_most_notes(self):
        tag_counts = {}
        for note in self.notes:
            for tag in note.tags:
                tag_counts[tag] = tag_counts.get(tag, 0) + 1
        if not tag_counts:
            return None
        max_count = max(tag_counts.values())
        most_common_tags = [tag for tag, count in tag_counts.items() if count == max_count]
        return sorted(most_common_tags)[0]












