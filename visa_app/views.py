from django.shortcuts import render
from django.views.generic import View, TemplateView

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

class ServicesPage(TemplateView):
    template_name = "services.html"

class TeamPage(TemplateView):
    template_name = "team.html"

class ExpressEntry(TemplateView):
    template_name = "express_entry.html"

class CareGiver(TemplateView):
    template_name = "care_giver.html"
