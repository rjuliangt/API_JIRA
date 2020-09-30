"""
Creation of all CRUD view and function of
the Task model
"""
from .models import Task
from .serializers import TaskSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TaskList(APIView):
    """
    List all task, or create a new task.
    """
    def get(self, request, format=None):
        task = Task.objects.all()
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        req_data = request.data
        print(type(req_data))
        print(dir(req_data))
        if req_data['fk_user'] is not None:
            print(req_data['fk_user'])
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = TaskSerializer(data=req_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetail(APIView):
    """
    Retrieve, update or delete a task instance.
    """
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        print(serializer.data)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskDetailByManage(APIView):
    """
    View all task instance by manage fk and update status
    """
    def get_object(self, fk_user):
        try:
            return Task.objects.filter(fk_user=fk_user)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, fk_user, format=None):
        task = self.get_object(fk_user)
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)

    def put(self, request, fk_user):
        task = self.get_object(fk_user)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Report secction
class TaskDetailByStatus(APIView):
    """
    View all task instance by manage fk
    """
    def get_object(self, task_status):
        try:
            status_op = {1: 'To Do',  2: 'Doing', 3: 'Done'}
            var = status_op[task_status]
            return Task.objects.filter(status=var)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, task_status):
        task = self.get_object(task_status)
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)


class TaskCountByManage(APIView):
    """
    View all task instance by manager_fk according to task status
    'To Do', 'Doing', 'Done'
    """
    def get_object(self, fk):
        try:
            op = {1: 'To Do',  2: 'Doing', 3: 'Done'}
            to_do = Task.objects.filter(status=op[1], fk_user=fk).count()
            doing = Task.objects.filter(status=op[2], fk_user=fk).count()
            done = Task.objects.filter(status=op[3], fk_user=fk).count()
            result = {'To Do': to_do, 'Doing': doing, 'Done': done}
            return result
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, fk):
        task = self.get_object(fk)
        return task
