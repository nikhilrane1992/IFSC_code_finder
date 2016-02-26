from django.shortcuts import render_to_response, HttpResponse
import json, datetime

def landing_page(request):
	return render_to_response('html_templates/landing_page.html')