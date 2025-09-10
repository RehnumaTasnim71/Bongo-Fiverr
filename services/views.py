
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Service
from .forms import ServiceForm


def service_list(request):
    services = Service.objects.all()
    category = request.GET.get('category')
    sort = request.GET.get('sort')
    if category:
        services = services.filter(category=category)
    if sort == 'price_asc':
        services = services.order_by('price')
    elif sort == 'price_desc':
        services = services.order_by('-price')
    context = {'services': services, 'categories': Service.CATEGORY_CHOICES}
    return render(request, 'services/service_list.html', context)

def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'services/service_detail.html', {'service': service})

@login_required
@login_required
def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save(commit=False)
            service.seller = request.user
            service.save()
            messages.success(request, 'Service posted successfully!')
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'services/service_form.html', {'form': form})

@login_required
def service_update(request, pk):
    service = get_object_or_404(Service, pk=pk)

    # Only the seller can update
    if request.user != service.seller:
        messages.error(request, "You are not authorized to update this service.")
        return redirect('service_list')

    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, "Service updated successfully!")
            return redirect('service_detail', pk=service.id)
    else:
        form = ServiceForm(instance=service)

    return render(request, 'services/service_update.html', {
        'form': form,
        'service': service  
    })

@login_required
def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.user != service.seller:
        messages.error(request, "You are not authorized to delete this service.")
        return redirect('service_list')

    if request.method == 'POST':
        service.delete()
        messages.success(request, "Service deleted successfully!")
        return redirect('service_list')
    return render(request, 'services/service_confirm_delete.html', {'service': service})