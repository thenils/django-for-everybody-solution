from django.shortcuts import render, redirect, get_object_or_404
from .models import Breed, Cat
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from cats.forms import BreedForm
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class CatView(LoginRequiredMixin, View) :
    def get(self, request):
        mc = Cat.objects.all()
        

        ctx = { 'cats': mc};
        return render(request, 'cats/main.html', ctx)


class BreedView(LoginRequiredMixin, View) :
    def get(self, request):
        bd = Breed.objects.all()
        

        ctx = { 'breeds': bd};
        return render(request, 'cats/breed_views.html', ctx)


class BreedCreate(LoginRequiredMixin, View):
	template = 'cats/breed_create.html'
	success_url = reverse_lazy('all-cat')
	def get(self, request):
		form = BreedForm()
		ctx = { 'form' : form}
		return render(request, self.template, ctx)

	def post(self, request):
		form = BreedForm(request.POST)
		if not form.is_valid():
			ctx = {'form' : form}
			return render(request, self.template, ctx)
		breeds = form.save()
		return redirect(self.success_url) 

class BreedUpdate(LoginRequiredMixin, View):
	template = 'cats/breed_create.html'
	success_url = reverse_lazy('all-cat')

	def get(self, request, pk):
		breed = get_object_or_404(Breed, pk=pk)
		form = BreedForm(instance=breed)
		ctx = { 'form': form }
		return render(request, self.template, ctx)

	def post(self, request, pk):
		breed = get_object_or_404(Breed, pk=pk)
		form = BreedForm(request.POST, instance = breed)
		if not form.is_valid():
			ctx = {'form':form}
			return render(request, self.template, ctx)
		form.save()
		return redirect(self.success_url)
        
        
class BreedDelete(LoginRequiredMixin, View):
    model = Breed
    success_url = reverse_lazy('all-cat')
    template = 'cats/breed_confirm_delete.html'

    def get(self, request, pk) :
        breed = get_object_or_404(self.model, pk=pk)
        form = BreedForm(instance=breed)
        ctx = { 'breeds': breed }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        breeds = get_object_or_404(self.model, pk=pk)
        breeds.delete()
        return redirect(self.success_url)
        
        

      

class CatCreate(LoginRequiredMixin,CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('all-cat')

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('all-cat')

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('all-cat')            
            

        
        


# def home(request):
# 	context = {
# 	'cats' : Cat.objects.all()
# 	}
# 	return render(request, 'cats/main.html',context)

