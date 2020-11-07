# Web scrapper for admin panel of insurance company
> This app is getting information about new tickets from insurance company like what device is that, what type of insurance is this etc.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)
* [Inspiration](#inspiration)
* [Contact](#contact)

## General info
This app was made to automate some of my work. It's written in Python using Selenium module.

This program is taking tickets numbers from Google Sheets. Then opens 'BASE_URL' of Insurance Company admin panel in Google Chrome. Next step is loggin to that panel. After succesfull login it takes tickets numbers list and one by one is opening all tickets to take all information about that ticket like what device is that, name of client, damage description etc. Finally, the program takes all the collected information and exports it to Google Sheets.

Data on insurer has been hidden and will not disclose them :)

## Technologies
* Python - version 3.9.0
* gspread - version 3.6.0
* Selenium - version 3.141.0

## Setup
Go to Resources and change SampleCredentialData.py to CredentialData.py. Fill it with your data.

Check Locators in Locators.py - if some of them has changed or stopped working you need to manually open ticket site, click F12, find specific element and then you need to right click on that element in code, and choose copy. Stay focused on type of locator (If it need ID or XPATH).

Change SampleSheetsData.json for your json file with generated json for gspread authentication

Open terminal in your project directory and type `python3 main.py` if you are on MacOS and Linux or `python main.py` on Windows.

## Features

To-do list:
* Change export method from all to single
* Change list of information to database
* Change Google Chrome for non header version

## Status
Project is: _in progress_

## Inspiration
Automation some of my work

## Contact
Created by gpachota.