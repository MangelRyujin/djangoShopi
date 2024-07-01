from django.shortcuts import render

from apps.general.models import *


def home_view(request):
    header = PrincipalHeader.objects.first()
    contact = Contact.objects.first()
    brands = Brand.objects.all()
    grouped_brands1 = []
    grouped_brands2 = []
    grouped_brands1.append(list(brands[:3]))
    index = 3 
    while index < len(brands):
        grouped_brands2.append(list(brands[index:index+3]))
        index += 3
    print(grouped_brands1)
    print(grouped_brands2)
    social = SocialMedia.objects.first()
    context={
        "header":header,
        "contact":contact,
        "grouped_brands1":grouped_brands1,
        "grouped_brands2":grouped_brands2,
        "social":social
    }
    return render(request,'client_site/index.html',context)