from asgiref.sync import sync_to_async
from django.db import IntegrityError

from admin_panel.telebot.models import Manager, Client, User


@sync_to_async()
def create_manager(username, telegram_id, phone, name):
    Manager.objects.get_or_create(telegram_id=telegram_id, username=username, phone=phone, name=name)


@sync_to_async()
def select_manager(telegram_id):
    return Manager.objects.filter(telegram_id=telegram_id)


@sync_to_async()
def status_manager(telegram_id):
    return Manager.objects.filter(telegram_id=telegram_id).first()


@sync_to_async()
def update_status_manager(telegram_id, status):
    Manager.objects.filter(telegram_id=telegram_id).update(is_working=status)


@sync_to_async()
def select_clients_by_manager(telegram_id):
    manager = Manager.objects.filter(telegram_id=telegram_id).first()
    return Client.objects.filter(manager=manager).all()


@sync_to_async()
def create_client(name, phone):
    try:
        Client.objects.create(name=name, phone=phone, status='Первый контакт')
    except IntegrityError:
        return True


@sync_to_async()
def get_last_client():
    return Client.objects.all().first()


@sync_to_async()
def get_client_numbers():
    return Client.objects.all()


@sync_to_async()
def get_client(phone):
    return Client.objects.filter(phone=phone).first()


@sync_to_async()
def update_status_client(pk, status):
    Client.objects.filter(pk=pk).update(status=status)


@sync_to_async()
def update_info_client(pk, info):
    Client.objects.filter(pk=pk).update(information=info)


@sync_to_async()
def update_manager_client(pk):
    Client.objects.filter(pk=pk).update(manager=None)


@sync_to_async()
def get_client_pk(pk):
    return Client.objects.filter(pk=pk).first()


@sync_to_async()
def update_client_manager(client_id, manager_tg_id):
    manager = Manager.objects.filter(telegram_id=manager_tg_id).first()
    Client.objects.filter(pk=int(client_id)).update(manager=manager.id)


@sync_to_async()
def get_is_working(telegram_id):
    return Manager.objects.filter(telegram_id=telegram_id).first().is_working


@sync_to_async()
def create_admin(password, username):
    user = User(username=username, is_superuser=True, is_staff=True)
    user.set_password(password)
    user.save()
    return user
