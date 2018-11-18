from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from .models import Cliente, Bicicleta
from .forms import formularioCliente, formularioArriendo



def main (request):
    return render_to_response('mobike/main.html')



def getCliente(request, ID_CLIENTE):
    cliente = get_object_or_404(Cliente, pk=ID_CLIENTE)
    return render(request, 'mobike/ficha-cliente.html', {'cliente': cliente})



def getDisponibles(request):
    lista_bicicleta_disponible = Bicicleta.objects.filter(ESTADO_CANDADO="Bloqueado")[:5]
    context = {'lista_bicicleta_disponible': lista_bicicleta_disponible}
    return render(request, 'mobike/bicicletas-disponibles.html', context)



def addCliente(request):
    if request.method == 'POST':
        form = formularioCliente( request.POST,request.FILES)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            pk=cliente.pk
            #return render(request, 'mobike/ficha-cliente.html', )
            #return redirect('cliente/', pk)
            return render_to_response('mobike/regis_edit.html')
    else:
        form = formularioCliente()
    context = {'form':form}
    return render(request, 'mobike/registro-Cliente.html',context)

class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = ['RUT','NOMBRE_COMPLETO','EDAD','MEDIO_PAGO','NUMERO_CELULAR','EMAIL']

    success_url = '/'

def regis_edit(self, form):
        form.instance.author = self.request.user
        if self.request.user.has_perm('cliente.change_post'):
            return super().regis_edit(form)
def regis_edit(self, form):
        form.instance.author = self.request.user
        if self.request.user.has_perm('cliente.change_post'):
            return super().regis_edit(form)
=======
def addArriendo(request):
    if request.method == 'POST':
        form = formularioArriendo( request.POST,request.FILES)
        if form.is_valid():
            arriendo = form.save(commit=False)
            arriendo.save()
            pk=arriendo.pk
            #return render(request, 'mobike/ficha-cliente.html', )
            #return redirect('cliente/', pk)
            return render_to_response('mobike/main.html')
    else:
        form = formularioArriendo()
    context = {'form':form}
    return render(request, 'mobike/registro-Arriendo.html',context)