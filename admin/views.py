from sqladmin import ModelView
from bot.database.models import User, ThatAdmin

class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.telegram_id]
    column_telegram_id= [User.telegram_id]

class ThatID(ModelView, model=ThatAdmin):
    column_list = [ThatAdmin.id, ThatAdmin.id_that]
    column_telegram_id = [ThatAdmin.id_that]