from django.http import HttpResponse,JsonResponse
def home_page(request):
    print("home page requested")
    friends=[
        'shivank',
        'abhishek',
        'hrithik',
        'prakhar',
    ]
    return JsonResponse(friends,safe=False)