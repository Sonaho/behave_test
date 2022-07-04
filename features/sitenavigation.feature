Feature:	Load and navigate for web

	Scenario: Load pypi.org site and search 
		Given I launch Chrome browser
		When I open "<web>" and compare "<title>"
		When I search selenium
		Then I landing at page "https://pypi.org/search/?q=selenium"

	Examples: 
     | web                           | title                           |
     | https://pypi.org			     | PyPI · The Python Package Index |