from django.shortcuts import render


def hello_view(request):
    name = request.GET.get('name', None)
    message = request.GET.get('message', None)
    if name is None or message is None:
        return render(request, 'error.html')
    return render(request, 'hello.html', {'name': name, 'message': message})
