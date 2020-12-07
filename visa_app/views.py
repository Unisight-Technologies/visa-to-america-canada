from django.shortcuts import render, get_object_or_404
from django.views.generic import View, TemplateView
from . import models
from . import scrap_news
import requests
import tempfile

from django.core import files

class HomePage(TemplateView):
    template_name = "index.html"


class InnerPage(TemplateView):
    template_name = "inner-page.html"


class PortfolioPage(TemplateView):
    template_name = "portfolio.html"

class AboutPage(TemplateView):
    template_name = "about.html"

class ContactPage(TemplateView):
    template_name = "contact.html"

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

class Blog(View):
    def get(self, request, *args, **kwargs):

        # scrapper = scrap_news.Scrapper()
        #
        # for i in range(0,5):
        #     news = models.News.objects.create(
        # 		author=scrapper.authors[i],
        # 		title=scrapper.titles[i],
        # 		description=scrapper.descriptions[i],
        # 		url=scrapper.urls[i]
        #         )
        #     news.save()
        #
        #     image_url = scrapper.url_images[i]
        #     response = requests.get(image_url, stream=True)
        #
        #     # Was the request OK?
        #     if response.status_code != requests.codes.ok:
        #         # Nope, error handling, skip file etc etc etc
        #         continue
        #
        #     # Get the filename from the url, used for saving later
        #     file_name = image_url.split('/')[-1]
        #
        #     # Create a temporary file
        #     lf = tempfile.NamedTemporaryFile()
        #
        #     # Read the streamed image in sections
        #     for block in response.iter_content(1024 * 8):
        #
        #         # If no more file then stop
        #         if not block:
        #             break
        #
        #         # Write image block to temporary file
        #         lf.write(block)
        #
        #     # Create the model you want to save the image to
        #     new_news = models.News.objects.get(title=scrapper.titles[i])
        #     # Save the temporary image to the model#
        #     # This saves the model so be sure that it is valid
        #     new_news.image.save(file_name, files.File(lf))

        render_news = models.News.objects.all()
        context = {
            'news': render_news
        }

        return render(request, 'blogs.html', context=context)
