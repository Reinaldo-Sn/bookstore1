from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import git


@csrf_exempt
def update(request):
    if request.method == "POST":
        '''
        pass the path of the diectory where your project will be
        stored on PythonAnywhere in the git.Repo() as parameter.
        Here the name of my directory is "test.pythonanywhere.com"
        '''
        repo = git.Repo('/home/Reinaldo/bookstore')
        origin = repo.remotes.origin

        origin.pull()
        return HttpResponse("Updated code on PythonAnywhere")
    else:
        return HttpResponse("Couldn't update the code on PythonAnywhere")


def hello_world(request):
    return HttpResponse("<h1>Bookstore API</h1><p>Acesse <a href='/bookstore/v1/order/'>/bookstore/v1/order/</a></p>")