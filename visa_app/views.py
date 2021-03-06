from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView
from . import models
from . import mailHandler
from django.contrib.auth.decorators import login_required
from . import scrap_news
import requests
from django.contrib import messages
from django.http import HttpResponse
import tempfile
#recaptcha imports
import json
import urllib
from django.conf import settings
import environ
env = environ.Env()
# reading .env file
environ.Env.read_env()
from django.core import files

class HomePage(TemplateView):
    template_name = "index.html"


class InnerPage(TemplateView):
    template_name = "inner-page.html"


class PortfolioPage(TemplateView):
    template_name = "portfolio.html"

class AboutPage(TemplateView):
    template_name = "about.html"

class Comingpage(TemplateView):
    template_name= "coming_soon.html"

class ContactPage(TemplateView):
    template_name = "contact.html"

    def get(self, request, *args, **kwargs):
        context={
            'SITE_KEY': env('RECAPTCHA_SITE_KEY')
        }

        return render(request, "contact.html",context = context)
    
    def post(self, request, *args, **kwargs):

        data = request.POST
        ''' Begin reCAPTCHA validation '''
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req =  urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        ''' End reCAPTCHA validation '''
        if result['success']:
            mailHandler.sendMailToUser(request.POST.get('name'), request.POST.get('email'))
            mailHandler.sendMailToVisaToCanada(request.POST.get('name'), request.POST.get('email'),request.POST.get('phone'),request.POST.get('subject'),request.POST.get('message'))
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('index')
        else:
            messages.info(request, 'Invalid reCAPTCHA. Please try again.')
            context={
            'SITE_KEY': env('RECAPTCHA_SITE_KEY')
            }
            return render(request,"contact.html",context = context)

class StudentPage(TemplateView):
    template_name = "student.html"

class PricingPage(TemplateView):
    template_name = "pricing.html"

class Nominee(TemplateView):
    template_name = "nominee.html"

class FamilyPage(TemplateView):
    template_name = "family.html"

class ServicesPage(TemplateView):
    template_name = "services.html"

class TeamPage(TemplateView):
    template_name = "team.html"

class ExpressEntry(TemplateView):
    template_name = "express_entry.html"

class CareGiver(TemplateView):
    template_name = "care_giver.html"

class Spain_Comingpage(TemplateView):
    template_name= "spain_coming_soon.html"

class Denmark_Comingpage(TemplateView):
    template_name= "Denmark_coming_soon.html"

class Italy_Comingpage(TemplateView):
    template_name= "Italy_coming_soon.html"

class Greece_Comingpage(TemplateView):
    template_name= "Greece_coming_soon.html"


class Blog(View):
    def get(self, request, *args, **kwargs):

        render_news = models.News.objects.all()
        context = {
            'news': render_news
        }

        return render(request, 'blogs.html', context=context)

@login_required(login_url='/admin/')
def refresh(request):
    if(models.News.objects.all().exists()):
        for i in range(0, 5):
            old_news = models.News.objects.all()[0]
            old_news.delete()

    scrapper = scrap_news.Scrapper()

    for i in range(0,5):
        news = models.News.objects.create(
    		author=scrapper.authors[i],
    		title=scrapper.titles[i],
    		description=scrapper.descriptions[i],
    		url=scrapper.urls[i]
            )
        news.save()

        image_url = scrapper.url_images[i]
        response = requests.get(image_url, stream=True)

        # Was the request OK?
        if response.status_code != requests.codes.ok:
            # Nope, error handling, skip file etc etc etc
            continue

        # Get the filename from the url, used for saving later
        file_name = image_url.split('/')[-1]

        # Create a temporary file
        lf = tempfile.NamedTemporaryFile()

        # Read the streamed image in sections
        for block in response.iter_content(1024 * 8):

            # If no more file then stop
            if not block:
                break

            # Write image block to temporary file
            lf.write(block)

        # Create the model you want to save the image to
        new_news = models.News.objects.get(title=scrapper.titles[i])
        # Save the temporary image to the model#
        # This saves the model so be sure that it is valid
        new_news.image.save(file_name, files.File(lf))

    return HttpResponse('News fetched successfully!')

def coming_soon(request):
    return render(request, 'coming.html')

class policy(TemplateView):
    template_name= "policy.html"

class terms(TemplateView):
    template_name= "terms.html"

class general(TemplateView):
    template_name= "generaldisclaimer.html"

class givesit(TemplateView):
    template_name= "givesit.html"
