import threading

from sqlalchemy import Column, String

from AnshiRobot.modules.sql import BASE, SESSION


class AnshiChats(BASE):
    __tablename__ = "Anshi_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


AnshiChats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()


def is_Anshi(chat_id):
    try:
        chat = SESSION.query(AnshiChats).get(str(chat_id))
        return bool(chat)
    finally:
        SESSION.close()


def set_Anshi(chat_id):
    with INSERTION_LOCK:
        Anshichat = SESSION.query(AnshiChats).get(str(chat_id))
        if not Anshichat:
            Anshichat = AnshiChats(str(chat_id))
        SESSION.add(Anshichat)
        SESSION.commit()


def rem_Anshi(chat_id):
    with INSERTION_LOCK:
        Anshichat = SESSION.query(AnshiChats).get(str(chat_id))
        if Anshichat:
            SESSION.delete(Anshichat)
        SESSION.commit()
      
