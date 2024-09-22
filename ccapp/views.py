from django.shortcuts import render
import requests


def home(request):
    if request.GET.get("amt") and request.GET.get("currency"):
        amt = float(request.GET.get("amt"))
        currency = request.GET.get("currency")


        bitcoin_to_usd_url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        bitcoin_to_usd_response = requests.get(bitcoin_to_usd_url)
        bitcoin_to_usd_data = bitcoin_to_usd_response.json()
        bitcoin_to_usd_rate = bitcoin_to_usd_data["bpi"]["USD"]["rate_float"]


        # Define exchange rates for other currencies
        usd_to_inr_rate = 83.32  
        usd_to_gbp_rate = 0.82  
        usd_to_rub_rate = 99.63  




        converted_amount = None
        currency_symbol = None


        if currency == "INR":
            converted_amount = amt * bitcoin_to_usd_rate * usd_to_inr_rate
            currency_symbol = "\u20B9"
        elif currency == "USD":
            converted_amount = amt * bitcoin_to_usd_rate
            currency_symbol = "$"
        elif currency == "GBP":
            converted_amount = amt * bitcoin_to_usd_rate * usd_to_gbp_rate
            currency_symbol = "£"
        elif currency == "RUB":
            converted_amount = amt * bitcoin_to_usd_rate * usd_to_rub_rate
            currency_symbol = "₽"


        if converted_amount is not None:
            msg = f"{currency_symbol}{converted_amount:.2f}"
            return render(request, "home.html", {"msg": msg})


    return render(request, "home.html")
