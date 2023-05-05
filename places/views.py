from django.shortcuts import render


def main_page(request):
    return render(request, 'main_page.html')


def main_page_map(request):
    return render(request, 'main_page_map.html')
