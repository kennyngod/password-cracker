# Password Cracker
This is a tweaked program demonstrating how brute force password crackers work. There is a little more logic used rather than brute forcing each letter to each possible letter it could be. The section [Letter Frequency](#letter-frequency) has a bit more details on it.

## The Server
Note: this program does **NOT** accurately model how passwords are cracked and how they are stored. Instead, this program uses the most simplified process of how passwords are stored. Many servers are secured and use cryptography to store passwords in a secured way. This program only demonstrates at a shallow level the process of password cracking and the emphasize the importance of a secure password. 
# Letter Frequency
Because Python is powerful, it can "crack" any password at ease very quickly. But rather than brute forcing each letter in alphabetical order, it made sense to me that some letters will tend to be used more frequently than others. Here is the [source](http://letterfrequency.org) I used that ranked the frequency of each letter. For this project, I used "Letter Frequency in the English Language". I then add in numbers and symbols into the list of possible characters that could be used in the password.


## File Reading
I wrote each letter per row in an Excel sheet and CSV file. The program reads the CSV file first. If it is not found, then it will try to read in the excel file with the .xlsx extension. For the excel file, pandas library is used. You may notice in the code that there is a try except block for importing pandas and openpyxl. Although most Python users should have pandas installed by now, there many be a chance that they may not have openpyxl installed. So, I decided to practice safe coding under the assumption that there many be a user that does not have pandas and openpyxl installed.

# Future Plans
I plan on implementing a webpage version of this program so that a Python compiler is not needed to run this. I also plan on adding a file feature. Since cracking one string of password takes much less than a second (about a millisecond) to crack, a file containing many different passwords should be more interesting and time consuming. 

However, as of 2021-12-29 (Dec 29), I currently do not have the knowledge to implement such a software yet.

# Topics Practiced in This Project
* importing libraries
* reading files
  * reading different types of files
* error and exception handling
  * using try except clauses