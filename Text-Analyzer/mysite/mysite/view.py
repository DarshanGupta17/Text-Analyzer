# i have created this file
from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     return HttpResponse(''' <h1>Home</h1> <a href="http://127.0.0.1:8000/about">Click to go in the about section</a>''')
# def about(request):
#     return HttpResponse('''<h1>About</h1> <a href="http://127.0.0.1:8000/">click to go in the Home section </a>''')

def index(request):
    return render(request,'index.html')
def analyze(request):
    djtext = (request.POST.get('text','default'))
    removepunc = request.POST.get('removePunc','off')
    FullCapitalize = request.POST.get('FullCapitalize','off')
    NewLine = request.POST.get('NewLine','off')
    extraSpacer = request.POST.get('extraSpacer' , 'off')
    charCount = request.POST.get('charCount' , 'off')
    print(removepunc)
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    f = False
    if removepunc == "on":
        f = True
        analyzed = ""
        for char in djtext:
            if char in punctuation:
                continue
            else:
                analyzed += char
        djtext = analyzed
    if FullCapitalize == 'on':
        f = True
        analyzed = ""
        for char in djtext:
            analyzed+=char.upper()
        djtext = analyzed
    if NewLine == 'on':
        f = True
        analyzed = ""
        for char in djtext:
            if char != '\n'and char !='\r':
                analyzed += char
        djtext = analyzed
    if extraSpacer == 'on':
        f = True
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == ' ' and djtext[index + 1] == ' '):
                analyzed += char
        djtext = analyzed
    if charCount == "on":
        f = True
        count = 0
        for char in djtext:
            count+=1
        analyzed = count
    if f == True:
        params = {'purpose': 'removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return render(request, 'Nothing.html')
# def capfirst(request):
#     return HttpResponse('''capitalize first <br>
#     <button><a href="http://127.0.0.1:8000/">back</a></button>''')
# def newlineRemover(request):
#     return HttpResponse('''newLine <br>
#     <button><a href="http://127.0.0.1:8000/">back</a></button>''')
# def spaceRemover(request):
#     return HttpResponse('''spaceRemover  <br>
#     <button><a href="http://127.0.0.1:8000/">back</a></button>''')
# def charCount(request):
#     return HttpResponse('''charCount  <br>
#     <button><a href="http://127.0.0.1:8000/">back</a></button>''')