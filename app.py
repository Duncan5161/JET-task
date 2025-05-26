
from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index(): 
    
    if request.method == "GET":

        Name = "Example Cafe" #Show example on landing page 
        Cuisines = "Italian and Hungarian"
        Rating = "1"
        Address = "5 Example Avenue"
        City = "Hove"
        Postcode = "BN3 511"
        restaurants = []
        dict = {"Name": Name,
                "Cuisines": Cuisines,
                "Rating": Rating,
                "Address": Address,
                "City": City,
                "Postcode": Postcode
                }
        
        restaurants.append(dict)
        return render_template("index.html",dict=restaurants)

    else: #if POST 
        #Get postcode from user 
        postcode = request.form.get("postcode")
        print(postcode)

        api_test = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"
        api_link = api_test 
        response = requests.get(api_link)

        headers = {
            "User-Agent": "Mozilla/5.0"  # Pretend to be a browser to access full API data (otherwise returned HTML)
        }

        response = requests.get(api_link, headers=headers)

        data = response.json()
       
        # get number of results
        result_count=data["metaData"]["resultCount"]
        print(result_count)
        if result_count < 10:
            i = result_count
        else:
            i = 10

        #loop over and add to list each time 
        restaurants = []
        for i in range(i):
            Name = data["restaurants"][i]["name"] #Name
            print(f"Name:{Name}")

            Cuisines = data["restaurants"][i]["cuisines"][0]["name"] #Cuisine
            print(f"Cuisines: {Cuisines}")
            Cuisines_1 = data["restaurants"][i]["cuisines"][1]["name"] #Cuisine
            print(f"Cuisines_1: {Cuisines_1}")

            Rating = data["restaurants"][i]["rating"]["starRating"] #Rating
            rating_count = data["restaurants"][i]["rating"]["count"]
            if rating_count == 0:
                Rating = 'No reviews submitted yet' #Prevents restaurants without reviews appearing as 0
            print(f"Rating: {Rating}")

            Address = data["restaurants"][i]["address"]["firstLine"] #Address
            print(f"Address: {Address}\n")
            City = data["restaurants"][i]["address"]["city"]
            Postcode = data["restaurants"][i]["address"]["postalCode"]

            dict = {
                "Name": Name,
                "Cuisines": Cuisines,
                "Cuisines_1":  Cuisines_1,
                "Rating": Rating,
                "Address":  Address,
                "City": City,
                "Postcode": Postcode
                }
            restaurants.append(dict)

        return render_template("index.html", dict=restaurants)




