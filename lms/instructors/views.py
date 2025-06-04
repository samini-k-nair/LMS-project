
from django.shortcuts import render ,redirect

from django.views import View

from django.db import transaction

from lms.utility import send_email

from .forms import InstructorForm

from students.forms import ProfileForm

from django.contrib.auth.hashers import make_password

import threading
class InstructorRegisterView(View):

    def get(self,request,*args,**kwargs):

        profile_form = ProfileForm()

        instructor_form = InstructorForm()

        data = {'profile_form' : profile_form,'instructor_form':instructor_form}

        return render(request,'instructors/instructor-register.html',context=data)

    def post(self, request, *args,**kwargs):

        profile_form = ProfileForm(request.POST)

        instructor_form = InstructorForm(request.POST, request.FILES)

        print(profile_form.errors)

        print(instructor_form.errors)



        if profile_form.is_valid():

            with transaction.atomic():

               profile = profile_form.save(commit=False)

               email = profile_form.cleaned_data.get('email')

               password = profile_form.cleaned_data.get('password')


               profile.username = email

               profile.role = 'Instructor'

               profile.password = make_password(password)

               profile.save()

               if instructor_form.is_valid():

                  instructor = instructor_form.save(commit=False)

                  instructor.profile = profile

                  instructor.name = f'{profile.first_name} {profile.last_name}'


                  instructor.save()

                  subject = 'Successfully Registered'

                  recipient = instructor.profile.email

                  template = 'email/success-registration.html'

                  context = {'name': instructor.name,'username':instructor.profile.email,'password':password}

                  thread = threading.Thread(target=send_email,args=(subject,recipient,template,context))

                  thread.start()

                  return redirect('login')

        data = {'profile_form' : profile_form,'  instructor_form':instructor_form} 

        return render(request,'instructors/instructor-register.html',context=data)   
