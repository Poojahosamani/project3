from django.shortcuts import render
from datetime import datetime
from first.models import train
from django.http import HttpResponse

# Create your views here.
def display(request):
	text = """Welcome to MyTrainApp """
	return render(request,"t.html",{"banner":text})
def MyTrain(request):
	t1 = train(slNo =1,Date="2021-11-26",TrainName="SHATABDI EXP",DepartureFrom="Bangalore",Departuretime="6:00",ArrivingAt="Mysuru",Arrivaltime="9:00")
	t1.save()
	t2= train(slNo =2,Date="2021-11-27",TrainName="COIMBATORE EXP",DepartureFrom="Bangalore",Departuretime="15:00",ArrivingAt="Chennai",Arrivaltime="9:00")
	t2.save()
	t3 = train(slNo =3,Date="2021-11-27",TrainName="KAVERI EXP",DepartureFrom="Mysuru",Departuretime="16:00",ArrivingAt="Bangalore",Arrivaltime="19:00")
	t3.save()
	t4 = train(slNo =4,Date="2021-11-28",TrainName="LOKAMANYA EXP",DepartureFrom="Bangalore",Departuretime="6:00",ArrivingAt="Goa",Arrivaltime="2:00")
	t4.save()
	t5 = train(slNo =5,Date="2021-11-28",TrainName="VASC0 EXP",DepartureFrom="Bangalore",Departuretime="14:00",ArrivingAt="Goa",Arrivaltime="10:00")
	t5.save()
	t6=train(slNo =6,Date="2021-11-29",TrainName="MALGUDI EXP",DepartureFrom="Mysuru",Departuretime="7:00",ArrivingAt="Bangalore",Arrivaltime="9:00")
	t6.save()
	t7 =train(slNo =7,Date="2021-11-29",TrainName="TIPPU EXP",DepartureFrom="Bangalore",Departuretime="18:00",ArrivingAt="Mysuru",Arrivaltime="20:30")
	t7.save()
	t8 =train(slNo =8,Date="2021-11-30",TrainName="SHATABDI EXP",DepartureFrom="Mysuru",Departuretime="6:00",ArrivingAt="Chennai",Arrivaltime="16:00")
	t8.save()
	t9 = train(slNo =9,Date="2021-11-30",TrainName="MANGALURU CENTRAL EXP",DepartureFrom="Mysuru",Departuretime="12:00",ArrivingAt="Chikmagaluru",Arrivaltime="22:00")
	t9.save()
	t10 =train(slNo =10,Date="2021-11-30",TrainName="KANNUR EXP",DepartureFrom="Mysuru",Departuretime="6:00",ArrivingAt="Kasargod",Arrivaltime="15:50")
	t10.save()
	objects = train.objects.all()
	return render(request,"test.html",{"objects":objects})
	#objects.delete()