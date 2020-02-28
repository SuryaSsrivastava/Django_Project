import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'ProjectTwo.settings')

import django
django.setup()

from ProjectTwoApp.models import User
from faker import Faker

fakegen=Faker()

def populate(N=5):
    for entry in range(N):
        fake_name=fakegen.name().split()
        fake_first_name=fakegen.name()[0]
        fake_last_name=fakegen.name()[1]
        fake_email=fakegen.email()

        #New entry

        user=User.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)[0]

if __name__ == '__main__':
    print("Populating Datebases!")
    populate(20)
    print("Population Complete!")
