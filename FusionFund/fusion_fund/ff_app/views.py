from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Text
from fusion_fund import manage

from summarizer.summary import * 

# says that this function can do handle POST requests
@api_view(["POST"])
def summarize_view(request):
	
	# handle data inputs
	if request.method == "POST":
		
		# # get the data and provide No value if not given
		# text = request.data.get("text", None)
		
		# # add it to the database and save
		# new_addition = Text(text=text)
		# new_addition.save()

		# pull the text and summarize it
		# summary = summarize(new_addition.text)
		try:
			summary = summarize(manage.getContent('https://www.ft.com/content/4c64ffc1-f57b-4e22-a4a5-f9f90a7419b7'))
		except Exception as e:
			print(e)
			summary = "Text Was Not Summarized"

		
		# return answer & status 200 (meaning everything worked!) 
		return Response(summary, status=200)

