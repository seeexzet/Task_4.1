import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from random import randint
import string, random
from students.models import Course, Student

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def factory_courses():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory

@pytest.mark.django_db
def test_course_retrieve(client, factory_courses):
    #arrange
    course = factory_courses(_quantity=1)

    #act
    response = client.get('/courses/')

    #assert
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == course[0].name


@pytest.mark.django_db
def test_courses(client, factory_courses):
    #arrange
    courses = factory_courses(_quantity=10)

    #act
    response = client.get('/courses/')

    #assert
    assert response.status_code == 200
    data = response.json()
    for i, c in enumerate(data):
       assert c['name'] == courses[i].name


@pytest.mark.django_db
def test_filter_courses_by_id(client, factory_courses):
    #arrange
    courses = factory_courses(_quantity=10)

    #act
    numb = randint(courses[0].id, courses[9].id)
    response = client.get('/courses/', data = {'id': numb}, format = 'json')

    #assert
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == courses[numb - courses[0].id].name


@pytest.mark.django_db
def test_filter_courses_by_name(client, factory_courses):
    #arrange
    courses = factory_courses(_quantity=10)

    #act
    col = randint(courses[0].id, courses[9].id) - courses[0].id
    numb = courses[col].name
    response = client.get('/courses/', data = {'name': numb}, format = 'json')

    #assert
    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == courses[col].id


@pytest.mark.django_db
def test_create_course(client):
    #arrange
    letter = random.choice(string.ascii_letters)
    data = {'name': letter}

    #act
    response = client.post('/courses/', data, format = 'json')

    #assert
    assert response.status_code == 201
    data = response.json()
    print('d=', data['name'])

    assert data['name'] == letter


# @pytest.mark.django_db
# def test_patch_course(client, factory_courses):
#     #arrange
#     courses = factory_courses(_quantity=1)
#     response = client.get('/courses/')
#     patch_id = response.json()[0]['id']
#
#     #act
#     patch_text = 'new_name'
#     response = client.patch('/courses/', data = {'id': patch_id, 'name': patch_text}, format = 'json')
#
#     #assert
#     #assert response.status_code == 200
#     data = response.json()
#     assert data == patch_text


@pytest.mark.django_db
def test_delete_course(client, factory_courses):
    #arrange
    courses = factory_courses(_quantity=1)
    response = client.get('/courses/')
    course_id = response.json()[0]['id']

    #act
    response = client.delete('/courses/', data = {'id': course_id}, format = 'json')

    #assert
    #assert response.status_code == 200
    data = response.json()
    print(data)
    assert data[0]['id'] == course_id
