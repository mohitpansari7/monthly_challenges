from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenge = {
    "january" : "“I dont believe in taking right decisions. I take decisions and then make them right.”-Ratan Tata",
    "february" : "“I always knew I was going to be rich. I don't think I ever doubted it for a minute.” -Warren Buffett",
    "march" : "The way to get started is to quit talking and begin doing. -Walt Disney",
    "april" : "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success. -James Cameron",
    "may" : "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma which is living with the results of other people's thinking. -Steve Jobs",
    "june" : "Spread love everywhere you go. Let no one ever come to you without leaving happier. -Mother Teresa",
    "july" : "Don't judge each day by the harvest you reap but by the seeds that you plant. -Robert Louis Stevenson",
    "august" : "It is during our darkest moments that we must focus to see the light. -Aristotle",
    "september" : "The future belongs to those who believe in the beauty of their dreams. -Eleanor Roosevelt",
    "october" : "Many of life's failures are people who did not realize how close they were to success when they gave up. -Thomas A. Edison",
    "november" : "You will face many defeats in life, but never let yourself be defeated. -Maya Angelou",
    "december" : "The purpose of our lives is to be happy. -Dalai Lama",
}
# Create your views here.

def ping(request):
    return HttpResponse('Server is up and running at PORT 8000')

def index(request):
    list_items = ""
    months = list(monthly_challenge.keys())

    for month in months:
        cap_month = month.capitalize()
        list_items += f"<li><a href=\"{month}\">{cap_month}</a></li>"

    return HttpResponse(f"<ul>{list_items}</ul>")

def monthly_challenge_by_int(request, month):
    months = list(monthly_challenge.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    fwd_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[fwd_month])
    #monthly_challenges(request, forward_month)
    return HttpResponseRedirect(redirect_path)

def monthly_challenges_by_str(request, month):
    print('printing request',request, month)
    try :  
        challenge_text = monthly_challenge[month]
        response_data = f"<h2>{challenge_text}</h2>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("This is invalid request")

    
    