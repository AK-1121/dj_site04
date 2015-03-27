from django.shortcuts import redirect, render
from lists.models import Item

# Create your views here.
def home_page(request):
    # Second condition controls that input text is not empty:
    if request.method == 'POST' and request.POST['item_text']:
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    
    items = Item.objects.all()
    return render(request, 'lists/home.html', {'items': items})
