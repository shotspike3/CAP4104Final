import streamlit as st
import pandas as pd
import requests

st.markdown(
    """
    <style>
        [data-testid="stSidebarNav"]::before {
            content: "News API";
            margin-left: 20px;
            margin-top: 20px;
            font-size: 30px;
            position: relative;
            top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
country = "us"

category = st.selectbox('news category chosen:', ('technology', 'politics', 'sports', 'business'))

finalURL = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey=0a54baab3c394337aa46d1ea286cfb24"
r = requests.get(finalURL).json()


# multiselect
countryoptions = st.multiselect('select by region', ['americas', 'europe', 'asia', 'africa'], ['americas'])
st.write(countryoptions)
# map element
# a map of news by region
df = pd.read_csv('../news-articles.csv',
                 newscolumn=['title', 'article', 'publishdate'])

df.columns = ['Source', 'Topic', 'Content']
st.map(df)
# bar chart
regions = {"news regions": ["americas", "europe", "asia"], "news articles by region": [2000, 1000, 4000]}

regions = pd.DataFrame(regions)

regions = regions.set_index("region name")

st.bar_chart(regions)

# line chart
newsinfo = pd.read_csv('../news-articles.csv')
st.write(newsinfo.head())
newsinfo = newsinfo.iloc[:, 1:]
st.write(newsinfo.head())
st.line_chart(newsinfo)

# button widget
st.title("button")
result = st.button("click me")
st.write(result)
if result:
    st.write(":success:")
st.title("welcome")
st.write("to this page")
# dataframe
df = pd.DataFrame({'first': [1, 2], 'second': [6, 7]})
st.sidebar.write(df)
df
st.sidebar.line_chart(df)
# checkbox widget
if st.checkbox("show table..."):
    df

    # selectbox
    opt = st.selectbox('which select')
    if opt == 'None':
        st.write("select val")
    else:
        st.write('selected', opt)

# slider
st.title("sliders")
st.subheader("news notification preferneces")
y = st.slider('select news inbox notification prefernece level from a scale of 0-10', value=50)
st.write("slider number: ", y)
# select-slider
news_options = ['politics', 'popular media']
news = st.select_slider("choose category")
options = news_options
st.write("selected:", news)

# radio button
newsr_radio = ['HomePage', 'FeaturedNews']
newsr = st.radio('Selected Stories', newsr_radio, index=1)
st.write("the 'news' returns", newsr)
if newsr['HomePage']:
    # if newsr='HomePage':
    st.subheader("welcome")
    st.write("hi")
else:
    st.subheader("hello")
    st.write("hi")

# success message
st.success('success')

# info box
st.info('this allows you to search for news stories based off regional and language preferences')

# error
st.error('please select your region of choice using the drop down menu')
