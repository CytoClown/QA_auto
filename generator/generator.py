import random
import string

from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()

def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + ' ' + faker_ru.last_name() + ' ' + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(10, 80),
        department=faker_ru.job(),
        salary=random.randint(10000, 100000),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        phone_number=random.randint(1000000000, 9999999999)
    )

def generated_file():
    path = rf'C:\QA\QA_auto\filetest{random.randint(0, 999)}.txt'
    file = open(path, 'w+')
    file.write(f'Hello world {random.randint(0, 999)}')
    file.close()
    return file.name, path

def generated_subject():
    subject = ['Maths', 'Hindi', 'Biology', 'Chemistry', 'Arts', 'Accounting', 'Computer Science', 'Social Studies']
    return subject[random.randint(0, len(subject)-1)]

def generated_text():
    length = random.randint(0, 30)
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string