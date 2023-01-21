from typing import List

from db.postgres import diary_table
from models.diary import Diary
from repositories.base import BaseRepository


class DiaryRepository(BaseRepository):
   def create(self, user_id: int, d: Diary):
       pass

   def update(self):
       pass

   def list(self):
       pass

   def delete(self):
       pass
