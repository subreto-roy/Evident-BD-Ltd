
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import InputHistory

from django.shortcuts import render

from .models import InputHistory
import datetime
# Create your views here.


@login_required(login_url='login')
def HomePage(request):
    return render(request, 'khoj_search.html')



def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('khoj_search')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

from .models import InputHistory
import datetime

@login_required(login_url='login')
def khoj_search(request):
    result = None
    input_history_list = []  # List to store input history

    if request.method == 'POST':
        input_values = request.POST.get('input_values')
        search_value = int(request.POST.get('search_value'))

        input_list = list(map(int, input_values.split(',')))
        input_list.sort(reverse=True)

        # Store input values in the database
        input_history = InputHistory(user=request.user, input_values=', '.join(map(str, input_list)))
        input_history.save()

        # Check if search value is in input values
        result = search_value in input_list

    # Retrieve input history for the user in descending order
    input_history_list = InputHistory.objects.filter(user=request.user).order_by('-timestamp')

    return render(request, 'khoj_search.html', {'result': result, 'input_history_list': input_history_list})




from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import InputHistory
from .serializers import InputHistorySerializer

@api_view(['POST'])
def post_input_numbers(request):
    if request.method == 'POST':
        input_values = request.data.get('input_values')  # Assuming input_values is a list of numbers

        # Convert list of numbers to a comma-separated string
        input_values_str = ', '.join(map(str, input_values))

        # Store input values in the database
        input_history = InputHistory(user=request.user, input_values=input_values_str)
        input_history.save()

        # Retrieve input history records for the user
        input_history_records = InputHistory.objects.filter(user=request.user)

        # Serialize input history records
        input_values_serializer = InputValuesSerializer(input_history_records, many=True)

        response_data = {
            'status': 'success',
            'user_id': request.user.id,
            'payload': input_values_serializer.data
        }

        return Response(response_data)

    return Response({'message': 'Invalid request method'})

