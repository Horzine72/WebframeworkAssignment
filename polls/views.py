from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import Invoice
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import InvoiceForm
from .models import Customertable

@login_required
def view_invoices(request):
    customer_id = request.user.id
    invoices = Invoice.objects.filter(customer_id=customer_id)
    return render(request, 'invoices.html', {'invoices': invoices})



def main(request):
    return render(request, 'main.html')


def login_view(request):
    if not request.user.is_authenticated and 'next' in request.GET:
        messages.info(request, 'Please log in to access this page.')

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(request, username=user_obj.username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {user.username}!')
                next_url = request.GET.get('next', '/polls/main/')
                return redirect(next_url)
            else:
                messages.error(request, 'Invalid email or password.')
        except User.DoesNotExist:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'login.html')





def logout_view(request):
    logout(request)
    return redirect('/polls/main/')

def invoice(request):
    return render(request, 'invoice.html')


def tracking(request):
    return render(request, 'tracking.html')


def contact(request):
    return render(request, 'contact.html')


def help(request):
    return render(request, 'help.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already registered.')
            else:

                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()


                Customertable.objects.create(
                    CustomerID=user.id,
                    Name=username,
                    Email=email,
                    Password=user.password,
                    Date=user.date_joined
                )

                messages.success(request, 'Account created successfully! You can now log in.')
                return redirect('/polls/login/')
        else:
            messages.error(request, 'Passwords do not match.')

    return render(request, 'register.html')





@permission_required('polls.can_add_invoice', login_url='/polls/login/')
def add_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()  #Saves invoice to database
            return redirect('/polls/invoices/manage/')
    else:
        form = InvoiceForm()

    return render(request, 'add_invoice.html', {'form': form})



#ONLY for staff/superuser
@user_passes_test(lambda u: u.is_staff or u.is_superuser, login_url='/polls/login/')
@login_required
def manage_invoices(request):
    invoices = Invoice.objects.all()  # Retrieve all invoices
    return render(request, 'manage_invoices.html', {'invoices': invoices})