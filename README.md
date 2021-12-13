# Challenge-2
FinTech Challenge for module 2
 Project Title

Loan Qualifier app

---

## Technologies

This application is written using Python 3.9.7 and uses Fire to enable using the command line interface [Fire documentation] (https://google.github.io/python-fire/guide/) and Questionary to query user input on CLIs [Questionary documentation (https://questionary.readthedocs.io/en/stable/index.html) to libraries.
User input includes credit score, monthly debt, monthly income, loan amount and home value. In addition, an option to save qualifying loans to a csv file is included.

---

## Installation Guide

Install Fire and Questionary libraries before running the loan qualifier app. 

`pip install fire` 

`pip install questionary`.

---

## Usage



Run the program from the command line as `python3 app4.py`. 

When prompted, enter the relative path to the daily rate sheet csv file from the banks offering loans. 

You will then be prompted to enter the applicant credit score, monthly debt payment, monthly income, loan amount and home valuation. 

The program will output the debt to income and loan amount to home value ratios, and the number of banks that offer qualifying loans.

![screen shot](/Users/Hockenbery/Desktop/Screen\ Shot\ 2021-12-09\ at\ 9.31.10\ AM.png )

The program will ask whether the applicant wants to save the list of qualifying bank loans to a csv file. If yes, the applicant will input a filepath for the csv file and the csv file will be generated. 

![screen shot](/Users/Hockenbery/Desktop/Screen\ Shot\ 2021-12-12\ at\ 10.20.00\ PM.png)

## Contributors

This program was written by David Hockenbery with the assistance of the UW FinTech class of 2021 and instructors. Contact David at dhockenb@gmail.com. 

---

## License

Copyright (c) [2021] [David Hockenbery]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
