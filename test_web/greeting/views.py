from django.shortcuts import render


def hello_view(request):
    name = request.GET.get('name', 'Recruto')
    message = request.GET.get('message', 'Давай дружить!')
    return render(request, 'hello.html', {'name': name, 'message': message})
