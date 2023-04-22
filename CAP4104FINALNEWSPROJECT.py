import pandas as pd
import streamlit as st
import requests
import json

# import pycountry
# from api import apiKEY
apiKey='0a54baab3c394337aa46d1ea286cfb24'

st.title('news app final CAP 4104 ')
col1, col2= st.columns(2)
with col1:
    country= st.selectbox('select country',options=["ae","ar","at","au","be","bg","br","ca","ch","cn","co","cu","cz","de",
                                                 "eg","fr","gb","gr","hk","hu","id","ie","il","in","it","jp","kr","lt",
                                                 "lv","ma","mx","my","ng","nl","no","nz","ph","pl","pt","ro","rs","ru",
                                                "sa","se","sg","si","sk","th","tr","tw","ua","us","ve","za"])
with col2:
    category= st.radio('news category chosen:',('technology', 'politics', 'sports','business'))
    btn= st.button('enter')
if country and category and btn:
    #asking user for country input, ex us for us news and turns it into alpha_2 through user method
    # country= pycountry.countries.get(name=user).alpha_2

    finalURL=f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey=0a54baab3c394337aa46d1ea286cfb24"
    r= requests.get(finalURL).json()
    print(r["articles"][0])
    articles= r['articles']
    for article in articles:
        st.header(article['title'])
        st.markdown(f"<span style='background-color:blue;padding:10px;border-radius:'> Published at: {article['publishedAt']}</span>", unsafe_allow_html=True)
        #st.write(article['publishedAt'])
        if article['author']:
            st.write(article['author'])
        st.write(article['source']['name'])
        st.write(article['description'])
        st.write(article['url'])
#multiselect
countryoptions= st.multiselect('select by region',['americas', 'europe', 'asia', 'africa'],['americas'])
st.write(countryoptions)
#map element
#a map of news by region
df = pd.read_csv('news-articles.csv',
                 newscolumns=['title', 'article', 'publishdate'])

df.columns = ['Source', 'Topic', 'Content']
st.map(df)
#bar chart
regions={"news regions": ["americas","europe","asia" ],"news articles by region":[2000,1000,4000]}

regions= pd.DataFrame(regions)

regions=regions.set_index("region name")

st.bar_chart(regions)

#line chart
newsinfo=pd.read_csv('news-articles.csv')
st.write(newsinfo.head())
newsinfo=newsinfo.iloc[:,1:]
st.write(newsinfo.head())
st.line_chart(newsinfo)

#button widget
st.title("button")
result= st.button("click me")
st.write(result)
if result:
    st.write(":success:")
st.title("welcome")
st.write("to this page")
    #dataframe
df= pd.DataFrame({'first':[1,2], 'second':[6,7]})
st.sidebar.write(df)
df
st.sidebar.line_chart(df)
    #checkbox widget
if st.checkbox("show table..."):
    df


    #selectbox
    opt = st.selectbox('which select')
    if opt== 'None':
        st.write("select val")
    else:
        st.write('selected', opt)

#slider
st.title("sliders")
st.subheader("news notification preferneces")
y = st.slider('select news inbox notification prefernece level from a scale of 0-10', value=50)
st.write("slider number: " , y )
#select-slider
news_options= ['politics' ,'popular media']
news= st.select_slider ("choose category")
options= news_options
st.write ("selected:" , news)

#radio button
newsr_radio= ['HomePage' ,'FeaturedNews']
newsr= st.radio('Selected Stories', newsr_radio, index=1)
st.write("the 'news' returns" , newsr)
if newsr['HomePage']:
#if newsr='HomePage':
    st.subheader("welcome")
    st.write("hi")
else:
    st.subheader("hello")
    st.write("hi")


#success message
st.success('success')

#info box
st.info('this allows you to search for news stories based off regional and language preferences')

#error
st.error('please select your region of choice using the drop down menu')

#states page

# select box for states, checkbox for topics and displays area chart and bar chart of most reported topics with in state

#selectbox
textdisplay= 'select states'
listdisplayed= ['alabama', 'arizona', 'florida', 'california', 'arkansas']
results= st.selectbox('select a state', listdisplayed)
st.write(f'state selected: {results}' )

#checkbox for topics
if st.checkbox("list of topics..."):
    df

#bar chart most reported topics by state
f = open('states.json')

data = json.load(f)

states = []
for data in data:
    states += [data["state"]]


data= {states}
data= pd.DataFrame(data)
st.bar_chart(data)
#compare page: map and table to compare different state and country

st.title('map to compare state/country')
categories= ('STATE', 'COUNTRY')
dropdown= st.multiselect('pick state or country', categories)

#table
sel_col, disp_col= st.beta_columns(2)

disp_col.subheader('states to compare')

dipl_col.subheader('countries to compare')
