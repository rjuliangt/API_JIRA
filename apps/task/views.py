from django.views import View
from .models import Task
from django.http import JsonResponse
from django.forms.models import model_to_dict


# Create your views here.
class TaskView(View):
    def get(self, request):
        all_data = Task.objects.all()
        return JsonResponse(list(all_data.values()), safe=False)


# Create your views here.
class TaskViewDetail(View):
    def get(self, request, fk):
        data = Task.objects.get(fk_user=fk)
        return JsonResponse(model_to_dict(data))
