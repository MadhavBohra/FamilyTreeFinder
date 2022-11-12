from django.shortcuts import render, HttpResponse
import requests

# Create your views here.
def get_electoralsearch_content():
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content = session.get(f"https://electoralsearch.in/").text
    return html_content





def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        state = request.POST.get('state')
        district = request.POST.get('district')
        AC = request.POST.get('AC')
        fname = request.POST.get('fname')
        gender = request.POST.get('gender')
        pass
    html_content = get_electoralsearch_content()
    print(html_content)
    return render(request,'index.html')
