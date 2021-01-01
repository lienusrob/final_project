from .models import ItemsCategory

def cat_list(request): 
    list = ItemsCategory.objects.all()