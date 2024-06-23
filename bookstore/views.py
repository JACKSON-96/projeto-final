import os
import git
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def update(request):
    if request.method == 'POST':
        # Caminho correto para o repositório
        repo_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'bookstore-main')
        repo = git.Repo(repo_path)
        origin = repo.remotes.origin
        origin.set_url('git@github.com:JACKSON-96/projeto-final.git')
        origin.pull()
        return HttpResponse('Updated code on local machine')
    else:
        return HttpResponse("Couldn't update the code on local machine")
