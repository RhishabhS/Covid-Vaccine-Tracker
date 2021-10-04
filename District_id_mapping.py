import urllib.request,json
import pandas as pd
#Getting all state ids
url_state="https://cdn-api.co-vin.in/api/v2/admin/location/states"

response1=urllib.request.urlopen(url_state)
state_data=json.loads(response1.read())
district_data=[]
for i in state_data["states"]:
    url_districts="https://cdn-api.co-vin.in/api/v2/admin/location/districts/"+ str(i["state_id"])
    response2=urllib.request.urlopen(url_districts)
    data=json.loads(response2.read())
    for j in data["districts"]:
        j["state"]=i["state_name"]
        district_data.append(j)

df=pd.DataFrame(district_data)
print(df)
df.to_excel("district_id_mapping.xlsx")
    
