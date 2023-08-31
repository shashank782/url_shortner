from django.shortcuts import render,redirect
from urlapp.models import Url
# Create your views here.
def ind(request):
    if request.method == 'POST':
        F_url=request.POST.get('F_url')
        obj = Url.create(F_url)
        return render(request,'urlapp/index.html',{'F_url': obj.F_url, 'S_url':request.get_host() + '/'+obj.S_url})
    
    return render(request,'urlapp/index.html')

def routetourl(request,key):
    try :
        obj = Url.objects.get(S_url=key)
        return redirect(obj.F_url)
    except:        
        return redirect(ind)
    

