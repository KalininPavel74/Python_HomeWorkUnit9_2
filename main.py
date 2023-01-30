# Калинин Павел 30.01.2023
# # Знакомство с языком Python (семинары) 
# Урок 9. Часть 2. 
# Домашняя работа

# . venv/Scripts/activate
# # pip freeze > requirements.txt

taskName = '''Задание  №2. Создайте любого бота телеграмм(можно самый простой),
главное чтобы у вас к след. уроку был свой бот в телеграмме,
в нем вы сможете работать над созданием нового бота на 10 семинаре.
'''
print(taskName)
print()

#token = input("Введите TOKEN: ")
import getpass
token = getpass.getpass("Введите TOKEN и нажмите Enter (невижимый режим): ")
print(f'Получено {len(token)} символов.')

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print('def hello:',f'Hello {update.effective_user.first_name}')
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
async def bye(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print('def bye:',f'Bye {update.effective_user.first_name}')
    await update.message.reply_text(f'Bye {update.effective_user.first_name}')

app = ApplicationBuilder().token(token).build()
print('TOKEN принят telegram')
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("bye", bye))
print('server before app.run_polling()')
app.run_polling()
print('server after app.run_polling()')




#----------------------------- OLD 
'''
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *

#updater = Updater('TOKEN')
updater = Updater(s)

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))

print('server start')
updater.start_polling()
print('server updater.start_polling()')
updater.idle()
print('server updater.idle()')
'''
#----------------------------- NEW 
'''
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

app = ApplicationBuilder().token("YOUR TOKEN HERE").build()
app.add_handler(CommandHandler("hello", hello))
app.run_polling()
'''
