from http import HTTPStatus

from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось!', status=HTTPStatus.OK)


def second_page(request):
    return HttpResponse('А это вторая страница!', status=HTTPStatus.OK)
