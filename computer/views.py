from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Computer, ComputerSpecification, ComputerBrand

# Create your views here.
from django.http import HttpResponse
from django.views import View

# class MyView(View):
#     def get(self, request):
#         # <view logic>
#         return HttpResponse('result')

def index(request):
    return render(request,'index.html')
    # return render(request,'nav.html')

def createList(request):
    totalPrice = 0.0
    message=''
    computerCode = 0
    quantity=1

    temp = ComputerSpecification.objects.all()
    specifications = []
    for specification in temp:
        specifications.append({"id": specification.id, "generation": specification.generation,})

    if request.method == 'POST':
        files = request.FILES.getlist('files')
        computerCode = request.POST.get('computerCode')
        specificationId = request.POST.get('specificationId')
      
        quantity = request.POST.get('quantity')
        unitPrice = request.POST.get('unitPrice')
        totalPrice = float(quantity)*float(unitPrice)
        for file in files:
            image_url = file
        specification = ComputerSpecification.objects.filter(id=specificationId)[0]
        price_min = ComputerSpecification.objects.filter(id=specificationId)[0].price_min
        price_max= ComputerSpecification.objects.filter(id=specificationId)[0].price_max
        if float(unitPrice) >= price_min and float(unitPrice) <= price_max:
            saveData = Computer(computer_code=computerCode, specification= specification, quantity=quantity, unit_rate=unitPrice, total_price = totalPrice, image=image_url)
            
            
            saveData.save()
            message='Data successfully added!'
            
        else:
            print("Invalid Unit Price!")
            message='Price Out of Range.'
            return render(request, 'create.html', {"specifications":specifications, 'message': message, 'computer_code': computerCode, 'quantity': quantity,})
    

    return render(request,'create.html', {"specifications":specifications, "total_price": totalPrice,'message': message})



def updateList(request, id):
    temp = ComputerSpecification.objects.all()
    specifications = []
    for specification in temp:
        specifications.append({"id": specification.id, "generation": specification.generation})

    try:
        current_specification = Computer.objects.get(pk=id)
    except Computer.DoesNotExist:
        raise Http404("The model does not exist")
    return render(request, 'update.html', {"specifications":specifications, "current_specification":current_specification})


def updated(request, id):
    if request.method == 'POST':
        
        obj = ComputerSpecification.objects.get(id=id)
        obj.computerCode = request.POST.get('computerCode')
        obj.quantity = request.POST.get('quantity')
        specificationId = request.POST.get('specificationId')
        
        obj.unitPrice = request.POST.get('unitPrice')
        totalPrice = float(obj.quantity)*float(obj.unitPrice)
    
        specification = ComputerSpecification.objects.filter(id=specificationId)[0]
        saveData = Computer(id = id,computer_code=obj.computerCode, specification= specification, quantity=obj.quantity, unit_rate=obj.unitPrice, total_price = totalPrice,  image = image_url)
        saveData.save()
    return render(request, "updateMessage.html")

def viewList(request):
    temp = Computer.objects.all()
    paginator = Paginator(temp,3 )
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    detail_list = []
    for data in temp:
        detail_list.append({'id': data.id,'computer_code': data.computer_code, 'specification': data.specification, 'quantity': data.quantity,'unit_rate': data.unit_rate,'total_price': data.total_price})
    
    return render(request, 'viewList.html', {'detail_list': detail_list, 'page_obj': page_obj})



def create_brand(request):
    if request.method == 'POST':
        print("Button clicked")
        brand_logo = request.FILES.getlist('brand_logo')
        brand_name = request.POST.get('brand_name')
        for file in brand_logo:
            logo = file
        saveData = ComputerBrand(brand_name = brand_name, logo = logo)
        saveData.save()
        print("Post successful.")
    return render(request,'create_brand.html')


def view_brand(request):
    temp = ComputerBrand.objects.all()
    paginator = Paginator(temp,3 )
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    detail_list = []
    for data in temp:
        detail_list.append({'id': data.id,'brand_name': data.brand_name, 'brand_logo': data.logo, })
    
    return render(request,'view_brand.html',{'detail_list': detail_list, 'page_obj': page_obj})

def update_brand(request, id):
    temp = ComputerBrand.objects.all()
    specifications = []
    for specification in temp:
        specifications.append({"id": specification.id, "brand_name": specification.brand_name, "brand_logo":specification.logo})

    try:
        current_specification = ComputerBrand.objects.get(pk=id)
    except ComputerBrand.DoesNotExist:
        raise Http404("The model does not exist")
    
    if request.method == 'POST':
        obj = ComputerBrand.objects.get(id=id)
        image_url= obj.logo
        
        files = request.FILES.getlist('brand_logo')
        brand_name = request.POST.get('brand_name')
        for file in files:
            if(file!=''):
                image_to_delete = ComputerBrand.objects.get(id = id).logo
                image_to_delete.delete()
                image_url = file
            print(image_url)
        
        
        saveData = ComputerBrand(id = id,brand_name=brand_name, logo= image_url)
        saveData.save()
        return render(request,'updateMessage.html')
    return render(request, 'update_brand.html',{'current_specification': current_specification})

def add_specification(request):
    
    temp = ComputerBrand.objects.all()
    specifications = []
    for specification in temp:
        specifications.append({"id": specification.id, "brand_name": specification.brand_name,})

    if request.method == 'POST':
        specificationId = request.POST.get('specificationId')
        generation = request.POST.get('generation')
        min_price = request.POST.get('min_price')
      
        max_price = request.POST.get('max_price')
        ram = request.POST.get('ram')

    #    generation min_price max_price ram
        brand = ComputerBrand.objects.filter(id=specificationId)[0]
        print(specification)
        saveData = ComputerSpecification(generation=generation, price_min= min_price, price_max=max_price, ram=ram, brand=brand)
        saveData.save()

    return render(request,'add_specification.html', {"specifications":specifications,})


def view_specification(request):
    temp = ComputerSpecification.objects.all()
    paginator = Paginator(temp,5 )
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    detail_list = []
    for data in temp:
        detail_list.append({'id': data.id, })
    
    return render(request,'view_specification.html',{'detail_list': detail_list, 'page_obj': page_obj})


def update_specification(request, id):
    temp = ComputerBrand.objects.all()
    specifications = []
    for specification in temp:
        specifications.append({"id": specification.id, "brand_name": specification.brand_name,})

    try:
        current_specification = ComputerSpecification.objects.get(pk=id)
    except ComputerSpecification.DoesNotExist:
        raise Http404("The model does not exist")
    
    if request.method == 'POST':
        obj = ComputerSpecification.objects.get(id=id)
        generation = request.POST.get('generation')
        price_min = request.POST.get('min_price')
        price_max = request.POST.get('max_price')
        ram = request.POST.get('ram')
        specificationId = request.POST.get('specificationId')
        specification = ComputerBrand.objects.filter(id=specificationId)[0]
        saveData = ComputerSpecification(id = id,generation=generation, price_min = price_min, price_max=price_max,ram =ram, brand = specification)
        saveData.save()
        return render(request,'updateMessage.html')
    return render(request, 'update_specification.html',{'current_specification': current_specification, 'specifications': specifications})


