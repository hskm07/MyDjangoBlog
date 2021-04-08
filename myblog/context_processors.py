from .models import Category

def common(request):
    """
        Data to pass to the template
    """
    context = {
        'category_list' : Category.objects.all(),
    }
    return context
