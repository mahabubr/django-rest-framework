from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET", "POST"])
def index(request):
    if request.method == "GET":
        courses = {"course_name": "python"}
        return Response(courses)

    elif request.method == "POST":
        courses = {"course_name": "python POST"}
        return Response(courses)
