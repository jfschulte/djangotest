from django.shortcuts import render
from redapp.models import Category, Page, UserProfile,  RedditUserName, FavRedditor
from redapp.forms import CategoryForm, PageForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
import redditparse
import listsreturn
import psycopg2
from django.views.decorators.cache import cache_page
from django.core.cache.utils import make_template_fragment_key
from django.core.cache import cache
import time, sys


try:
    conn = psycopg2.connect("dbname='rgwdb' user='jfschulteadmin' host='localhost' password='Dbacks123!'")
except:
    print "I am unable to connect to the database"



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
    return render(request, 'redapp/index.html', {"subredditList": listsreturn.get_fullSubredditList(),
                                                })

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
    return render(request, 'redapp/category.html', context_dict)

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
    return render(request, 'redapp/add_category.html', {'form': form})

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

    return render(request, 'redapp/add_page.html', context_dict)


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
                  'redapp/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                print '1'
                return HttpResponseRedirect('/index')
            else:
                return HttpResponse("Your Rango account is currently disabled.")
        else:
            print "Invalid login details were provided: {0}, {1}".format(username,password)
            return HttpResponse("Invalid login details supplied.")
    else:
        print '2'
        return render(request, 'redapp/favorites.html', {"subredditList": listsreturn.get_fullSubredditList()})


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return render(request, 'redapp/index.html', {"subredditList": listsreturn.get_fullSubredditList()})


def getSubreddit(request, inputSubreddit, nextp = 'None'):
    template = 'redapp/subreddit.html'
    pagetemplate= 'redapp/subredditpage.html'
    key = '/r/' + inputSubreddit + nextp


    if (cache.get(key) == None):
        print "cache is none, getting parse"
        if nextp == 'None':
            blah = redditparse.getSubmissionsInSubreddit(inputSubreddit)
        else:
            blah = redditparse.getExtraSubmissionsInSubreddit(inputSubreddit, nextp)
        print "blah is"
        print blah
        cache.set(key, blah, 300)
        print cache.get(key)
    else:
        blah = cache.get(key)

    print "size is"
    print sys.getsizeof(blah)

    if blah:
        workingList = blah[0]
        nextp = blah[1]
    else:
        return render(request, template, {"title": "Oops!",
                                                    "workingList": [],
                                                    "nextPage": [],
                                                    "glist": listsreturn.getGlist(),
                                                    "thumbnailSize": THUMBNAIL_SIZE,
                                                    "sideList": listsreturn.get_quickList(),
                                                    "subredditList": listsreturn.get_fullSubredditList()
                                                    })


    #if request.is_ajax():
    #    template = pagetemplate


    return render(request, template, {"title": '/r/' + inputSubreddit,
                                                    "workingList": workingList,
                                                    "nextPage": nextp,
                                                    "glist": listsreturn.getGlist(),
                                                    "thumbnailSize": THUMBNAIL_SIZE,
                                                    "sideList": listsreturn.get_quickList(),
                                                    })

def getRedditor(request, inputRedditor, nextp = 'None'):
    start = time.time()

    key = '/u/' + inputRedditor + nextp

    cacheCheck = cache.get(key)
    print type(cacheCheck)
    if (cacheCheck == None):
        print "cache is none, getting parse"
        if nextp == 'None':
            blah = redditparse.getSubmissionsInRedditor(inputRedditor)
        else:
            blah = redditparse.getExtraSubmissionsInRedditor(inputRedditor, nextp)
        print "setting"
        print blah
        cache.set(key, blah, 5)
        print cache.get(key)
    else:
        blah = cache.get(key)

    if blah:
        workingList = blah[0]
        nextp = blah[1]
    else:
        return render(request, 'redapp/redditorbody.html', {"title": "Oops!",
                                                    "workingList": [],
                                                    "nextPage": [],
                                                    "glist": listsreturn.getGlist(),
                                                    "thumbnailSize": THUMBNAIL_SIZE,
                                                    "sideList": listsreturn.get_quickList(),
                                                    "subredditList": listsreturn.get_fullSubredditList()
                                                    })

    finish = time.time() - start
    print finish
    return render(request, 'redapp/redditorbody.html', {"title": '/u/' + inputRedditor,
                                                    "workingList": workingList,
                                                    "nextPage": nextp,
                                                    "glist": listsreturn.getGlist(),
                                                    "thumbnailSize": THUMBNAIL_SIZE,
                                                    "sideList": listsreturn.get_quickList(),
                                                    })

def add_fav(request, inputRedditor, inputImage ):
    #print inputRedditor
    #print inputImage



    if request.method == 'GET':
        if request.user.is_authenticated():
            username = request.user.username
            print username

            #r = RedditUserName.objects.get_or_create(username=username)[0]
            r = RedditUserName.objects.filter(username = username)
            print r
            if len(r) == 0:
                print "inside if r"
                r = RedditUserName(username=username)
                print r
                r.save()

            print "before f"
            f = FavRedditor.objects.filter(redditUserName = r, favRedditor = inputRedditor)
            #f = FavRedditor.objects.all()
            print "f is "
            print f
            if not f.exists():
                print "f is none"
            if len(f) == 0:
                print "inside if f"
                f = FavRedditor(redditUserName = RedditUserName.objects.get(username = username), favRedditor = inputRedditor, redditorImage = inputImage)
                #print f
                f.save()

            """
            u = UserFavorites.objects.get_or_create(redditUserName = r)[0]

            if len(FavRedditor.objects.filter(favRedditor = inputRedditor,  userFavorites = u )) == 0:
                f = FavRedditor.objects.create(userFavorites = u)
                #print "f.favRedditor saving as " + inputRedditor
                f.favRedditor = inputRedditor
                #print "f.redditorImage saving as " + inputImage
                f.redditorImage = inputImage

                f.save()

            favlist = FavRedditor.objects.filter(  userFavorites = u )

            return render(request, 'redapp/favorites.html', {"favlist": favlist,
                                                    "glist": listsreturn.getGlist(),
                                                    "thumbnailSize": THUMBNAIL_SIZE

                                                    })
            """
            favlist = FavRedditor.objects.filter( redditUserName = r )

            return render(request, 'redapp/favorites.html', {"favlist": favlist,
                                                    "glist": listsreturn.getGlist(),
                                                    "thumbnailSize": THUMBNAIL_SIZE

                                                    })

def getFavorites(request):
    r = RedditUserName.objects.get(username=request.user.username)
    #print "checking favlist"
    favlist = FavRedditor.objects.filter(  redditUserName = r )
    #print favlist[0].redditorImage
    #print "end checking favlist"

    #if len(favlist) > 0:
        #print favlist

    return render(request, 'redapp/favorites.html', {"favlist": favlist,
                                                    "glist": listsreturn.getGlist(),
                                                    "thumbnailSize": THUMBNAIL_SIZE,
                                                    "sideList": listsreturn.get_quickList(),
                                                    })

