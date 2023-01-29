from django.shortcuts import render, redirect
from .models import Posts, Events, Categories, GroupCategories, Groups, Users, Comments
from django.contrib.auth import login, authenticate  # add to imports
from django.views.generic.detail import DetailView
from .filters import EventFilter


# Create your views here.
def home(request):
    context = {}
    all_posts = Posts.objects.all()
    user_groups = Groups.objects.all()
    logged_in_user = ""
    context = {'posts': all_posts, 'groups': user_groups, 'logged_in_user': logged_in_user}
    return render(request, 'mh23App/homepage.html', context)

def index(request):
    events = Events.objects.all()
    myFilter = EventFilter(request.GET, queryset=events)
    events = myFilter.qs
    context = {
        'myFilter': myFilter,
        'events': events,
    }
    return render(request, 'mh23App\homepage.html', context)

def filter_data(request):
	if request.method == 'POST':
		num_miles = request.POST.get('field')
		entries = []
		for i in Posts.objects.all():
			if int(num_miles) > int(i.location):
				entries.append(i)
		context = {'posts': entries}
		return render(request, 'mh23App/homepage.html', context)


def notifications(request):
    context = {}
    events = Events.objects.all()
    latest_date = events[0];
    for i in events:
        if i.date_of_event > latest_date.date_of_event:
            latest_date = i
    context = {'post': latest_date}
    print( latest_date.name, latest_date.description)
    return render(request, 'mh23App/notifications.html', context)


def settings(request):
    context = {}
    return render(request, 'mh23App/settings.html', context)


def messages(request):
    context = {}
    return render(request, 'mh23App/messages.html', context)

# def check_login(request):
#     email = request.POST.get('email')
#     password = request.POST.get('password')
#     all_users = Users.objects.all()
#     if email in all_users:
#         if all_users[email].password == password:
#             print("success")
#             return render(request, 'mh23App/homepage.html', context={'logged_in_user': all_users[email].email})
#         else:
#             print("wrong pw")
            
# def login_page(request):
#     return render(request, 'mh23App/login.html', context={})


def events(request):
    all_events = Events.objects.all()
    context = {'events': all_events}
    return render(request, 'mh23App/events.html', context)


def post_image_view(request):

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PostForm()
    return render(request, 'mh23App/homepage.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')


class UserView(DetailView):
    template_name = 'mh23App/homepage.html'

    def get_object(self):
        return self.request.user

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, email=user.email, password=raw_password)
            if user is not None:
                login(request, user)
            else:
                print("user is not authenticated")
            return redirect('mh23App:profile')
    else:
        form = SignUpForm()
    return render(request, 'mh23App/signup.html', {'form': form})
