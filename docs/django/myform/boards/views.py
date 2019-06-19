from django.shortcuts import render, redirect, get_object_or_404
from IPython import embed
from .models import Board
from .forms import BoardForm
from django.contrib.auth.decorators import login_required # 로그인이 필요한 기능을 정의시
from django.contrib.auth import get_user_model

# Create your views here.
def index(request):
    #embed()
    boards = Board.objects.order_by('-pk')
    context = {'boards': boards,}
    return render(request, 'boards/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        # Binding : form 인스턴스를 생성하고 요청(request.POT) 로 데이터를 채운다.
        form = BoardForm(request.POST)
        # form 유효성 체크
        if form.is_valid():
            '''
            # cleaned_data 는 dict 를 return 하기 때문에 .get 으로 접근 가능
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            # 검증을 통과한 깨끗한 데이터를 가져와서 board 인스턴스를 만든다.
            board = Board.objects.create(title=title, content=content)
            '''

            board = form.save(commit=False) # 추가적으로 값을 받겠다는 의미
            board.user = request.user # == request.user.pk
            board.save()
            # 이미 model 에서 정의한 메타 정보를 바탕으로 함으로 따로 clean 을 통한 유효성 검사를 안하여도 된다.
            
            return redirect('boards:detail', board.pk)
    # GET : 기본 form 인스턴스를 생성
    else:
        form = BoardForm()
    # context 에 넘어가는 2가지 form
    # 1. GET : 기본 FORM 모습으로 넘겨짐
    # 2. POST : 요청에서 검증에 실패한 form 이 오류메세지를 포함한 상태로 넘겨짐.
    context = {'form': form}
    return render(request, 'boards/form.html', context)

def detail(request, board_pk):
    # board = Board.objects.get(pk=board_pk)
    board = get_object_or_404(Board, pk=board_pk)
    person = get_object_or_404(get_user_model(), pk=board.user.pk)
    context = {'board': board, 'person' : person, }
    return render(request, 'boards/detail.html', context)

def delete(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if board.user == request.user:
        if request.method == 'POST':
            board.delete()
            return redirect('boards:index')
        else:
            return redirect('boards:detail', board.pk)
    else:
        return redirect('boards:index')

@login_required
def update(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if board.user == request.user or str(request.user) == 'admin':
        if request.method == 'POST':
            form = BoardForm(request.POST, instance=board)
            if form.is_valid():
                board = form.save()
                return redirect('boards:detail', board_pk)
        else:
            #embed()
            #form = BoardForm(initial={'title': board.title, 'content': board.content})
            form = BoardForm(instance=board) # 위의 코드와 동일
    else:
        # 남의 글을 수정하려 할 때
        return redirect('boards:index') 

    context = {'form': form, 'board': board, }
    return render(request, 'boards/form.html', context)

@login_required
def like(request, board_pk):
    # 로직 설명 :
    # 좋아요를 누른 사용자 목록 중에 내가 있다면 이미 좋아요를 누른 뜻이므로
    # 다시 누르면 좋아요 해제
    # 아니면
    # 좋아요
    board = get_object_or_404(Board, pk=board_pk)
    user = request.user
    if board.like_users.filter(pk=user.pk).exists(): 
        # if user in board.like_users.all()

        # get이 아닌 filter를 사용하는 이유:
        # get은 보통 유일한 값을 받아올 때 사용한다.
        # 즉, 값이 반드시 있다는 가정하에 동작하므로 없는 데이터를 get 하면 에러가 난다.
        board.like_users.remove(user)
    else:
        board.like_users.add(user)
    return redirect('boards:index')

def follow(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    user = request.user
    if person.followers.filter(pk=user.pk).exists():
        person.followers.remove(user)
    else:
        person.followers.add(user)
    return redirect('profile', person.username)
