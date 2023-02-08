from django.shortcuts import redirect, render
import datetime
from .models import Category, Employee,Login, Order
from .forms import EmployeeForm, LoginForm
from rest_framework.decorators import api_view



from rest_framework import status




from rest_framework.response import Response



from django.http.response import JsonResponse


from .serializers import CategorySerializers, EmployeeSerializers,OrderSerializers



from django.contrib import messages

def index(request):
    return render(request, 'HomePage.html')


def AdminHomePage(request):
    return render(request, 'admin/AdminHomePage.html')


def employeehome(request):
    return render(request, 'employee/employeehome.html')

def hodhome(request):
    return render(request, 'hod/hodhome.html')




def LogOut(request):
    return render(request, 'LogOut.html')


def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/AdminHomePage')

    else:
        form = EmployeeForm()
    return render(request, 'admin/add_employee.html', {'form': form})

def view_employee(request):
    employee = Employee.objects.all()
    print("data:")
    return render(request, "admin/view_employee.html", {'employee': employee})




def edit_employee(request,id):
    employee=Employee.objects.get(id=id)
    return render(request,"admin/edit_vehicle.html",{'employee':employee})



def update_vehicle(request, id):
    employee = Employee.objects.get(id=id)
    print(id)
    form = EmployeeForm(request.POST,instance=employee)
    if form.is_valid():
        form.save()
        return redirect("../view_vehicle")
    return render(request, 'admin/edit_vehicle.html', {'employee': employee})


def delete_employee(request, id):
    vehicle = Employee.objects.get(id=id)
    vehicle.delete()
    return redirect('../view_employee')



def breakfast(request):
    if request.method == "POST":
        cid=request.session['uid']
        category_name ='Breakfast'
        user_id =cid
        guest='null'
        quantity=1
        guest_name='null'
        date= datetime.date.today()
        servingtype=request.POST['servingtype']
        data = Order(category_name=category_name,user_id=user_id, guest=guest,quantity=quantity,servingtype=servingtype,guest_name=guest_name,date=date)
        data.save()
        return redirect("/employeehome")
    return render(request,'employee/parselordinning.html')


def lunch(request):
    if request.method == "POST":
        cid=request.session['uid']
        category_name ='Lunch'
        user_id =cid
        guest='null'
        quantity=1
        guest_name='null'
        date= datetime.date.today()
        servingtype=request.POST['servingtype']
        data = Order(category_name=category_name,user_id=user_id, guest=guest,quantity=quantity,servingtype=servingtype,guest_name=guest_name,date=date)
        data.save()
        return redirect("/employeehome")
    return render(request,'employee/parselordinning.html')


def dinner(request):
    if request.method == "POST":
        cid=request.session['uid']
        category_name ='Dinner'
        user_id =cid
        guest='null'
        quantity=1
        guest_name='null'
        date= datetime.date.today()
        servingtype=request.POST['servingtype']
        data = Order(category_name=category_name,user_id=user_id, guest=guest,quantity=quantity,servingtype=servingtype,guest_name=guest_name,date=date)
        data.save()
        return redirect("/employeehome")
    return render(request,'employee/parselordinning.html')



def View_all_order(request):
    ord=Order.objects.all()
    if request.method=='POST':
        nm=request.POST['date']
        print(nm)
        pd=Order.objects.filter(date=nm)
        print(pd)
        return render(request,"admin/View_all_order.html", {'p':pd,'n':nm})
    return render(request,"admin/View_all_order.html",{'or':ord})


#------------------------------------------employeepage--------------------------------------------------------#



def view_category_emp(request):
    return render(request, 'employee/view_category_emp.html')




def login(request):
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form['username'].value()
                password = form['password'].value()

                try:
                    request.session['uid']=username
                    user = Login.objects.get(username=username, password=password)
                    if user is not None:
                        LoginForm(request, user)
                        messages.info(request, f"You are now logged in as {username}.")
                        return redirect("/AdminHomePage")
                except :
                    pass
                try:
                    user = Employee.objects.get(username=username,password=password,designation='WORKER')
                    print(user)
                    if user is not None:
                        print(user)
                        request.session['cid']=user.id

                        return redirect("/employeehome")
                except :
                    pass
                try:
                    user = Employee.objects.get(username=username, password=password,designation='HOD')
                    if user is not None:
                        request.session['cid']=user.id
                        return redirect("/hodhome")
                except :
                    pass


            else:
                messages.error(request, "Invalid username or password.",message=messages)
        form = LoginForm()
        return render(request,'login.html', {'form': form})


def Ordering_item(request, id):
    if request.method == "POST":
        cid=request.session['cid']
        category_name =id
        user_id = cid
        guest='null'
        quantity=request.POST['quantity']
        data = Order(category_name=category_name, user_id=user_id, guest=guest,quantity=quantity)
        data.save()
        return redirect("/employeehome")
    else:

        request.session['cid'] = id
    return render(request, 'employee/Ordering_item.html', {'id': id})



def Ordering_item_hod(request, id):
    cid=request.session['cid']
    if request.method == "POST":
        category_name =id
        user_id = cid
        guest='null'
        quantity=request.POST['quantity']
        data = Order(category_name=category_name, user_id=user_id, guest=guest,quantity=quantity)
        data.save()
        return redirect("/hodhome")
    else:
        request.session['cid'] = id

    return render(request, 'hod/Ordering_item_hod.html', {'id': id})

def view_category_Hod(request):
    employee = Category.objects.all
    return render(request, 'hod/view_category_Hod.html',{'employee': employee})

def view_category_Guest(request):
    employee = Category.objects.all
    return render(request, 'hod/view_category_Guest.html',{'employee': employee})

def Ordering_item_guest(request,id):
    cid=request.session['cid']
    if request.method == "POST":
        category_name =id
        user_id = cid
        guest=request.POST['guest']
        quantity=request.POST['quantity']
        data = Order(category_name=category_name, user_id=user_id, guest=guest,quantity=quantity)
        data.save()
        return redirect("/hodhome")
    else:
        request.session['cid'] = id

    return render(request, 'hod/Ordering_item_guest.html', {'id': id})




def breakfast_hod(request):
    if request.method == "POST":
        cid=request.session['uid']
        category_name ='Breakfast'
        user_id =cid
        guest='null'
        quantity=1
        guest_name='null'
        date= datetime.date.today()
        servingtype=request.POST['servingtype']
        data = Order(category_name=category_name,user_id=user_id, guest=guest,quantity=quantity,servingtype=servingtype,guest_name=guest_name,date=date)
        data.save()
        return redirect("/hodhome")
    return render(request,'hod/parselordinning.html')


def lunch_hod(request):
    if request.method == "POST":
        cid=request.session['uid']
        category_name ='Lunch'
        user_id =cid
        guest='null'
        quantity=1
        guest_name='null'
        date= datetime.date.today()
        servingtype=request.POST['servingtype']
        data = Order(category_name=category_name,user_id=user_id, guest=guest,quantity=quantity,servingtype=servingtype,guest_name=guest_name,date=date)
        data.save()
        return redirect("/hodhome")
    return render(request,'hod/parselordinning.html')


def dinner_hod(request):
    if request.method == "POST":
        cid=request.session['uid']
        category_name ='Dinner'
        user_id =cid
        guest='null'
        quantity=1
        guest_name='null'
        date= datetime.date.today()
        servingtype=request.POST['servingtype']
        data = Order(category_name=category_name,user_id=user_id, guest=guest,quantity=quantity,servingtype=servingtype,guest_name=guest_name,date=date)
        data.save()
        return redirect("/hodhome")
    return render(request,'hod/parselordinning.html')


def breakfast_guest(request):
    if request.method == "POST":
        cid=request.session['uid']
        category_name ='Breakfast'
        user_id =cid
        guest=request.POST['guest']
        quantity=request.POST['quantity']
        servingtype=request.POST['servingtype']
        guest_name=request.POST['guest_name']
        date= datetime.date.today()
        data = Order(category_name=category_name,user_id=user_id, guest=guest,quantity=quantity,servingtype=servingtype,guest_name=guest_name,date=date)
        data.save()
        return redirect("/hodhome")
    return render(request,'hod/parselordinning_guest.html')


def lunch_guest(request):
    if request.method == "POST":
        cid=request.session['uid']
        category_name ='Lunch'
        user_id =cid
        guest=request.POST['guest']
        quantity=request.POST['quantity']
        servingtype=request.POST['servingtype']
        guest_name=request.POST['guest_name']
        date= datetime.date.today()
        data = Order(category_name=category_name,user_id=user_id, guest=guest,quantity=quantity,servingtype=servingtype,guest_name=guest_name,date=date)
        data.save()
        return redirect("/hodhome")
    return render(request,'hod/parselordinning_guest.html')


def dinner_guest(request):
    if request.method == "POST":
        cid=request.session['uid']
        category_name ='Dinner'
        user_id =cid
        guest=request.POST['guest']
        quantity=request.POST['quantity']
        servingtype=request.POST['servingtype']
        guest_name=request.POST['guest_name']
        date= datetime.date.today()
        data = Order(category_name=category_name,user_id=user_id, guest=guest,quantity=quantity,servingtype=servingtype,guest_name=guest_name,date=date)
        data.save()
        return redirect("/hodhome")
    return render(request,'hod/parselordinning_guest.html')


def view_chart(request):
    lebels=[]
    data=[]
    queryset=Order.objects.order_by('-category_name')[:5]
    for a in queryset:
        lebels.append(a.quantity)
        data.append(a.category_name)

    return render(request,'admin/view_chart.html',{'lebels':lebels,'data':data})


@api_view(['POST'])
def signup(request):
    data = request.data
    username=data['username']
    password=data['password']        
    try:
        user=Employee.objects.get(username=username,password=password,designation='WORKER')
        serializer = EmployeeSerializers(user,many=False)
        if user is not None:
            return JsonResponse(serializer.data)
              
    except:
        pass  
      
    try:

        note=Employee.objects.get(username=username,password=password,designation='HOD')
        serializer = EmployeeSerializers(note,many=False)
        return JsonResponse(serializer.data)
    except:
        pass  




@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'list':'/job-category/',
        'detial view':'/job-detials/<int:id>',
        'create':'/category-create/',
        'update':'/category-update/<int:id>',
        'delete':'/category-delete/<int:id>',
    }
    return JsonResponse(api_urls);

@api_view(['GET'])
def Showall(request):
    category=Category.objects.all()
    serializer=CategorySerializers(category, many=True)
    return JsonResponse({"categories": serializer.data}, safe=False, status=status.HTTP_200_OK)

@api_view(['GET'])
def Detialview(request,pk):
    category=Category.objects.get(id=pk)
    serializer=CategorySerializers(category, many=False)
    return JsonResponse({"categories": serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(['POST'])
def Employeecreate(request):
    serializer=EmployeeSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        data = {}
        data['response'] = ' Employee Added'
    
    else:
        data = serializer.errors
        
    return Response(data, status=status.HTTP_200_OK)  

 
@api_view(['GET'])
def Showall_Employee(request):
    category=Employee.objects.all()
    serializer=EmployeeSerializers(category, many=True)
    return JsonResponse({"Employees": serializer.data}, safe=False, status=status.HTTP_200_OK)



@api_view(['GET'])
def Showall_Orders(request):
    order=Order.objects.all()
    serializer=OrderSerializers(order, many=True)
    return JsonResponse({"Reports": serializer.data}, safe=False, status=status.HTTP_200_OK)



@api_view(['POST'])
def api_Breakfast(request):
    serializer=OrderSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        data = {}
        data['response'] = ' Breakfast Added'
    
    else:
        data = serializer.errors
        
    return Response(data, status=status.HTTP_200_OK)  



@api_view(['POST'])
def api_Lunch(request):
    serializer=OrderSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        data = {}
        data['response'] = ' Lunch Added'
    
    else:
        data = serializer.errors
        
    return Response(data, status=status.HTTP_200_OK)  


@api_view(['POST'])
def api_Dinner(request):
    serializer=OrderSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        data = {}
        data['response'] = ' Dinner Added'
    
    else:
        data = serializer.errors
        
    return Response(data, status=status.HTTP_200_OK)  









