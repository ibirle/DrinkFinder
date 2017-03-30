from flask import *
from urllib2 import Request, urlopen, URLError
import json, ast, random

#This function parses through the json return from a Beer api
#and finds a random beer of the given style or a random style if the style 0 is given
def findStyle(style):
    search = ""
    style = int(style)

    catDic = [1,23,40,55,70,73,85,100,105,107,115,150]
    

    if style > 0:
        style = catDic[style-1]
        search = "&order=random&styleId=" + str(style)
    else:
        style = random.randint(1,150)
        search = "&order=random&&styleId=" + str(style)
        

    link = "http://api.brewerydb.com/v2/beers?key=1c58439ba5fb13b156425a7ea6959557"+search
    request = Request(link)
    response = []

    try:
        response = urlopen(request).read()
    except URLError, error:
        print error
        
    data = json.loads(response)
    results = []
    if style > 0:
        beers = data['data']
        results = beers[random.randint(0,len(beers)-1)]

    
    return results

#Finds a random wine of given style or random style if given 0
def getWine(style):
    if style == 8:
        style = random.randint(0,7)
    styleList = ["Red - Light & Fruity",
                 "Red - Smooth & Supple",
                 "Red - Earthy & Spicy",
                 "Red - Big & Bold",
                 "White - Light & Crisp",
                 "White - Fruity & Smooth",
                 "White - Rich & Creamy",
                 "Sweet"]
    
    styleDict = {"Red - Light & Fruity":610,
                 "Red - Smooth & Supple":611,
                 "Red - Earthy & Spicy":612,
                 "Red - Big & Bold":613,
                 "White - Light & Crisp":614,
                 "White - Fruity & Smooth":615,
                 "White - Rich & Creamy":616,
                 "Sweet":617}

    link = "http://services.wine.com/api/beta2/service.svc/JSON/catalog?apikey=325220f9fe2a3ea277a06b74277d7c03&size=100&filter=categories(" + str(styleDict[styleList[style]]) + ")"
    request = Request(link)

    try:
        response = urlopen(request).read()
    except(URLError):
        print(error)

    str_response = response.decode('utf-8')
    dic = json.loads(str_response)

    choice = random.choice(dic["Products"]["List"])
    return {"Name":choice["Name"], "Price":choice["PriceMax"], "URL":choice["Url"]}

#Here is where flask manages the html routing and data between pages and python script


#
#
#If you want to run this you have to set this file location to where ever you put img
app = Flask(__name__,static_folder='/root/DrinkFinder/img')
#
#
#

@app.route('/')
def homepage():
    return render_template('Alcohol.html')

@app.route('/wine.html')
def Wine():
    return render_template('wine.html')

@app.route('/beer.html')
def Beer():
    return render_template('beer.html')

@app.route('/beer2.html', methods=["GET"])
def Beer2():
    beer = findStyle(request.args['style'])
    try:
        Description=beer['description']
    except:
        Description = 'n/a'
        
    try:
        year='Year: ' + beer['year']
    except:
        year = ''    
        
    return render_template('beer2.html', name=beer['name'], Category=beer['style']['category']['name'], Description=Description)

@app.route('/wine2.html', methods=["GET"])
def Wine2():
    WD = getWine(int(request.args['style']))

    return render_template('wine2.html', name=WD["Name"], price=WD["Price"], url=WD["URL"])
    
    
#This method runs the app, without paramters it makes runs locally and gives you an ip to connect in the console
if __name__ == "__main__":
    app.run(host = "104.236.201.174")

