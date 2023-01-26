from django.shortcuts import render
from rest_framework.decorators import api_view
import africastalking
from rest_framework.response import Response
from rest_framework import status

# phone_number = "+2349037601811"
#  #Change this to your country's code
# amount = 900
# following_msg = "thank you for signing up"

# try:
    
#     print(response)
# except Exception as e:
#     print(f"Encountered an error while sending airtime. More error details below\n {e}")

def talker(phone_number, amount):
    username = "sandbox"
    api_key = "7e62c3354e8c37df9cc21abb2fee96f5286d7d314cc244ad52c6e508068f1afa"
    currency_code = "NGN"
    africastalking.initialize(username, api_key)
    airtime = africastalking.Airtime
    result = airtime.send(phone_number=phone_number, amount=amount, currency_code=currency_code)
    return result

@api_view(['POST'])
def reacharge(request):
    data = request.data
    phone_number = data['mobile']
    amount = data['amount']
    
    try:
        result = talker(phone_number,amount)

        return Response(data=result, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)
    


# {"phone_number":"+2349037601811",
# "amount":"500"
# }
