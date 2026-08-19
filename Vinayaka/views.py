import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Vinayaka


def convert_data(obj):
    return {
        "id": obj.id,
        "Name": obj.Name,
        "Amount": obj.Amount,
        "Phone": obj.Phone,
        "SenderNumber": obj.SenderNumber,
        "updatedAt": obj.updatedAt.isoformat(),
    }


@csrf_exempt
def vinayaka_list(request):

    # =====================================
    # GET ALL
    # =====================================

    if request.method == "GET":

        data = Vinayaka.objects.all().order_by("-id")

        result = [
            convert_data(item)
            for item in data
        ]

        return JsonResponse(
            result,
            safe=False
        )

    # =====================================
    # POST
    # =====================================

    if request.method == "POST":

        try:

            data = json.loads(
                request.body
            )

            obj = Vinayaka.objects.create(
                Name=data.get("Name", ""),
                Amount=data.get("Amount", ""),
                Phone=data.get("Phone", ""),
                SenderNumber=data.get(
                    "SenderNumber",
                    ""
                ),
            )

            return JsonResponse(
                convert_data(obj),
                status=201
            )

        except Exception as error:

            return JsonResponse(
                {
                    "error": str(error)
                },
                status=400
            )

    return JsonResponse(
        {
            "error":
                "Method not allowed"
        },
        status=405
    )


@csrf_exempt
def vinayaka_detail(
    request,
    mid
):

    # =====================================
    # GET SINGLE
    # =====================================

    if request.method == "GET":

        try:

            obj = Vinayaka.objects.get(
                id=mid
            )

            return JsonResponse(
                convert_data(obj)
            )

        except Vinayaka.DoesNotExist:

            return JsonResponse(
                {
                    "error":
                        "Data not found"
                },
                status=404
            )

    # =====================================
    # PUT
    # =====================================

    if request.method == "PUT":

        try:

            obj = Vinayaka.objects.get(
                id=mid
            )

            data = json.loads(
                request.body
            )

            obj.Name = data.get(
                "Name",
                obj.Name
            )

            obj.Amount = data.get(
                "Amount",
                obj.Amount
            )

            obj.Phone = data.get(
                "Phone",
                obj.Phone
            )

            obj.SenderNumber = data.get(
                "SenderNumber",
                obj.SenderNumber
            )

            obj.save()

            return JsonResponse(
                convert_data(obj)
            )

        except Vinayaka.DoesNotExist:

            return JsonResponse(
                {
                    "error":
                        "Data not found"
                },
                status=404
            )

        except Exception as error:

            return JsonResponse(
                {
                    "error": str(error)
                },
                status=400
            )

    # =====================================
    # DELETE
    # =====================================

    if request.method == "DELETE":

        try:

            obj = Vinayaka.objects.get(
                id=mid
            )

            obj.delete()

            return JsonResponse(
                {
                    "message":
                        "Successfully deleted"
                }
            )

        except Vinayaka.DoesNotExist:

            return JsonResponse(
                {
                    "error":
                        "Data not found"
                },
                status=404
            )

    return JsonResponse(
        {
            "error":
                "Method not allowed"
        },
        status=405
    )