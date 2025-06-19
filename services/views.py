from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import MarkCompletedForm, RequestServiceForm
from services.models import Service
from devices.models import Device
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def mark_completed(request, pk):
    service = get_object_or_404(Service, pk=pk)

    if request.method == 'POST':
        form = MarkCompletedForm(request.POST, instance=service)
        if form.is_valid():
            service = form.save(commit=False)
            service.status = 'finished'
            service.end_date = timezone.now().date()
            service.save()
            messages.success(request, f"Service #{service.id} for {service.device} marked as COMPLETED.")
            return redirect('technician_all_requests')
    else:
        form = MarkCompletedForm(instance=service)

    return render(request, 'services/mark_completed.html', {
        'form': form,
        'service': service
    })
    
@login_required   
def mark_uncompleted(request, pk):
    service = get_object_or_404(Service, pk=pk)

    # Optional: only allow reverting finished services
    if service.status == 'finished':
        service.status = 'pending'
        service.end_date = None  # Optional: clear end_date
        service.save()
        messages.success(request, f"Service #{service.id} for {service.device} marked as pending.")
    else:
        messages.warning(request, "Only finished services can be marked as uncompleted.")

    return redirect('technician_all_services')


@login_required
def request_service(request, device_id):
    device = get_object_or_404(Device, id=device_id, user=request.user)

    if request.method == 'POST':
        form = RequestServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.device = device
            service.user = request.user
            service.request_date = timezone.now()
            service.status = 'requested'
            service.service_type = 'R'
            service.save()
            messages.success(request, 'Service request submitted successfully.')
            return redirect('client_my_devices')
    else:
        form = RequestServiceForm()

    return render(request, 'services/client_request_service.html', {
        'form': form,
        'device': device,
    })
    

@login_required
def cancel_service_request(request, service_id):
    service = get_object_or_404(Service, id=service_id, user=request.user)

    if service.status in ['requested', 'pending']:
        service.status = 'canceled'
        service.save()
        messages.success(request, 'Your service request has been canceled.')
    else:
        messages.error(request, 'Only requested or pending services can be canceled.')

    return redirect('client_requests')