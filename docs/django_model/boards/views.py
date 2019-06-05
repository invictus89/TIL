from django.shortcuts import render, redirect
from .models import Board
# Create your views here.

def index(request):
    boards = Board.objects.all()
    context = {'boards' : boards,}
    return render(request, 'boards/index.html', context)

def new(request):
    return render(request, 'boards/new.html')

def create(request):
    # from new, get data
    title=request.POST.get('title')
    content=request.POST.get('content')
    # allocate orm title and content
    board = Board()
    board.title = title
    board.content = content
    # db save
    board.save()
    print(f'title: {board.title}')
    print(f'content: {board.content}')

    # render page
    return redirect('/boards/index/')

def detail(request, pk):
    board = Board.objects.get(pk=pk)
    context = {'board':board,}
    return render(request, 'boards/detail.html', context)
