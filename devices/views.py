from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import DeviceForm
from django.contrib.auth.decorators import login_required
from .models import Device


@login_required
def add_device(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            device = form.save()
            messages.success(request, 'Device added succesfuly.')
            return redirect('technician_all_devices')
    else:
        form = DeviceForm()
    
    return render(request, 'devices/add_device.html', {'form': form })

@login_required
def delete_device(request, pk):
    device = get_object_or_404(Device, pk=pk)
    
    if request.method == 'POST':
        device.delete()
        messages.success(request, 'Device deleted succesfuly.')
        return redirect('technician_all_devices')
    
    return render(request, 'devices/confirm_delete.html', {'device': device})

def edit_device(request, pk):
    device = get_object_or_404(Device, pk=pk)

    if request.method == 'POST':
        form = DeviceForm(request.POST, instance=device)
        if form.is_valid():
            form.save()
            messages.success(request, 'Device updated successfully.')
            return redirect('technician_all_devices')  # Adjust if needed
    else:
        form = DeviceForm(instance=device)

    return render(request, 'devices/edit_device.html', {'form': form, 'device': device})
