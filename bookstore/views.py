# bookstore/views.py

from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import git
import os

@csrf_exempt
def update(request):
    if request.method == 'POST':
        repo_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        repo = git.Repo(repo_path)
        origin = repo.remotes.origin
        origin.set_url('https://github.com/JACKSON-96/bookstore.git')  # Substitua pela URL do seu repositório GitHub
        origin.pull()
        return HttpResponse('Updated code on local machine')
    else:
        return HttpResponse("Couldn't update the code on local machine")

def hello_world(request):
    template = loader.get_template('hello_world.html')
    return HttpResponse(template.render())

def home(request):
    return HttpResponse("Welcome to the Bookstore!")
