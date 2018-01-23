from populate import base
from django.contrib.auth.models import User
from account.models import UserProfile


def populate(): 
    print('Creating user accounts ... ', end='')
    User.objects.exclude(is_superuser=True).delete()
    for a in range(1):
        username = 'user' + str('a')
        user = User.objects.create_user(username=username, password=username, email=username+'@gmail.com')
        UserProfile.objects.create(user=user, fullName=user.username)
    print('done')


if __name__ == '__main__':
    populate()