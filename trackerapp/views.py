import faker
import json
from django.shortcuts import render, redirect
from .models import User, ActivityPeriod


fake = faker.Faker()


def home(request):
    return render(request, 'home.html')


def insert_fakedata(request):
    for i in range(2):
        id = (fake.bothify(text='?###?#???')).upper()
        name = fake.name()
        t_z = fake.timezone()
        data = User(
            id=id,
            name=name,
            time_zone=t_z
        )
        data.save()
        for i in range(3):
            s_time = fake.date_time()
            e_time = fake.future_datetime()
            data_a = ActivityPeriod(
                ID_id=id,
                s_time=s_time,
                e_time=e_time
            )
            data_a.save()

    return redirect('/fetch')


def fetch_data(request):
    fakedata = User.objects.all().values_list('id', 'name', 'time_zone')
    response = {}
    list1 = []
    for i in fakedata:
        out_dict = {}
        out_dict['id'] = i[0]
        out_dict['real_name'] = i[1]
        out_dict['tz'] = i[2]
        access = ActivityPeriod.objects.filter(ID=i[0]).values_list('s_time', 'e_time')
        list2 = []
        for j in access:
            time_dict = {}
            time_dict['start_time'] = j[0].strftime("%b %d %Y %H:%M %p")
            time_dict['end_time'] = j[1].strftime("%b %d %Y %H:%M %p")
            list2.append(time_dict)
        out_dict['activity_periods'] = list2
        list1.append(out_dict)
    output = list1
    response['ok'] = True
    response['members'] = list(output)
    response = json.dumps(response)
    return render(request, 'fetching.html', {'response': response})


def delete_data(request):
    User.objects.all().delete()
    ActivityPeriod.objects.all().delete()
    return render(request, 'delete.html')
