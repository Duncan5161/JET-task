
# Running solution 
Run the application using Flask Run and open the link to the development server, then once the page has loaded enter the postcode of your choice to see the first ten restaurants in that area. If there are fewer than ten, all will be displayed. 

# Design choices
## General
I chose to present my results in a table rendered via Flask using Python and Jinja. I put the data into a dictionary then appended each restaurants data to a list for rendering. I felt this gave me a good level of control over the data, e.g. for rendering the address using different data sets. 

## Print statements
I have left in print statements as I use these during creation to ensure the program as expected, and to show my thought process. 

## Ratings
I have chosen to add a written statement where there are no ratings recorded, to avoid it appearing that said restaurants have a rating of 0. 

## Filtering data
I tried to ensure that only the data needed was passed to the HTML page, so rather than filtering on the front end via JavaScript, I made sure only the required data was sent across.

# Assumptions
## Returned restaurants
The brief states the first ten restaurants returned but it did not say if they should be sorted on a certain basis - this might make sense, e.g. on rating. If I had longer to work on this I would have implemented such a solution.

# Improvements
## Data validation
I have only put minimal data validation onto the interface from the front end with the required tag and character litmit included as part of the form where the postcode is entered - if the user enters a six digit but incorrect postcode it simply shows no results. I would instead return an error message briefly then redirect to the index page. 

## Front End
The front end is minimal and could be improved, again with more time, including using some Boostrap features. 

## Cuisines 
I have only displayed the first two cuisines that are listed for each restaurant - though this does make a degree of sense.

## Testing
I would undertake further testing given more time, including on edge cases but potentially also speed. 

## DRY principle
I feel I have somewhat violated the DRY principle by listing an identical dictionary in both the the POST and GET methods. 