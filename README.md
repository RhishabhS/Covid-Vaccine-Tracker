# Covid-Vaccine-Tracker

##Intro:
A simple tracker for vaccine slots on CoWIN using api's from API Setu

This is a basic program that uses data from cowin api to send mails and whatsapp messages using selenium and pandas. The reciever list is an excel file named "receivers". Enter data in that file and run the program. Note that this program will run 10000 times before terminating so check accordingly. To send whatsapp messages the program uses Whatsapp web. So to configure for the first time you might need a qr code but afterwards the process is automatic (stores it as a cookie). To use whatsapp web the phone having whatsapp should be connected to the internet and expected internet speed is around 2-3 mbps for proper functioning.
(You may alter sleep time for slow internet speeds)
Mail is sent using a sample gmail account. It is advised that you alter the gmail account for your own purposes.

NOTE: If you do not want to use either mail or whatsapp channels for communication you MUST fill "no"(without the quotes of course) instead, in respective fields.

Caution: Use this program responsibly, do not misuse the automation part to spam others, you may be banned by whatsapp as per it's policies
