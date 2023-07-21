from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Computer, ComputerSpecification, ComputerBrand

# Create your views here.
def index(request):
    return render(request,'index.html')
    # return HttpResponse("Index")

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
    # totalPrice = 0.0

    # if request.method == 'POST':
    #     computerCode = request.POST.get('computerCode')
    #     specificationId = request.POST.get('specificationId')
      
    #     quantity = request.POST.get('quantity')
    #     unitPrice = request.POST.get('unitPrice')
    #     totalPrice = float(quantity)*float(unitPrice)
    
    #     specification = ComputerSpecification.objects.filter(id=specificationId)[0]
    #     saveData = Computer(id = id,computer_code=computerCode, specification= specification, quantity=quantity, unit_rate=unitPrice, total_price = totalPrice,)
        
    #     saveData.save()
    
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
        
        obj = Computer.objects.get(id=id)
        image_url= obj.image
        
        files = request.FILES.getlist('files')
        for file in files:
            if(file!=''):
                image_to_delete = Computer.objects.get(id = id).image
                image_to_delete.delete()
                image_url = file
            print(image_url)
        
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

def delete_image(request, pk):
    if request.method =='POST':
        image_to_delete = Computer.objects.get(id = pk).image
        image_to_delete.delete()
        return render(request, 'base.html')

