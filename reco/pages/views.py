from django.shortcuts import render,redirect
from .models import Citizen
from address.models import Address

# Create your views here.
def index(request):
    if request.method=="POST":
          first_name=request.POST['first_name']
          last_name=request.POST['last_name']
          email=request.POST['email']
          dob =request.POST["dob"]
          phone =request.POST["Phone"]
          age =  request.POST["Age"]
          gender =request.POST["gender"]
          father_name =request.POST["fathername"]
          mother_name=request.POST["mothername"]
          husband_name=request.POST["husbandname"]
          grandfather_name =request.POST["Grandfathername"]
          father_citizen_number =request.POST["fathercitizennumber"]
          mother_citizen_number = request.POST["mothercitizenshipnumber"]
          husband_citizen_number = request.POST["husbandcitizenshipnumber"]
          birth_certificate_photo =request.POST["birthcerificatephoto"]
          father_citizenship_photo =request.POST["fathercitizenship"]
          mother_citizenship_photo = request.POST["mothercitizenship"]
          husband_citizenship_photo = request.POST["husbandcitizenship"]
          zone = request.POST["Zone"]
          district =request.POST["District"]
          village = request.POST["Village/Municipality"]
          ward = request.POST["Ward no"]
          tole = request.POST["Tole"]
          house_no = request.POST["House no."]
          address_type=request.POST['address_type']


          citizen=Citizen(first_name=user.first_name,last_name=user.last_name,email=user.email,dob=dob,phone=phone,age=age,gender=gender,father_name=father_name,mother_name=mother_name,husband_name=husband_name,
                          grandfather_name=grandfather_name,father_citizen_number=father_citizen_number,mother_citizen_number=mother_citizen_number,
                          husband_citizen_number= husband_citizen_number,father_citizenship_photo=father_citizenship_photo,
                          mother_citizenship_photo=mother_citizenship_photo,husband_citizenship_photo=husband_citizenship_photo)
          address=Address(zone=zone,district=district,village=village,ward=ward,tole=tole,house_no=house_no,address_type=address_type)
          citizen.save()
          address.save()
          message.success(request,"Your form has been submitted to the admin")
          return redirect('index')





    else:

      return render(request,'pages/index.html')