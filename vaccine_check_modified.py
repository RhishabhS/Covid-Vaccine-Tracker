import urllib.request, json
import datetime
import smtplib
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
# SCANNING PART
print("VACCINE SLOT CHECK v1.1")
print("Built using CoWIN API from API Setu.")
print("Built by Rhishabh Suneeth")

today_date=datetime.date.today()        
print("Initiating Slot check procedures....\n\n")
print("SLOT TRACKING LOG")
print("-----------------\n")
print("Today's Date: "+ today_date.strftime("%d-%m-%Y")+"\n")  
   
# ACCESSING COWIN API FOR ALL DAYS OF THE WEEK
for i in range(100000):
    now=datetime.datetime.now()
    print("**Checking for slots** ","["+now.strftime("%d-%m-%Y, %H:%M:%S")+"]")
    # READING RECIEVER LISTS
    df=pd.read_excel("recievers.xlsx")
    err_101=0
    num_of_days_to_be_checked=14
    for i,row in df.iterrows():
        c=[]
        flag=0
        for j in range(num_of_days_to_be_checked):
            d1=today_date+ datetime.timedelta(days=j)
            if row["date (checks after this date)"]>d1:
                continue
            d=d1.strftime("%d-%m-%Y")
            today6pm=now.replace(hour=18,minute=0,second=0,microsecond=0)
            if now>today6pm and j==0:
                continue
            try:
                url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id="+str(row["district_id"])+"&date="+d
                response=urllib.request.urlopen(url)
                data= json.loads(response.read())
            except:
                print("ERROR 101: <<COULD NOT CONNECT TO SERVER >>")
                print("REASON(S): NOT CONNECTED TO INTERNET or SERVER DOWN AT URL "+url)
                print("PERIODIC CHECKS WILL CONTINUE TILL CONNECTION IS RESTORED")
                err_101=1
                break
            if err_101==1:
                break      
            for i in data["sessions"]:
    
                if int(i["min_age_limit"]) not in [int(x) for x in str(row["age"]).split(",")]:
                    iflag1=0
                else:
                    iflag1=1
                if i["vaccine"].lower() not in [x for x in row["vaccine"].split(",")]:
                    iflag2=0
                    if row["vaccine"].lower()=="all":
                        iflag2=1
                
                else:
                    iflag2=1
                dose_no=str(row["dose"]).split(",")    
                for k in dose_no:
                    if i["available_capacity_dose"+k]==0:
                        iflag3=1
                    else:
                        iflag3=1
                        break
                if row["preferred centers"]=="all":
                    iflag4=1
                elif i["name"].lower() not in row["preferred centers"].split(","):
                    iflag4=0
                else:
                    iflag4=1
                iflag= iflag1*iflag2*iflag3*iflag4    
                if iflag==1:
                    flag=1
                    c.append(i)
        if flag==1:
            dfc=pd.DataFrame(c)
            print(dfc)
            print("SLOTS FOUND FOR <<"+ str(row["name"]).upper()+ ">>AT LOCATION <<"+ row["district"].upper()+">>")
            if not(row["mail"]=="no"):
                try:
                    s=smtplib.SMTP("smtp.gmail.com",587)
                    s.starttls()
                    s.login("vaccinecheckkannur@gmail.com","vaccine@123")
                except:
                    print("Gmail Login failed...Check connectivity and settings")
                    
                
            now=datetime.datetime.now()
            k=""
            for i in c:
                w=""
                if len(str(row["dose"]).split(","))==1:
                    w= "\nAvailable capacity dose"+str(row["dose"])+": "+ str(i["available_capacity_dose"+str(row["dose"])])
                    
                elif len(str(row["dose"]).split(","))==2:
                    for j in row["dose"].split(","):
                        w+="\nAvailable capacity dose "+str(j)+": "+ str(i["available_capacity_dose"+str(j)])
                                 
                k+="-----------------------------------------------\n\nCenter name: "+ i["name"]+"\nAddress: "+ i["address"]+" "+str(i["pincode"])+ "\nVaccine: "+ i["vaccine"]+"\n\nSlot date: "+ str(i["date"])+ "\n\nDose(s) requested: "+ str(row["dose"])+ w+"\n(As on "+ now.strftime("%d-%m-%Y, %H:%M:%S")+")" +"\n" + i["fee_type"] +",Cost: Rs "+ str(i["fee"])+"\n\n\n"
            body="Greetings "+ row["name"]+",\n\nWe have found the vaccine slots at the centers requested. Here are the details: \n\n"+k+ "\nYou are hereby requested to book the slots immedietely on https://selfregistration.cowin.gov.in/"+"\n\nRegards,\nVaccine check\n"
            print(k)
            if not row["mail"]=="no":
                print(row["mail"])
                msg="From: Vaccine Check <vaccinecheckkannur@gmail.com>\nTo:"+str(row["mail"])+"\nSubject: IMPORTANT: VACCINATION SLOTS FOUND- Details\n\n"+body
            body="Greetings "+ row["name"]+",\n\nWe have found the vaccine slots at the centers requested. Here are the details: \n"+k+ "You are hereby requested to book the slots immedietely on https://selfregistration.cowin.gov.in/"
            msg1= body
            if(row["whatsapp_id"]=="no"):
                flagw=0
            else:
                flagw=1  
                
            
            if flagw==1:
                try:
                   
                    for u in row["whatsapp_id"].split(","):
                        options=Options()
                        options.add_argument("user-data-dir=C:\environments\selenium")
                        options.add_experimental_option("excludeSwitches", ["enable-automation"])
                        options.add_experimental_option('useAutomationExtension', False)
                        driver = webdriver.Chrome("C:\\Users\\Rhishabh\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe",options=options)
                        driver.maximize_window()
                        driver.get("https://web.whatsapp.com")
                        for i in range(10):
                            try:
                                time.sleep(5)
                                search_xpath = '//*[@id="side"]/div[1]/div/label/div/div[2]'
                                search = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(search_xpath))
                                search.click()
                                ActionChains(driver).send_keys(u).perform()
                                ActionChains(driver).key_down(Keys.ENTER).perform()
                                time.sleep(3)
                                driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]').click()
                                time.sleep(3)
                                for b in body.split("\n"):
                                    ActionChains(driver).send_keys(b).perform()
                                    ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
                                ActionChains(driver).key_down(Keys.ENTER).perform()   
                                print("<< Message sent by Whatsapp to >>"+ u)
                                time.sleep(5)
                                driver.quit()
                            except:
                                continue
                            
                            break
                except:
                    print("Failed to send message by whatsapp.. Please ensure phone is cnnected to the internet.")
                    driver.quit()
                if not (row["mail"]=="no"):
                    try:
                        s.sendmail("vaccinecheckkannur@gmail.com",row["mail"],msg)
                        if not (row["mail"]=="no"):    
                            print("Message sent to "+ row["mail"],"at ",now.strftime("%d-%m-%Y, %H:%M:%S"))
                    except:
                        print("Failed to send mail.. Check internet connectivity")
            
        else:
            print("<<<NO SLOT FOUND FOR "+ row["name"]+">>>>\n")
    print("------------------------------------------------")       
    time.sleep(30)
