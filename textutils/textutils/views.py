from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request,'index.html')

def analyzed(request):
    djtext=request.POST.get('Text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps', 'off')
    newlineremove=request.POST.get('newlineremove', 'off')
    extraspaceremove=request.POST.get('extraspaceremove', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')

    print(removepunc)
    print(djtext)

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'Analyze.html', params)

    if fullcaps== "on":
        analyzed = ""

        for char in djtext:

           analyzed = analyzed + char.upper()

        params = {'purpose': 'Full capital', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'Analyze.html', params)

    if newlineremove == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext=analyzed

        # Analyze the text

        #return render(request, 'analyze.html', params)

    if extraspaceremove== "on":
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index]== " " and djtext[index+1]== " "):
             analyzed = analyzed + char
        params = {'purpose': 'Removed Extra space', 'analyzed_text': analyzed}


        if (removepunc != "on" and fullcaps != "on" and newlineremove != "on" and extraspaceremove != "on"):
            return HttpResponse("error hain")




        return render(request, 'analyze.html', params)

    '''elif  charactercounter== "on":
        analyzed=len(djtext)

        params={'purpose': 'count the no of words', 'analyzed_text': analyzed}
        return render(request,'Analyze.html',params)'''







'''def capfirst(request):
    return HttpResponse("Capitalization first")

def newlineremover(request):
    return HttpResponse("New line remove")

def spaceremover(request):
    return HttpResponse("Remove space")

def charcount(request):
    return HttpResponse("Character count")'''