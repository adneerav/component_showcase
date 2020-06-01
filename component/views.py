from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import render, get_list_or_404

# Create your views here.
from component.models import Component, Detail
from technology.models import Technology


def home(request):
    data = {
        "technology_list": _get_technology(),
        "components": _get_components(),
    }
    if request.is_ajax():
        return render(request, "components/list_item.html", context=data)
    else:
        return render(request, 'components/home.html', context=data)


def search(request):
    if request.method == 'POST':
        search_text = request.POST["txt_search_query"]
        qs_search_result = Detail.objects.filter \
            (Q(description__icontains='{}'.format(search_text))
             | Q(component__name__icontains='{}'.format(search_text))
             | Q(language__name__icontains='{}'.format(search_text))
             | Q(technology__name__icontains='{}'.format(search_text))).distinct()
        response_data = {
            "components": qs_search_result,
            'is_technology_wise': False,
            'search_text': search_text,
            "title": ("Search %s", search_text),
        }
        return render(request, 'components/components_page.html', context=response_data)
    else:
        return PermissionDenied


def components(request, name):
    print(name)
    if request.is_ajax():
        query_set_result = _get_components() if name.lower() == 'all' else _get_technology_components(
            technology_name=name)
        qs_component_all = {
            "components": query_set_result,
            "title": "{} Components".format(name)
        }
        return render(request, "components/list_item.html", context=qs_component_all)
    else:
        qs_component_all = {
            "components": _get_technology_components(technology_name=name),
            'is_technology_wise': True,
            'technology_detail': _get_technology_detail(technology_name=name),
            "title": "{} Components".format(name)
        }
        return render(request, 'components/components_page.html', context=qs_component_all)


def component_list(request):
    qs_component_all = {
        "components": _get_components(),
        'is_technology_wise': False,
        "title": "All Components"
    }
    return render(request, 'components/components_page.html', context=qs_component_all)


def detail_by_id(request, component_id):
    if request.method == 'GET':
        print(component_id)  # component_data
        component_detail = Detail.objects.get(pk=component_id)
        language_list = component_detail.language.all()
        data = {
            "detail": component_detail,
            "languages": language_list,
            "dev_detail": {
                "name": "John",
                "nickname": "Jimmy",
                "team": "Yo Yo"
            }
        }
        return render(request, 'components/detail.html', data)
    else:
        raise PermissionDenied


def detail(request):
    if request.method == 'POST':
        component_id = request.POST["btn_component_detail"];
        print(request.POST["btn_component_detail"])  # component_data
        component_detail = Detail.objects.get(pk=component_id)
        language_list = component_detail.language.all()
        data = {
            "detail": component_detail,
            "languages": language_list,
            "dev_detail": {
                "name": "John",
                "nickname": "Jimmy",
                "team": "Yo Yo"
            }
        }
        return render(request, 'components/detail.html', data)
    else:
        raise PermissionDenied


def _get_technology_components(technology_name):
    qs_tech_components = get_list_or_404(Detail, technology__name__iexact=technology_name)
    return qs_tech_components


def _get_technology_detail(technology_name):
    technology_detail = Technology.objects.get(name=technology_name)
    return technology_detail


def _get_components():
    qs_comp_list = Detail.objects.all()
    return qs_comp_list


def _get_technology():
    qs_technologies = Technology.objects.all()
    return qs_technologies
