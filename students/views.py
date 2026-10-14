from django.shortcuts import render

def home(request):

    students = ["Jagan", "Ram", "Shiva", "Somu", "Ravi"]

    context = {
            "students": students

            }

    return render(request, "home.html", context)
