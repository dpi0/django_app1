from django.http import JsonResponse


def index(request):
    data = [
        {
            "id": 1,
        },
        {
            "id": 2,
        },
    ]
    return JsonResponse(data, safe=False)
