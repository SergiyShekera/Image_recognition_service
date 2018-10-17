from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.http import HttpResponse
from PIL import Image
from .services import get_avg_rgb_img



def Upload_File(request):


    if request.method == 'POST':

        r = request.FILES['image']

        image = Image.open(r)

        width = image.size[0]
        height = image.size[1]

        avg_color = get_avg_rgb_img(image, width, height)

        content = {'width' : width,
                   'height': height,
                   'avg_color': avg_color}

        return HttpResponse(render(request, 'index.html', {'content': content}))

    else:
        return HttpResponse(render(request, 'index.html'))



