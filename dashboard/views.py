from django.shortcuts import render, redirect
from .models import userdb, noname
from .forms import user_registry

# returns a form page for uploading images and stores responses in the form to imgdb database
# If a get request to the URL is made, a blank form is rendered
def index(request):
    if request.method == 'POST':
        form = user_registry(request.POST)
        if form.is_valid():
            saveRes = form.save()
    else:
        form = user_registry()
    return render(request, 'dashboard/index.html', {
        'form' : form
    })

# pulls out the last entry in the imgdb database and displays the images in the "image_list/" URL
def gallery_display(request):
    images = imgdb.objects.last()
    image_files = noname.objects.filter(sequence = images.id)
    context = []
    for file in image_files:
        context.append(file)

    return render(request, 'dashboard/display.html', {'image_files' : context,
                                                      'title' : images.title,
                                                      'description' : images.description
                                                      })
