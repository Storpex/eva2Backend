from django.shortcuts import render, redirect
from App.forms import FormDocente
from App.models import Docente

# Create your views here.
def index(request):
  return render(request, 'index.html')

def listadoDocentes(request):
  docentes = Docente.objects.all()
  data = {'docentes': docentes}
  return render(request, 'docentes.html', data)

def agregarDocentes(request):
  form = FormDocente(request.POST)
  if form.is_valid():
    form.save()
    return index(request)
  data = {'form': form}
  return render(request, 'agregarDocente.html', data)

def eliminarDocente(request, id):
  docente = Docente.objects.get(id = id)
  docente.delete()
  return redirect('/docentes')

def actualizarDocente(request, id):
  docente = Docente.objects.get(id = id)
  form = FormDocente(instance = docente)
  if request.method == 'POST':
    form = FormDocente(request.POST, instance = docente)
    if form.is_valid():
      form.save()
    return index(request)
  data = {'form': form}
  return render(request, 'agregarDocente.html', data)






