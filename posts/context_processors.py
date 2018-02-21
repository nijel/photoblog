from .models import Category

def context(request):
    return {
        'categories': Category.objects.all(),
    }
