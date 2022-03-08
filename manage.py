from bot_config import admins, bot 
# from bot_config import schedule
from utils import notify
from handlers import sets

handlers = {
    'start': sets.hello
}

admin_handlers = {
    
}


def start():
    bot.admins = admins
    # bot.add_task(schedule.on_startup)
    for cmd in handlers:
        bot.add_command_handler(cmd, handlers[cmd])
    for cmd in admin_handlers:
        bot.add_command_handler(cmd, admin_handlers[cmd], admin_only=True)
    notify.notify_admins('bot started')
    bot.start()
    notify.notify_admins('bot stopped')
