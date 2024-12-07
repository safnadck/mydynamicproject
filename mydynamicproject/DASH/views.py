from django.http import HttpResponse

def dashboard_view(request):
    return HttpResponse("<h1>Dashboard</h1><p>Get an overview of the key metrics and data.</p>")

def profile_view(request):
    return HttpResponse("<h1>User Profile</h1><p>Manage your account details and preferences here.</p>")

def services_view(request):
    return HttpResponse("<h1>Services</h1><p>Explore the services we offer to enhance your experience.</p>")

def support_view(request):
    return HttpResponse("<h1>Support</h1><p>Need help? Get in touch with our support team.</p>")

def faq_view(request):
    return HttpResponse("<h1>FAQs</h1><p>Find answers to the most frequently asked questions.</p>")
