import requests, re
import json

#from bs4 import BeautifulSoup

# Ana URL
BASE_URL = 'https://monitoringapi.solaredge.com'

# Santraller bu istekte geliyor
link1 = '/sites/list?size=6&searchText=Turkey&sortProperty=name&sortOrder=ASC&api_key='

token = 'L6HKIVFN4PMX7272IQ1NI3GNZL8H3R3M' # Admin
token2 = 'XJDAZ7ZL1YO4IP5VME5MUGMB7Z67B715' # User
url3 = BASE_URL + '/site/1824266/details.json?api_key=' + token
url4 = BASE_URL + '/site/1824266/overview.json?api_key=' + token
url5 = BASE_URL + '/site/1824266/powerDetails?api_key=' + token
url6 = BASE_URL + '/site/1824266/inventory?api_key='+token



url7 = BASE_URL+link1+token2
url2 = 'https://monitoringapi.solaredge.com/sites/list?size=6&searchText=Lyon&sortProperty=name&sortOrder=ASC&api_key='+ token


print(url7)

headers = {
    'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.1.1; en-gb; Build/KLP) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30'
    }
r = requests.get(url7,
                 headers={'Accept': "application/json"},
                 )
"""

r1 = requests.get(url3,
                 #headers={'Accept': 'application/vnd.github.v3.text-match+json'},
                 headers={'Accept': "application/json"},
                 )
r2 = requests.get(url4,
                 #headers={'Accept': 'application/vnd.github.v3.text-match+json'},
                 headers={'Accept': "application/json"},
                 )
r3 = requests.get(url5,
                 #headers={'Accept': 'application/vnd.github.v3.text-match+json'},
                 headers={'Accept': "application/json"},
                 )
"""
resp_parsed = re.sub(r'^jsonp\d+\(|\)\s+$', '', r.text)
data = json.loads(resp_parsed)
#print(type(data))
#print(data.keys())
d = data['sites']['site']
#print(d)
print(type(d))
print(d[0]['name'])
print(d[0]['status'])

print(d[1]['name'])
print(d[1]['status'])

print(d[2]['name'])
print(d[2]['status'])

print(d[3]['name'])
print(d[3]['status'])

print(d[4]['name'])
print(d[4]['status'])

print(d[5]['name'])
print(d[5]['status'])

"""
print(data['sites']['site']['name'])
print(data['sites']['site']['status'])
print(data['sites']['site']['peakPower'])
"""
#print(r1.content)
#print(r2.content)
#print(r3.content)

#r = requests.get('https://monitoring.solaredge.com/solaredge-web/p/site/603955/#/dashboard', headers=headers)
#soup = BeautifulSoup(r.content, "html.parser")
#print(soup)

#kList = soup.find_all('a', attrs={'class': 'x4-component  se-site-overview-data-box-data x4-box-item x4-component-default'})


#<div class="x4-component  se-site-overview-data-box-data x4-box-item x4-component-default" id="component-1068">69.55 kW</div>



#print(kList)
"""
import dryscrape
from bs4 import BeautifulSoup
import sys


session = dryscrape.Session()
session.visit("https://monitoring.solaredge.com/solaredge-web/p/site/603955/#/dashboard")
response = session.body()
print(response)
soup = BeautifulSoup(response)
soup.find(id="intro-text")
r = requests.get("https://monitoring.solaredge.com/solaredge-web/p/site/603955/#/dashboard")
print(r.content)

"""

"""
sabah 7 -8 arası mesaj gelmesi istiyoruz .
İnvertör bazlı : totalActivePower:77864.0, bu veri alınacak
İnvertör haberleşme bilgis alınacak
"""

# Tüm Hesap üzerindeki Santrallerin Bilgileri
"""
https://monitoringapi.solaredge.com/sites/list?size=5&searchText=Turkey&sortProperty=name&sortOrder=ASC&api_key=XJDAZ7ZL1YO4IP5VME5MUGMB7Z67B715

<siteList>
<count>6</count>
<site>
<id>2176821</id>
<name>ABDULLAH YILMAZ GÜNEŞ GES</name>
<accountId>77057</accountId>
<status>Active</status>
<peakPower>28.925</peakPower>
<lastUpdateTime>2021-06-04</lastUpdateTime>
<installationDate>2021-03-30</installationDate>
<notes/>
<type>Optimizers & Inverters</type>
<publicSettings>
<isPublic>false</isPublic>
</publicSettings>
<location>
<country>Turkey</country>
<city>Mugla</city>
<address>Bodrum</address>
<address2/>
<zip>48400</zip>
<timeZone>Europe/Istanbul</timeZone>
<countryCode>TR</countryCode>
</location>
<alertQuantity>0</alertQuantity>
<highestImpact>0</highestImpact>
<primaryModule>
<manufacturerName>Winasol</manufacturerName>
<modelName>2H-60M3-325</modelName>
<maximumPower>325.0</maximumPower>
<temperatureCoef>0.0</temperatureCoef>
</primaryModule>
<uris>
<uri key="SITE_IMAGE">/site/2176821/siteImage/AYG.jpeg</uri>
<uri key="DATA_PERIOD">/site/2176821/dataPeriod</uri>
<uri key="DETAILS">/site/2176821/details</uri>
<uri key="OVERVIEW">/site/2176821/overview</uri>
</uris>
</site>
<site>
<id>1061237</id>
<name>ALKOR GES</name>
<accountId>77057</accountId>
<status>Active</status>
<peakPower>50.0</peakPower>
<lastUpdateTime>2021-06-04</lastUpdateTime>
<installationDate>2019-04-03</installationDate>
<notes/>
<type>Optimizers & Inverters</type>
<publicSettings>
<isPublic>false</isPublic>
</publicSettings>
<location>
<country>Turkey</country>
<city>izmir</city>
<address>izmir</address>
<address2/>
<zip>20000</zip>
<timeZone>Europe/Istanbul</timeZone>
<countryCode>TR</countryCode>
</location>
<alertQuantity>0</alertQuantity>
<highestImpact>0</highestImpact>
<primaryModule>
<manufacturerName>Hanwha Q-Cells</manufacturerName>
<modelName>310</modelName>
<maximumPower>310.0</maximumPower>
<temperatureCoef>0.0</temperatureCoef>
</primaryModule>
<uris>
<uri key="SITE_IMAGE">/site/1061237/siteImage/8356.jpg</uri>
<uri key="DATA_PERIOD">/site/1061237/dataPeriod</uri>
<uri key="DETAILS">/site/1061237/details</uri>
<uri key="OVERVIEW">/site/1061237/overview</uri>
</uris>
</site>
<site>
<id>603955</id>
<name>CELAL BAYAR ÜNİVERSİTESİ GES</name>
<accountId>77057</accountId>
<status>Active</status>
<peakPower>334.8</peakPower>
<lastUpdateTime>2021-06-04</lastUpdateTime>
<installationDate>2017-12-10</installationDate>
<notes/>
<type>Optimizers & Inverters</type>
<publicSettings>
<name>Manisa</name>
<isPublic>true</isPublic>
</publicSettings>
<location>
<country>Turkey</country>
<city>Manisa</city>
<address>Muradiye</address>
<address2/>
<zip>45110</zip>
<timeZone>Europe/Istanbul</timeZone>
<countryCode>TR</countryCode>
</location>
<alertQuantity>1</alertQuantity>
<highestImpact>2</highestImpact>
<primaryModule>
<manufacturerName>Heckert</manufacturerName>
<modelName>270 P</modelName>
<maximumPower>270.0</maximumPower>
</primaryModule>
<uris>
<uri key="PUBLIC_URL">
https://monitoring.solaredge.com/solaredge-web/p/public?name=Manisa
</uri>
<uri key="SITE_IMAGE">
/site/603955/siteImage/D98CDEF2-9A5A-40C1-A786-5DF338222F74.jpeg-768.jpg
</uri>
<uri key="DATA_PERIOD">/site/603955/dataPeriod</uri>
<uri key="DETAILS">/site/603955/details</uri>
<uri key="OVERVIEW">/site/603955/overview</uri>
</uris>
</site>
<site>
<id>2205847</id>
<name>GALETOS GES</name>
<accountId>77057</accountId>
<status>Active</status>
<peakPower>259.2</peakPower>
<lastUpdateTime>2021-06-04</lastUpdateTime>
<installationDate>2021-04-20</installationDate>
<notes/>
<type>Optimizers & Inverters</type>
<publicSettings>
<isPublic>false</isPublic>
</publicSettings>
<location>
<country>Turkey</country>
<city>Izmir</city>
<address>Kemalpaşa OSB Ulucak Mevkii</address>
<address2/>
<zip>35730</zip>
<timeZone>Europe/Istanbul</timeZone>
<countryCode>TR</countryCode>
</location>
<alertQuantity>0</alertQuantity>
<highestImpact>0</highestImpact>
<primaryModule>
<manufacturerName>Winasol</manufacturerName>
<modelName>2H-72M3-400</modelName>
<maximumPower>400.0</maximumPower>
<temperatureCoef>-0.38</temperatureCoef>
</primaryModule>
<uris>
<uri key="SITE_IMAGE">
/site/2205847/siteImage/WhatsApp%2520Image%25202021-04-21%2520at%252016.31.13.jpeg
</uri>
<uri key="DATA_PERIOD">/site/2205847/dataPeriod</uri>
<uri key="DETAILS">/site/2205847/details</uri>
<uri key="OVERVIEW">/site/2205847/overview</uri>
</uris>
</site>
<site>
<id>1824266</id>
<name>MEGASUT GES</name>
<accountId>77057</accountId>
<status>Active</status>
<peakPower>538.2</peakPower>
<lastUpdateTime>2021-06-04</lastUpdateTime>
<installationDate>2020-09-25</installationDate>
<notes/>
<type>Optimizers & Inverters</type>
<publicSettings>
<isPublic>false</isPublic>
</publicSettings>
<location>
<country>Turkey</country>
<city>AYDIN</city>
<address>Umurlu AOSB</address>
<address2/>
<zip>09630</zip>
<timeZone>Europe/Istanbul</timeZone>
<countryCode>TR</countryCode>
</location>
<alertQuantity>0</alertQuantity>
<highestImpact>0</highestImpact>
<primaryModule>
<manufacturerName>HT-SAAE</manufacturerName>
<modelName>HT-SAEE HT-72-156M</modelName>
<maximumPower>380.0</maximumPower>
</primaryModule>
<uris>
<uri key="SITE_IMAGE">/site/1824266/siteImage/MEGAS%25C3%259CT.jpg</uri>
<uri key="DATA_PERIOD">/site/1824266/dataPeriod</uri>
<uri key="DETAILS">/site/1824266/details</uri>
<uri key="OVERVIEW">/site/1824266/overview</uri>
</uris>
</site>
<site>
<id>521013</id>
<name>TED DENİZLİ KOLEJİ GES</name>
<accountId>77057</accountId>
<status>Active</status>
<peakPower>514.63</peakPower>
<lastUpdateTime>2021-06-04</lastUpdateTime>
<installationDate>2017-08-16</installationDate>
<notes/>
<type>Optimizers & Inverters</type>
<publicSettings>
<isPublic>false</isPublic>
</publicSettings>
<location>
<country>Turkey</country>
<city>Denizli</city>
<address>1. Sokak, 2</address>
<address2/>
<zip>20050</zip>
<timeZone>Europe/Istanbul</timeZone>
<countryCode>TR</countryCode>
</location>
<alertQuantity>1</alertQuantity>
<highestImpact>2</highestImpact>
<primaryModule>
<manufacturerName>Heckert</manufacturerName>
<modelName>270 P</modelName>
<maximumPower>270.0</maximumPower>
</primaryModule>
<uris>
<uri key="SITE_IMAGE">
/site/521013/siteImage/havaalan%25C4%25B1%2520billboard.jpg
</uri>
<uri key="DATA_PERIOD">/site/521013/dataPeriod</uri>
<uri key="DETAILS">/site/521013/details</uri>
<uri key="OVERVIEW">/site/521013/overview</uri>
</uris>
</site>
</siteList>

"""


# Proje Bazlı İnvertör Bilgileri Linki
"""
Bu Linkte Proje Bazlı İnvertör Bilgileri geldi

https://monitoringapi.solaredge.com/site/1824266/inventory?api_key=L6HKIVFN4PMX7272IQ1NI3GNZL8H3R3M

b'{"Inventory":
    {"meters":[],
    "sensors":[],
    "gateways":[],
    "batteries":[],
    "inverters":[
        {   "name":"Inverter 1",
             "manufacturer":"SolarEdge",
             "model":"SE82.8K-RW0P0BNY4",
             "communicationMethod":"RS485",
             "dsp1Version":"1.13.1646",
             "dsp2Version":"2.19.1429",
             "cpuVersion":"4.10.25",
             "SN":"7E097F4B-51",
             "connectedOptimizers":138},
        {  "name":"Inverter 2",
            "manufacturer":"SolarEdge",
            "model":"SE82.8K-RW0P0BNY4",
            "communicationMethod":"RS485",
            "dsp1Version":"1.13.1781",
            "dsp2Version":"2.19.1440",
            "cpuVersion":"4.12.28",
            "SN":"7E097F73-79",
            "connectedOptimizers":138},
        {   "name":"Inverter 3",
            "manufacturer":"SolarEdge",
            "model":"SE82.8K-RW0P0BNY4",
            "communicationMethod":"RS485",
            "dsp1Version":"1.13.1646",
            "dsp2Version":"2.19.1429",
            "cpuVersion":"4.10.25",
            "SN":"7E096538-24",
            "connectedOptimizers":138},
        {   "name":"Inverter 4",
            "manufacturer":"SolarEdge",
            "model":"SE82.8K-RW0P0BNY4",
            "communicationMethod":"RS485",
            "dsp1Version":"1.13.1646",
            "dsp2Version":"2.19.1429",
            "cpuVersion":"4.10.25",
            "SN":"7E09814C-54",
            "connectedOptimizers":138},
        {   "name":"Inverter 5",
            "manufacturer":"SolarEdge",
            "model":"SE82.8K-RW0P0BNY4",
            "communicationMethod":"ETHERNET",
            "dsp1Version":"1.13.1646",
            "dsp2Version":"2.19.1429",
            "cpuVersion":"4.10.25",
            "SN":"7E097F66-6C",
            "connectedOptimizers":138}]}}'

"""


# Bireysel İnvertör Üretim Bilgisi -> Üretim varsa, devrede çalışıyor bilgisi
"""
https://monitoringapi.solaredge.com/equipment/1824266/7E097F66-6C/data?startTime=2021-06-03%2021:10:00&endTime=2021-06-04%2021:14:00&api_key=L6HKIVFN4PMX7272IQ1NI3GNZL8H3R3M
 
<threePhaseInverterTelemetry>
<date>2021-06-04 15:27:39</date>
<totalActivePower>71551.0</totalActivePower>
<dcVoltage>747.375</dcVoltage>
<groundFaultResistance>2470.22</groundFaultResistance>
<powerLimit>100.0</powerLimit>
<totalEnergy>8.79752E7</totalEnergy>
<temperature>70.4796</temperature>
<inverterMode>MPPT</inverterMode>
<operationMode>0</operationMode>
<L1Data>
<acCurrent>101.727</acCurrent>
<acVoltage>233.312</acVoltage>
<acFrequency>50.0292</acFrequency>
<apparentPower>23861.0</apparentPower>
<activePower>23838.0</activePower>
<reactivePower>-1060.0</reactivePower>
<cosPhi>1.0</cosPhi>
</L1Data>
<vL1To2>404.594</vL1To2>
<vL2To3>404.969</vL2To3>
<vL3To1>404.875</vL3To1>
<L2Data>
<acCurrent>101.711</acCurrent>
<acVoltage>233.453</acVoltage>
<acFrequency>50.029</acFrequency>
<apparentPower>23886.0</apparentPower>
<activePower>23850.0</activePower>
<reactivePower>-992.0</reactivePower>
<cosPhi>1.0</cosPhi>
</L2Data>
<L3Data>
<acCurrent>101.766</acCurrent>
<acVoltage>234.453</acVoltage>
<acFrequency>50.0296</acFrequency>
<apparentPower>23870.0</apparentPower>
<activePower>23863.0</activePower>
<reactivePower>-1062.0</reactivePower>
<cosPhi>1.0</cosPhi>
</L3Data>
</threePhaseInverterTelemetry>

"""


# Bireysel Santral Bilgisi -> Buradaki aktiflik bilgisine göre Santral devrede ya da değil bilgisi üretilecek
"""
Bireysel Santral Bilgisi
https://monitoringapi.solaredge.com/sites/list?size=5&searchText=Lyon&sortProperty=name&sortOrder=ASC&api_key=L6HKIVFN4PMX7272IQ1NI3GNZL8H3R3M

<siteList>
<count>1</count>
<site>
<id>1824266</id>
<name>MEGASUT GES</name>
<accountId>77057</accountId>
<status>Active</status>
<peakPower>538.2</peakPower>
<lastUpdateTime>2021-06-04</lastUpdateTime>
<installationDate>2020-09-25</installationDate>
<notes/>
<type>Optimizers & Inverters</type>
<publicSettings>
<isPublic>false</isPublic>
</publicSettings>
<location>
<country>Turkey</country>
<city>AYDIN</city>
<address>Umurlu AOSB</address>
<address2/>
<zip>09630</zip>
<timeZone>Europe/Istanbul</timeZone>
<countryCode>TR</countryCode>
</location>
<primaryModule>
<manufacturerName>HT-SAAE</manufacturerName>
<modelName>HT-SAEE HT-72-156M</modelName>
<maximumPower>380.0</maximumPower>
</primaryModule>
<uris>
<uri key="SITE_IMAGE">/site/1824266/siteImage/MEGAS%25C3%259CT.jpg</uri>
<uri key="DATA_PERIOD">/site/1824266/dataPeriod</uri>
<uri key="INSTALLER_IMAGE">/site/1824266/installerImage/entegro%2520.png</uri>
<uri key="DETAILS">/site/1824266/details</uri>
<uri key="OVERVIEW">/site/1824266/overview</uri>
</uris>
</site>
</siteList>

"""


# İnvertör üzerindeki Tüm güç değerini veriyor - Tarih Aralığında Veriyor
"""
İnvertör üzerindeki tüm güç değeri - Tarih Aralığında Veriyor
https://monitoringapi.solaredge.com/site/1824266/powerDetails.json?startTime=2021-06-04%2014:00:00&endTime=2021-06-04%2015:31:00&api_key=L6HKIVFN4PMX7272IQ1NI3GNZL8H3R3M

{
    "powerDetails":
        {
            "timeUnit":"QUARTER_OF_AN_HOUR",
            "unit":"W",
            "meters":[{
                "type":"Production",
                "values":[
                    {"date":"2021-06-04 14:45:00",
                     "value":378234.34},
                    {"date":"2021-06-04 15:00:00",
                     "value":390352.3},
                    {"date":"2021-06-04 15:15:00",
                     "value":366695.7},
                    {"date":"2021-06-04 15:30:00",
                    "value":278777.3}
                    ]}]}}

"""