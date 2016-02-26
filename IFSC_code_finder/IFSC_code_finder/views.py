from django.shortcuts import render_to_response, HttpResponse
import json, datetime,os
from settings import BASE_DIR

def landing_page(request):
	return render_to_response('html_templates/landing_page.html')

def serve_bank_names(request):
	bankNameFileList =  os.listdir(BASE_DIR+'/static/Data')
	return HttpResponse(json.dumps({"bankNameFileList": bankNameFileList, "status": True}), content_type="application/json")

def send_branch_ifsc_code(request):
	dataDictionary = json.loads(request.body)
	jsonFile = open(BASE_DIR+'/static/Data/'+dataDictionary['bankName'], 'r')
	jsonFile = json.loads(jsonFile.read())
	return HttpResponse(json.dumps({"bankIfscCodeJsonObj": jsonFile, "status": True}), content_type="application/json")