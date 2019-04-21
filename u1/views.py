from django.shortcuts import render

def home_view(request):
    return render(request,'home.html')
def movies_view(request):
    news1='In Telugu DEVDas movie is not bad'
    news2='Salman Updating minimum 100 Crores Gurantee for his movies'
    news3='Sonali slsowly getting curring'
    news4='Amitabh Bacchan next movie is Thugs of Hindustan'
    news5='Salman and Karina going to marry soon'
    my_dict={'news1':news1,'news2':news2,'news3':news3,'news4':news4,'news5':news5}
    return render(request,'movies.html',my_dict)
def sports_view(request):
    sports1='In ipl csk points in first'
    sports2='mi leads to the second position'
    my_dict1={'sports1':sports1,'sports2':sports2}
    return render(request,'sports.html',my_dict1)
def politics_view(request):
    politics1='there are three position parties in ap'
    politics2='present situation is two parities mainly trending'
    my_dict2={'politics1':politics1,'politics2':politics2}
    return render(request,'politics.html',my_dict2)
