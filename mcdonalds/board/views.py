from django.http import HttpResponse
from django.views import View
from .tasks import hello, printer
from datetime import datetime, timedelta


class IndexView(View):
    def get(self, request):
        printer.apply_async([10],
                            eta=datetime.now() + timedelta(seconds=5))
        hello.delay()
        return HttpResponse('Hello!')
