from django.shortcuts import render
from users.models import CustomUser
from services.models import Service
from devices.models import Device
from django.contrib.auth.decorators import login_required


@login_required
def technician_dashboard(request):
    num_clients = CustomUser.objects.filter(role='client').count()
    num_devices = Device.objects.count()
    awaiting_services = Service.objects.filter(status__in=['pending', 'requested']).count()
    finished_services = Service.objects.filter(status='finished').count()
    
    
    context = {
        'num_clients': num_clients,
        'num_devices': num_devices,
        'awaiting_services': awaiting_services,
        'finished_services': finished_services,
    }

    return render(request, 'users/tech_dashboard.html', context)

@login_required
def technician_all_devices(request):
    query = request.GET.get('q')
    devices = Device.objects.all().order_by('-installation_date')
    
    if query:
        devices = Device.objects.filter(serial_number__icontains = query)
    return render(request, 'users/tech_all_devices.html', {'devices': devices, 'query': query} )


@login_required
def technician_all_requests(request):
    awaiting_services = Service.objects.filter(status__in=['pending', 'requested']).order_by('-request_date')
    
    return render(request, 'users/tech_all_requests.html', {'awaiting_services': awaiting_services} )

@login_required
def technician_all_services(request):
    all_services = Service.objects.filter(status='finished').order_by('-end_date')
    
    return render(request, 'users/tech_all_services.html', {'all_services': all_services} )


@login_required
def client_dashboard(request):
    user = request.user
    
    my_devices = Device.objects.filter(user=user).count()
    awaiting_services = Service.objects.filter(user=user, status='pending').count()
    finished_services = Service.objects.filter(user=user, status='finished').count()
    
    
    context = {
        'my_devices': my_devices,
        'awaiting_services': awaiting_services,
        'finished_services': finished_services,
    }

    return render(request, 'users/client_dashboard.html', context)
        
        
@login_required
def client_my_devices(request):
    user = request.user
    
    devices = Device.objects.filter(user=user).order_by('-installation_date')
    
    return render(request, 'users/client_my_devices.html', {'devices': devices} )