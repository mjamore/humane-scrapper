This is a script to scrape my local humane society website and notify me via email when dogs are are available that match the criteria I'm looking for.

To-Do:
	- Clean up code and refactor into functions


Feature Requests:
	- write contents to a file and only notify me when changes are made

Completed:

	- check if energy level is equal to our values
		- if it is, then check if size matches as well
			- if it does, add dog to JSON object
	- scrape the page (https://www.chittendenhumane.org/Dogs) and notify when there are new additions that are not already adopted
	- go to the details page and only notify me of medium or low level energy dogs
	- if relative_details_links length doesn't equal final output, send me email.  This will help catch human input errors into the cms, i.e. energy level value "high- ...." or "low: ..."


Current Issue:
	- when changing the filter options in criteria.json from more options to less options, we are not seeing the log message 'There have not been any new dogs added that meet the specified criteria.\n'			