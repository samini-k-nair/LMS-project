from django.shortcuts import render,redirect

from django.views import View

from .models import Courses,CategoryChoices,LevelChoices

from .forms import CourseCreateForm

from instructors.models import Instructors

from django.db.models import Q

from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from  authentication.permissions import permission_roles

# from lms.utility import get_recommended_courses
# Create your  here.
class CoursesListView(View):

    def get(self,request,*args,**kwargs):

        # fetching all courses from model

        query = request.GET.get('query')

        courses =Courses.objects.all()

        if query :

            courses =Courses.objects.filter(Q(title__icontains=query)|
                                           Q(description__icontains=query)|
                                           Q(instructor__name__icontains=query)|
                                           Q(category__icontains=query)|
                                           Q(type__icontains=query)|
                                           Q(level__icontains=query)|
                                           Q(fee__icontains=query))

            
       

        data = {'courses':courses,'page':'courses-page','query':query}

        return render(request,'courses/courses-list.html',context=data)
class CourseDetailView(View): 

    def get(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        course = Courses.objects.get(uuid=uuid) # pk means primery key

        # recommended_courses = get_recommended_courses(course)

        # data = {'course': course,'recommended_courses': recommended_courses}

        data = {'course': course}


        return render(request,'courses/course-detail.html',context=data)    
    
class HomeView(View): 

    def get(self,request,*args,**kwargs):

        data={'page':'home-page'}

        return render(request,'courses/home.html',context=data)

# @method_decorator(login_required(login_url='login'),name='dispatch')   

@method_decorator(permission_roles(roles=['Instructor']),name='dispatch')
class InstructorCourseListView(View):

     def get(self,request,*args,**kwargs):

        query = request.GET.get('query')

        # courses =Courses.objects.all()

        print(query)
      

        instructor =Instructors.objects.get(profile=request.user)

        courses = Courses.objects.filter(instructor = instructor)
        if query :

            courses =Courses.objects.filter(Q(title__icontains=query)|
                                           Q(description__icontains=query)|
                                           Q(instructor__name__icontains=query)|
                                           Q(category__icontains=query)|
                                           Q(type__icontains=query)|
                                           Q(level__icontains=query)|
                                           Q(fee__icontains=query))


        print(courses)

        data = { 
             'query' : query,
            'page': 'instructor-courses-page',
            'courses' : courses}

        # data={'page':'instructor-course-list','courses':courses}

        return render(request,'courses/instructor-course-list.html',context=data)

# @method_decorator(login_required(login_url='login'),name='dispatch')    
@method_decorator(permission_roles(roles=['Instructor']),name='dispatch')    
class CourseCreateView(View):

    def get(self,request,*args,**kwargs):

       # data = {'categories':CategoryChoices,'levels':LevelChoices}# from model.py import

        form = CourseCreateForm()

        data = {'form': form}

        return render(request,'courses/course-create.html',context=data)
    
    
    def post(self,request,*args,**kwargs):

        form = CourseCreateForm(request.POST,request.FILES)

        instructor =Instructors.objects.get(id=1)

        if form.is_valid():

           
            course = form.save(commit=False)

            # course.instructor = 'John Doe'

            course.instructor = instructor

            course.save()
           

            return redirect('instructor-course-list')
        data = {'form':form}
        
        return render(request,'courses/course-create.html',context=data)

# @method_decorator(login_required(login_url='login'),name='dispatch')  
@method_decorator(permission_roles(roles=['Instructor']),name='dispatch')     
class InstructorCourseDetailView(View): 

    def get(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        course = Courses.objects.get(uuid=uuid) # pk means primery key

        data = {'course': course }

        return render(request,'courses/instructor-course-detail.html',context=data)

@method_decorator(permission_roles(roles=['Instructor']),name='dispatch')    
class InstructorCourseDeleteView(View):    

    def get(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')# pick id

        course =Courses.objects.get(uuid=uuid)# object pick

        course.delete()

        return redirect('instructor-course-list')

# @method_decorator(login_required(login_url='login'),name='dispatch') 
@method_decorator(permission_roles(roles=['Instructor']),name='dispatch')  
class InstructorCourseupdateView(View):    

    def get(self,request,*args,**kwargs): 

        uuid =kwargs.get('uuid')

        course =Courses.objects.get(uuid=uuid)

        form = CourseCreateForm(instance=course)

        data = {'form':form}

        return render(request,'courses/instructor-course-update.html',context=data)
    
    def post(self,request,*args,**kwargs): 

        uuid = kwargs.get('uuid')

        course =Courses.objects.get(uuid=uuid)

        form = CourseCreateForm(request.POST,request.FILES,instance=course)
        
        if form.is_valid():

            form.save()

            return redirect('instructor-course-list')
    
        data = {'form':form}
       
        return render(request,'courses/instructor-course-update.html',context=data)
    
    
    

      
    

   
  