import json
import os

from django.http import HttpResponse
from .puzzle_resolver import PuzzleResolver


def index(request):
    if request.method == 'GET':
        params = request.GET
        if params.get('q') and params.get('d'):
            return process_resume_queries(params)
        else:
            return HttpResponse("Welcome to RealTime Resume Validator. Expected parameters missing!")
    else:
        return HttpResponse("Welcome to RealTime Resume Validator. Only GET request supported!")


def process_resume_queries(params):
    field = params['q']
    expr = params['d']
    with open(os.path.join(os.path.dirname(__file__),
                           "resume_properties.json"), 'r') as json_file:
        data = json.load(json_file)
    valid_fields = ["Name", "Email Address", "Phone", "Position", "Years", "Referrer", "Degree",
                    "Resume", "Source", "Status", "Ping"]
    if field in valid_fields:
        return HttpResponse(data['Default'][field])
    elif field == 'Puzzle':
        return HttpResponse(PuzzleResolver(expr)())
    return HttpResponse("Incorrect param value!")


