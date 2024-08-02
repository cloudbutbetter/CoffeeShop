from django.shortcuts import render,redirect # type: ignore
from .models import Coffee,Order
# Create your views here.
def home(request):

    return render(request,'home.html')

def manage(request):
    context = Coffee.objects.all()
    return render(request, 'manage.html', {'coffees': context})

def menu(request):
    menu_obj=Coffee.objects.all()
    context={'Menus':menu_obj}
    return render(request,'menu.html',context)


def add(request):
    if request.method=="POST":
        image=request.FILES.get('image')
        name=request.POST.get("name")
        description=request.POST.get("description")
        price=request.POST.get('price')
        Coffee.objects.create(name=name,description=description,image=image,price=price)
        return redirect('/menu')
    return render(request,'add.html')


def delete0(request, pk):
    menu_obj=Coffee.objects.get(id=pk)
    menu_obj.delete()
    return redirect('manage')


def delete(request, pk):
    order_obj=Order.objects.get(id=pk)
    order_obj.delete()
    return redirect('customer')

def order(request,pk):
    order_obj=Coffee.objects.get(id=pk)
    context={'order':order_obj}
    if request.method=='POST':
        # Get the new data from the request
        image = request.FILES.get('image', order_obj.image)  # Keeping existing image if no new one is provided
        title = request.POST.get("title")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")
        customer = request.POST.get("customer")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        address = request.POST.get("address")
        Order.objects.create(image=image,title=title,price=price,quantity=quantity,customer=customer,phone=phone,email=email,address=address)
        return redirect('order',pk=pk)
    return render(request,'order.html',context)


def edit(request,pk):
    coffee=Coffee.objects.get(id=pk)
    context={'menu':coffee}
    if request.method == 'POST':
        # Update the Coffee object with new data
        coffee.name = request.POST.get('name')
        coffee.description = request.POST.get('description')
        coffee.price = request.POST.get('price')
        
        # Handle file upload
        if 'image' in request.FILES:
            coffee.image = request.FILES['image']

        # Save the updated Coffee object
        coffee.save()
        return redirect('manage')
    return render(request,'edit.html',context)


def customer(request):
    context = Order.objects.all()
    return render(request, 'customer.html', {'Orders': context})
