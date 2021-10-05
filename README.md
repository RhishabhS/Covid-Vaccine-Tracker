# Covid-Vaccine-Tracker

## Intro:
A simple tracker for vaccine slots on CoWIN using api's from API Setu
## Steps
### Step 1: Reciever lists
Fill the recievers excel sheet (recievers.xlsx) with all details in lower case. Ensure correct spellings. If you do not want to use either mail or whatsapp enter "no" (without quotes) instead
### Step 2: Whatsapp Web Automation setup
Install Google Chrome (for whatsapp automation) and chromedriver (https://chromedriver.chromium.org/downloads) if you dont have them already. 
Ensure that the version of chromedriver corresponds to that of Google chrome which is installed.
Or you can use drivers of other browsers (research!) and edit the automation part accordingly.
For the first use, connect to your whatsapp web using QR code on your phone. Your details are saved, so you won't need to do this everytime.
Edit sleep times, depending on how much time it takes to load completely on your computer
### Step 3: Mail
Set up a mail server account (Gmail account or any other domain) and edit the parts of the code used for sending the mail(commented in code)
### Step 4: District id setup
Manually look up district ID's for corresponding districts (district_id_mapping.xlsx) and write accordingly (Code for obtaining this file using API's is attached). Or you can use VLOOKUP in excel to automatically fill it for you.
### Step 5: Miscellaneous
Convert xlsx to csv if you don't have excel (use read_csv/ to_csv() instead of read_excel/ to_excel() etc.)
### Enjoy!!!
Word of caution: Last tested on 04/10/2021. Do not misuse the automation part of whatsapp for spamming etc. You may get banned as per whatsapp policies.
