from django.shortcuts import render
import json


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        to_json = {'name': name,
                   'phone': phone,
                   'message': message}
        print(f'{name} ({phone}): {message}')
        try:
            with open("contacts_data.json", "r") as json_file:
                content = json.load(json_file)
                content.append(to_json)
            with open("contacts_data.json", "w") as json_file:
                json.dump(content, json_file, ensure_ascii=False, indent=2)
        except FileNotFoundError:
            with open("contacts_data.json", "w", encoding='utf-8') as json_file:
                content = [to_json]
                json.dump(content, json_file)
    return render(request, 'catalog/contacts.html')
