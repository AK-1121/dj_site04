from django.shortcuts import redirect, render
from lists.models import Item, List

# Create your views here.
def home_page(request):
    # Second condition controls that input text is not empty:
    
    if request.method == 'POST' and request.POST['item_text']:
        list_ = List.objects.create()
        Item.objects.create(text=request.POST['item_text'], list=list_)
        return redirect('/lists/the-only-common-list/')
        

    return render(request, 'lists/home.html')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'lists/list.html', {'items': items})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/the-only-common-list/')

