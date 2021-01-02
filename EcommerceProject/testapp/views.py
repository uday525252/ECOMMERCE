from django.shortcuts import render,redirect
from django.views.generic import DetailView
from testapp.models import Product
from testapp.forms import ConfirmationForm

# Create your views here.

def read_data(request):
    product_list=Product.objects.all()

    item_name=request.GET.get('item_name')#laptop
    if item_name!='' and item_name is not None:
        product_list=product_list.filter(name__contains=item_name)



    my_dict={'product_list':product_list}
    return render(request,"welcome.html",my_dict)


class Read_One_Data(DetailView):
    model=Product
    #default template name:product_detail.html
    #default context variable:product or object



def confirm_view(request):
    form=ConfirmationForm()
    my_dict={'form':form}

    if request.method=='POST':
        form=ConfirmationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return redirect('/success')


    return render(request,"order.html",my_dict)


def successful_view(request):
    return render(request,"success.html")

def order(request):
    if request.method=='POST':
        order_amount = 50000
        order_currency = 'INR'
        client=razorpay.Client(auth=('rzp_test_6NoFgUCfE30f1c','cwQ6xkJPQ1ZZcU5f9rM19BGT'))

        
   # OPTIONALclient.order.create(amount=order_amount, currency=order_currency, receipt=order_receipt, notes=notes)
    return render(request,"order.html")
