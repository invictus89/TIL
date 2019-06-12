from django.shortcuts import render, redirect
from .models import Board, Comment
from IPython import embed
# Create your views here.

def index(request):
    boards = Board.objects.all()
    context = {'boards' : boards,}
    return render(request, 'boards/index.html', context)

def create(request):
    # request 가 POST 로 왔을 때 create
    if request.method == 'POST':
        title=request.POST.get('title')
        content=request.POST.get('content')
        board = Board()
        board.title = title
        board.content = content
        board.save()
        return redirect('/boards/index')
    else:
        return render(request, 'boards/create.html')

def detail(request, pk):
    board = Board.objects.get(pk=pk)
    comments = board.comment_set.order_by('-pk')
    context = {'board':board, 'comments': comments, }
    return render(request, 'boards/detail.html', context)

def delete(request, pk):
    board = Board.objects.get(pk=pk)
    if request.method == 'POST':
        board.delete()
        return redirect('boards:index')
    else:
        pass

def update(request, pk):
    board = Board.objects.get(pk=pk)
    if request.method == 'POST':
        board.title = board.title = request.POST.get('title')
        board.content = board.content= request.POST.get('content')
        board.save()
        return redirect('boards:detail', board.pk)
    else:
        context = {'board': board, }
        return render(request, 'boards/edit.html', context)

def comments_create(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        comment = Comment(board=board, content=content)
        # comment = Comment(board_id=board_pk, content=content)
        comment.save()
        return redirect('boards:detail', board.pk)
    else:
        return redirect('boards:detail', board.pk)

def comments_delete(request, comment_pk, board_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('boards:detail', board_pk)
    else:
        return redirect('boards:detail', board_pk)
