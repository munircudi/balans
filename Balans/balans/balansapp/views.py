from django.http import HttpResponse
from django.shortcuts import render

data = {
    "marka":[
        {
            "title": "marka adı 1",
            "description": "marka açıklama 1",
            "imageUrl": "service_img1.png",
            "slug": "marka-adi-1",

        },
        {
            "title": "marka adı 2",
            "description": "marka açıklama 2",
            "imageUrl": "service_img2.png",
            "slug": "marka-adi-2",

        },
        {
            "title": "marka adı 3",
            "description": "marka açıklama 3",
            "imageUrl": "service_img3.png",
            "slug": "marka-adi-3",

        },
        {
            "title": "marka adı 4",
            "description": "marka açıklama 4",
            "imageUrl": "service_img4.png",
            "slug": "marka-adi-4",

        }

    ]
}


# Create your views here.
def index(request):
    marka = data["marka"]

    return render(request, 'index.html', {
        "marka": marka
    })


def balansapp(request):
    return render(request, 'markalar.html')


def balansapp_details(request, slug):
    return render(request, 'markalar-details.html')


def about(request):
    return render(request, 'about.html')
