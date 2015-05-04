from django.shortcuts import render
from rango.models import Category, Page, UserProfile, UserFavorites, RedditUserName, FavRedditor
from rango.forms import CategoryForm, PageForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
import redditparse
import listsreturn
THUMBNAIL_SIZE = 'm'

# Create your views here.
def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    # Render the response and send it back!
    return render(request, 'rango/index.html', context_dict)

def category(request, category_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        pages = Page.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'rango/category.html', context_dict)

def add_category(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = CategoryForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'rango/add_category.html', {'form': form})

def add_page(request, category_name_slug):

    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
                cat = None

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                page.views = 0
                page.save()
                # probably better to use a redirect here.
                return category(request, category_name_slug)
        else:
            print form.errors
    else:
        form = PageForm()

    context_dict = {'form': form, 'category': cat, 'category_name_slug': category_name_slug}

    return render(request, 'rango/add_page.html', context_dict)


def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'rango/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/rango/')
            else:
                return HttpResponse("Your Rango account is currently disabled.")
        else:
            print "Invalid login details were provided: {0}, {1}".format(username,password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'rango/login.html', {})

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/rango/')


def getSubreddit(request, inputSubreddit, nextp = 'None'):

    if nextp == 'None':
        blah = redditparse.getSubmissionsInSubreddit(inputSubreddit)
    else:
        blah = redditparse.getExtraSubmissionsInSubreddit(inputSubreddit, nextp)

    if blah is None:
        #print "displaying none.html"
        return render(request, 'rango/index.html', {})
    else:
        #print "Not displaying none.html"
        workingList = blah[0]
        nextPage = blah[1]

    return render(request, 'rango/subreddit.html', {"title": '/r/' + inputSubreddit,
                                                    "workingList": workingList,
                                                    "nextPage": nextPage,
                                                    "glist": listsreturn.getGlist(),
                                                    "thumbnailSize": THUMBNAIL_SIZE
                                                    })

def getRedditor(request, inputRedditor, nextp = 'None'):
    #print 'start getRedditor'


    #print inputRedditor
    #print nextp
    if nextp == 'None':
        blah = redditparse.getSubmissionsInRedditor(inputRedditor)
    else:
        blah = redditparse.getExtraSubmissionsInRedditor(inputRedditor, nextp)


    if blah is None:
        return render(request, 'rango/index.html', {})
    else:
        workingList = blah[0]
        nextPage = blah[1]

    return render(request, 'rango/redditor.html', {"title": '/u/' + inputRedditor,
                                                    "workingList": workingList,
                                                    "nextPage": nextPage,
                                                    "glist": listsreturn.getGlist(),
                                                    "thumbnailSize": THUMBNAIL_SIZE
                                                    })

def add_fav(request, inputRedditor, inputImage ):
    #print inputRedditor
    #print inputImage



    if request.method == 'GET':
        if request.user.is_authenticated():
            username = request.user.username
            #print username

            r = RedditUserName.objects.get_or_create(username=username)[0]
            u = UserFavorites.objects.get_or_create(redditUserName = r)[0]

            if len(FavRedditor.objects.filter(favRedditor = inputRedditor,  userFavorites = u )) == 0:
                f = FavRedditor.objects.create(userFavorites = u)
                #print "f.favRedditor saving as " + inputRedditor
                f.favRedditor = inputRedditor
                #print "f.redditorImage saving as " + inputImage
                f.redditorImage = inputImage

                f.save()

            favlist = FavRedditor.objects.filter(  userFavorites = u )

            return render(request, 'rango/favorites.html', {"favlist": favlist,
                                                    "glist": listsreturn.getGlist(),
                                                    "thumbnailSize": THUMBNAIL_SIZE

                                                    })

def getFavorites(request):
    r = RedditUserName.objects.get_or_create(username=request.user.username)[0]
    u = UserFavorites.objects.get_or_create(redditUserName = r)[0]
    #print "checking favlist"
    favlist = FavRedditor.objects.filter(  userFavorites = u )
    #print favlist[0].redditorImage
    #print "end checking favlist"

    #if len(favlist) > 0:
        #print favlist

    return render(request, 'rango/favorites.html', {"favlist": favlist,
                                                    "glist": listsreturn.getGlist(),
                                                    "thumbnailSize": THUMBNAIL_SIZE
                                                    })

