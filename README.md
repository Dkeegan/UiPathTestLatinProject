# UiPathTestLatinProject
A UiPath project that automates user testing of my Latin project
The Latin project makes a call to the wikipedia api but it is not guranteed to have pictures. 

It loads the webpage of https://github.com/Dkeegan/Visual-latin - it is set to the default port numbers.
This cycles through calling random chapters for a given amount of calls.
Checks to see if pictures or text is returned.
Writes the word,chapter, and a binary check.

This also has the side affect of gameifying the program. 

There is a sample python script to determine the percentage of results have pictures.

ToDo: 
Checks if Pexels returns pictures 
