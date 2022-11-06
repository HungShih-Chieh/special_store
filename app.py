import streamlit as st
import requests

def getAllBookstore():
    url = 'https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M' 
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    res = response.json()
    return res

def getCountyOption(items):
        optionlist = []
        for item in items:
            name = item['cityName'][0:3]
            if name  not in optionlist:
                optionlist.append(name)
        return optionlist


def getSpecificBookstore(items, county):
    specificBookstoreList = []
    for item in items:
        name = item['cityName']
        if county in name:
                specificBookstoreList.append(item)
    return specificBookstoreList













def app():
    bookstorelist= getAllBookstore()
    countyOption = getCountyOption(bookstorelist)
    st.header('特色書店地圖')
    st.metric('Total bookstore', len(bookstorelist))
    county = st.selectbox('請選擇縣市', getCountyOption(bookstorelist))
    #district = st.multiselect('請選擇區域', ['a', 'b', 'c', 'd'])
    specificBookstore = getSpecificBookstore(bookstorelist,county)
    num = len(specificBookstore)
    st.write(f'總共有{num}項結果')
	 
	
if __name__ == '__main__':
    app()

    
        
