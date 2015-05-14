import praw
import json
import requests
import BeautifulSoup
import re
import urllib
import os
import pprint

user_agent = ("blah")
r = praw.Reddit(user_agent = user_agent)

GRABSIZE = 30
thumbnailSize = 'm'
debugcheck = 1

def innerReformURL(newURL):


    print "before innerReformURL newURL is " + newURL
    if 'https://' in newURL:
        newURL = 'http://' + newURL[8:]
    if 'http://imgur' in newURL:
        #print "inner case 1"
        newURL = "i." + newURL[7:]
        #print "after inner case 1 newURL is " + newURL
    elif 'http://m.' in newURL:
        #print "inner case 2"
        newURL = "i." + newURL[9:]
        #print "stripping m. to "
        #print "after inner case 2 newURL is " + newURL
    elif 'http://www.' in newURL:
        #print "inner case 3"
        newURL = "i." + newURL[11:]
        #print "after inner case 3 newURL is " + newURL
    elif 'http://i.' in newURL:
        #print "inner case 4"
        newURL = newURL[7:]
        #print "after inner case 4 newURL is " + newURL
    elif (newURL[0:4] == "imgur"):
        #print "inner case 5"
        newURL = "i." + newURL
        #print "after inner case 5 newURL is " + newURL

    newURL = 'i' + newURL[12:]
    print "at stage 1 newURL is " + newURL

    if (newURL[-3:] == 'jpg'):
        if (len(newURL) == 11 or len(newURL)== 13):
            #print "thumbnail found in newURL as " + newURL
            newURL = newURL[:-5] + 'j'
            #print "after stripping thumbnail, newURL is " + newURL
        else: newURL = newURL[:-4] + 'j'

    elif (newURL[-4:] == 'jpeg'):
        if debugcheck == 1:
            print "jpeg found as " + newURL
        if (len(newURL) == 12 or len(newURL)== 14):
            #print "thumbnail found in newURL as " + newURL
            newURL = newURL[:-6] + 'j'
            #print "after stripping thumbnail, newURL is " + newURL
        else: newURL = newURL[:-5] + 'j'

        if debugcheck == 1:
            print "after stripping, newURL is " + newURL

        """
        if ((newURL[-5] == 't' or newURL[-5] == 'm' or newURL[-5] == 'l' or newURL[-5] == 'h' or newURL[-5] == 's' or newURL[-5] == 'b') and newURL[-12] != '/'):
            #print 'found thumbnail, replacing with l.jpg'
            newURL = newURL[:-5] + 'j'
        else:
            #print 'did not find thumbnail, converting to large thumbnail'
            newURL = newURL[:-4] + 'j'
        """

    elif(newURL[-4:] == 'gifv'):
        newURL = newURL[:-5] + 'g'
        newURL = newURL

    elif(newURL[-3:] == 'gif'):
        newURL = newURL[:-4] + 'g'
        newURL = newURL

    elif(newURL[-3:] == 'png'):
        newURL = newURL[:-4] + 'p'
        newURL = newURL


    else:
        #print 'Not a jpg, no thumbnail code'
        newURL = newURL + 'j'

    #print "after innerReformURL newURL is " + newURL
    return newURL

def innerReformGfy(newURL):
    if debugcheck == 1:
        print "starting innerReformGfy"

    if "https://" in newURL:
        newURL = newURL[8:]
    elif "http://" in newURL:
        newURL = newURL[7:]

    newURL = 'g' + newURL[newURL.index('/')+1:]

    while not (newURL.isalpha()):
        newURL = newURL[:-1]




    """
    if newURL[:5] == "zippy":
        newURL = 'g' + newURL[17:]
    elif newURL[:3] == "fat":
        newURL = 'g' + newURL[15:]
    elif newURL[:3] == "www":
        newURL = 'g' + newURL[15:]
    elif newURL[:5] == "giant":
        newURL = 'g' + newURL[17:]
    """
    print "gfycat changing to " + newURL
    return newURL

def reformURL(newURL):
    if debugcheck ==1:
        print "starting reformURL"
    urlList = []
    #print "starting reformURL"
    appendThis = 0
    if newURL[-2] == '?':
        newURL = newURL[:-2]
    if 'imgur.com/a/' in newURL and ',' not in newURL:
        #print("Case 1 " + newURL)
        match = re.match('(https?)\:\/\/(www\.)?(?:m\.)?imgur\.com/a/([a-zA-Z0-9]+)(#[0-9]+)?', newURL)
        if match:
            #raise ImgurAlbumException("URL must be a valid Imgur Album")

            subProtocol = match.group(1)
            subAlbum_key = match.group(3)
            noscriptURL = "http://imgur.com/a/" + subAlbum_key + "/noscript"
            subResponse = urllib.urlopen(noscriptURL)
            if subResponse.getcode() == 200:

                html = subResponse.read().decode('utf-8')
                foundImages = re.findall('<img src="(\/\/i\.imgur\.com\/([a-zA-Z0-9]+\.(jpg|jpeg|png|gif)))"', html)#,html
                for image in foundImages:
                    line = image[0][2:]
                    newURL = line
                    #print("newURL is starting as " + newURL)
                    #print"########################################################################################"

                    newURL = innerReformURL(newURL)



                    #print("newURL is ending as " + newURL)
                    appendThis = 1
                    urlList.append(newURL)
            else:
                print "no album match"

    elif ( "imgur.com/a/" in newURL and newURL[-4] != '.' and newURL[-5] != '.'):
        #print("Case 2 " + newURL)
        noscriptURL = newURL
        subResponse = urllib.urlopen(noscriptURL)
        if subResponse.getcode() == 200:
        #    raise ImgurAlbumException("Error reading Imgur: Error Code " + str(subResponse.getcode()))
            html = subResponse.read().decode('utf-8')
            #foundImages = re.findall('<img src="(\/\/i\.imgur\.com\/([a-zA-Z0-9]+\.(jpg|jpeg|png|gif)))"', html)#,html
            foundImages = re.findall('<img src="(\/\/imgur\.com\/([a-zA-Z0-9]+\.(jpg|jpeg|png|gif)))"', html)#,html
            #print("len foundImages = " + str(len(foundImages)))
            if len(foundImages) > 0:
                for image in foundImages:
                    #print("Case 2 Found Image " + str(image))
                    line = image[0][2:]
                    newURL = line
                    #print"########################################################################################"

                    newURL = innerReformURL(newURL)

                    #print("newURL is ending as " + newURL)
                    appendThis = 1
                    urlList.append(newURL)
                    #print urlList
    elif ("gfycat.com" in newURL):
        print "gfycat image"
        newURL = innerReformGfy(newURL)
        appendThis = 1
        urlList.append(newURL)

    else:
        #print("Case 3 " + newURL)
        #print("newURL is starting as " + newURL)

        #print"########################################################################################"

        newURL = innerReformURL(newURL)

        #print("newURL is ending as " + newURL)
        appendThis = 1
        urlList.append(newURL)
    if appendThis == 1:
        #print "#printing urlList"
        #print urlList
        return urlList
    else:
        return None


def getSubmissionsInSubreddit(subreddit):
    print 'running getSubmissionsInSubreddit'
    print str(subreddit)
    print 'blah'
    submissionList = []
    workingList = []
    appendThis = 0
    lastItem = None
    print subreddit

    returnedSubmissions = r.get_subreddit(subreddit).get_hot(limit=GRABSIZE)

    print "finished getting subreddit"
    print returnedSubmissions

    for submission in returnedSubmissions:
        lastItem = submission.name
        if submission.url not in submissionList:
            submissionList.append(submission.url)
            urlList = []
            print "submission url is"
            print submission.url

            if ("imgur" in submission.url and "gallery" not in submission.url):
                if(submission.author != None):
                    redditorname = submission.author.name
                else:
                    redditorname = "blank"
                subTitle = submission.title
                newURL = submission.url

                # Testing new function here
                print "calling reformURL"
                urlList = reformURL(newURL)


                if urlList != None:
                    submissionSubreddit = str(submission.subreddit)
                    workingList.append([redditorname, subTitle, urlList, len(urlList), submission.url, submission.permalink, submissionSubreddit])

            elif ("gfycat" in submission.url):
                if debugcheck ==1:
                    print "gfycat in submission.url"
                if(submission.author != None):
                    redditorname = submission.author.name
                else:
                    redditorname = "blank"

                subTitle = submission.title
                urlList = reformURL(submission.url)

                if urlList != None:
                    submissionSubreddit = str(submission.subreddit)
                    workingList.append([redditorname, subTitle, urlList, len(urlList), submission.url, submission.permalink, submissionSubreddit])



    print 'finishing getSubmissionsInSubreddit'

    if len(workingList) > 0:
        return [workingList, lastItem]
    else:
        return None

def getExtraSubmissionsInSubreddit(subreddit, page):
    print 'running getExtraSubmissionsInSubreddit'
    submissionList = []
    workingList = []
    appendThis = 0
    lastItem = None
    print page
    print subreddit

    returnedSubmissions = r.get_subreddit(subreddit).get_hot(params={'limit':GRABSIZE, 'after': page})

    print "finished getting subreddit"
    print returnedSubmissions

    for submission in returnedSubmissions:
        lastItem = submission.name
        if submission.url not in submissionList:
            submissionList.append(submission.url)
            urlList = []
            print "submission url is"
            print submission.url

            if ("imgur" in submission.url and "gallery" not in submission.url):
                if(submission.author != None):
                    redditorname = submission.author.name
                else:
                    redditorname = "blank"
                subTitle = submission.title
                newURL = submission.url

                # Testing new function here
                print "calling reformURL"
                urlList = reformURL(newURL)


                if urlList != None:
                    submissionSubreddit = str(submission.subreddit)
                    workingList.append([redditorname, subTitle, urlList, len(urlList), submission.url, submission.permalink, submissionSubreddit])

            elif ("gfycat" in submission.url):
                if debugcheck ==1:
                    print "gfycat in submission.url"
                if(submission.author != None):
                    redditorname = submission.author.name
                else:
                    redditorname = "blank"

                subTitle = submission.title
                urlList = reformURL(submission.url)

                if urlList != None:
                    submissionSubreddit = str(submission.subreddit)
                    workingList.append([redditorname, subTitle, urlList, len(urlList), submission.url, submission.permalink, submissionSubreddit])

    print 'finishing getExtraSubmissionsInSubreddit'
    if len(workingList) > 0:
        return [workingList, lastItem]
    else:
        return None


def getSubmissionsInRedditor(redditor):
    print 'running getSubmissionsInRedditor'
    print str(redditor)
    print 'blah'
    submissionList = []
    workingList = []
    appendThis = 0
    lastItem = None
    print redditor

    returnedSubmissions =  r.get_redditor(redditor).get_submitted(limit=GRABSIZE)

    print "finished getting redditor"
    print returnedSubmissions

    for submission in returnedSubmissions:
        lastItem = submission.name
        print "checking for url in submisisonList"
        if submission.url not in submissionList:
            submissionList.append(submission.url)
            urlList = []
            print "submission url is"
            print submission.url

            if ("imgur" in submission.url and "gallery" not in submission.url):
                if(submission.author != None):
                    redditorname = submission.author.name
                else:
                    redditorname = ""
                subTitle = submission.title
                newURL = submission.url

                # Testing new function here
                print "calling reformURL"
                urlList = reformURL(newURL)


                if urlList != None:
                    submissionSubreddit = str(submission.subreddit)
                    workingList.append([redditorname, subTitle, urlList, len(urlList), submission.url, submission.permalink, submissionSubreddit])

            elif ("gfycat" in submission.url):
                if debugcheck ==1:
                    print "gfycat in submission.url"
                if(submission.author != None):
                    redditorname = submission.author.name
                else:
                    redditorname = "blank"

                subTitle = submission.title
                urlList = reformURL(submission.url)

                if urlList != None:
                    submissionSubreddit = str(submission.subreddit)
                    workingList.append([redditorname, subTitle, urlList, len(urlList), submission.url, submission.permalink, submissionSubreddit])

                    #print workingList
    print 'finishing getSubmissionsInRedditor'
    if len(workingList) > 0:
        return [workingList, lastItem]
    else:
        return None

def getExtraSubmissionsInRedditor(redditor, page):
    print 'running getExtraSubmissionsInRedditor'
    submissionList = []
    workingList = []
    appendThis = 0
    lastItem = None
    print page
    print redditor

    returnedSubmissions = r.get_redditor(redditor).get_submitted(params={'limit': GRABSIZE, 'after': page})


    print "finished getting extra redditor"
    print returnedSubmissions

    for submission in returnedSubmissions:
        print 'blahblah'
        lastItem = submission.name
        if submission.url not in submissionList:
            submissionList.append(submission.url)
            urlList = []
            print "submission url is"
            print submission.url

            if ("imgur" in submission.url and "gallery" not in submission.url):
                if(submission.author != None):
                    redditorname = submission.author.name
                else:
                    redditorname = "blank"
                subTitle = submission.title
                newURL = submission.url

                # Testing new function here
                print "calling reformURL"
                urlList = reformURL(newURL)


                if urlList != None:
                    submissionSubreddit = str(submission.subreddit)
                    workingList.append([redditorname, subTitle, urlList, len(urlList), submission.url, submission.permalink, submissionSubreddit])

            elif ("gfycat" in submission.url):
                if debugcheck ==1:
                    print "gfycat in submission.url"
                if(submission.author != None):
                    redditorname = submission.author.name
                else:
                    redditorname = "blank"

                subTitle = submission.title
                urlList = reformURL(submission.url)

                if urlList != None:
                    submissionSubreddit = str(submission.subreddit)
                    workingList.append([redditorname, subTitle, urlList, len(urlList), submission.url, submission.permalink, submissionSubreddit])

                    #print workingList
    print 'finishing getExtraSubmissionsInRedditor'
    if len(workingList) > 0:
        return [workingList, lastItem]
    else:
        return None