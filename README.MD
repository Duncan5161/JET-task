# Interview Task

# Technologies used 
1. Python: Underlying code including route for the web page and extracting data from the API
2. Flask: Programme written using the Flask web framework.
3. HTML: Used to render the web pages.
4. CSS: Used via a stylesheet to produce the basic visual rendering seen on the web app.
5. Jinja: Loops used to render information via dictionaries. 

# Installation 
1.  Clone the repository: `git clone <https://github.com/Duncan5161/JET-task>` 
2.  Create a virtual environment: `python3 -m venv venv`
3.  Activate the environment: `source venv/bin/activate`
4.  Install dependencies: `pip install -r requirements.txt

# Usage
1. Navigate to the the project directory: 'cd JET'
2. Run the application: "Flask Run'
3. Access the app in your browser: http://127.0.0.1:5000

# Design choices
## General
I chose to present my results in a table rendered via Flask using Python and Jinja. I put the data into a dictionary then appended each restaurants data to a list for rendering. I felt this gave me a good level of control over the data, e.g. for rendering the address using different data sets. 

## Ratings
I have chosen to add a written statement where there are no ratings recorded, to avoid it appearing that said restaurants have a rating of 0. 

# Improvements I would make with more time 
## Data validation
I have only put minimal data validation onto the interface from the front end with the required tag and character limit included as part of the form where the postcode is entered - if the user enters a six digit but incorrect postcode it simply shows no results. I would instead return an error message briefly then redirect to the index page. 

## Front End
The front end is minimal and could be improved, again with more time, including using some Boostrap features. 

## Cuisines 
I have only displayed the first two cuisines that are listed for each restaurant - though this does make a degree of sense as listing more would look ungainly.


