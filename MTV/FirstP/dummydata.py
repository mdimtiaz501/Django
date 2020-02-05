import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','FirstP.settings')

import django
django.setup()

import random  
from Hello.models import Subject,AccessRecord,Webpage
from faker import Faker

fakeobj = Faker()
subjects = ['Bangla','English','ICT','Physics','Chemistry']

def add_sub():
    s = Subject.objects.get_or_create(top_name=random.choice(subjects))[0]
    s.save()
    return s


def populate(N=5):
    for entry in range(N):

        top = add_sub()
        fake_url = fakeobj.url()
        fake_date = fakeobj.date()
        fake_name = fakeobj.company()

        wpage = Webpage.objects.get_or_create(topic=top,name=fake_name,url=fake_url)[0]
        acc_rec = AccessRecord.objects.get_or_create(name=wpage,date=fake_date)[0]



if __name__ == '__main__':
    print("Population Script!")
    populate(20)
    print("Population complete")




