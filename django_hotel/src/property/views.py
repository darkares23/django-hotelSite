from django.shortcuts import render

# Create your views here.
from .models import Property, Category
from .forms import ReserveForm
from django.db.models import Q


def property_list(request):

    property_list = Property.objects.all()
    template = 'property/list.html'
    search_query = request.GET.get('q')
    property_type = request.GET.get('property_type', None)

    if search_query and property_type:
        property_list = property_list.filter(
            Q(name__icontains=search_query) &
            Q(type__icontains=property_type[0]) |
            Q(location__icontains=search_query)
        ).distinct()

    context = {
        'property_list': property_list,
    }

    return render(request, template, context)


def property_detail(request, id):
    property_detail = Property.objects.get(pk=id)
    template = 'property/detail.html'

    if request.method == 'POST':
        reserve_form = ReserveForm(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()
    else:
        reserve_form = ReserveForm()

    context = {
        'property_detail': property_detail,
        'reserve_form': reserve_form
    }
    return render(request, template, context)
