from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.

def index(request):
	try:
		tasks = Task.objects.all()

		form = TaskForm()

		if request.method =='POST':
			form = TaskForm(request.POST)
			if form.is_valid():
				form.save()
			return redirect('/')


		context = {'tasks':tasks, 'form':form}
		return render(request, 'tasks/list.html', context)
	except Exception as e:
		print(e)

def updateTask(request, pk):
	try:
		task = Task.objects.get(id=pk)

		form = TaskForm(instance=task)

		if request.method == 'POST':
			form = TaskForm(request.POST, instance=task)
			if form.is_valid():
				form.save()
				return redirect('/')

		context = {'form':form}

		return render(request, 'tasks/update_task.html', context)
	except Exception as e:
		print(e)

def deleteTask(request, pk):
	try:

		item = Task.objects.get(id=pk)

		if request.method == 'POST':
			item.delete()
			return redirect('/')
		context = {'item':item}
		return render(request, 'tasks/delete.html', context)

	except Exception as e:
		print(e)
