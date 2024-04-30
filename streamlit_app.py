import streamlit as st
from datetime import date

import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
from PIL import Image

def creds_entered():
    if st.session_state["user"].strip() == "stock@18" and st.session_state["passwd"].strip() == "123":
     st.session_state ["authenticated"]= True
    else:
      st.session_state["authenticated"]= False
      if not st.session_state["passwd"]:
         st.warning("Please enter password.")
      elif not st.session_state["user"]:
         st.warning("Please enter username.")
      else:
        st.error ("Please enter valid Username/Password")

def authenticate_user():
   if "authenticated" not in st.session_state: 
    image = Image.open('stock.png')
    st.image(image)
    with open("stock.png") as file:
     st.header('WELCOME TO STOCKMART')
    ('Stock Price Prediction App')
    st.text_input(label="USERNAME:", value="", key="user", on_change=creds_entered)
    st.text_input(label="PASSWORD:", value="", key="passwd", type="password", on_change=creds_entered)
    st.button('Login')
    return False
   else:
     if st.session_state ["authenticated"]:
       return True
     else:
        image = Image.open('stock.png')
        st.image(image)
        with open("stock.png") as file:
         st.header('WELCOME TO STOCKMART')
        ('Stock Price Prediction App')
        st.text_input(label="USERNAME:", value="", key="user", on_change=creds_entered)
        st.text_input(label="PASSWORD:", value="", key="passwd", type="password", on_change=creds_entered)
        st.button('Login')
        return False
     
if authenticate_user():
  st.title('Stock Price Prediction App')
  image = Image.open('stock.png')
  st.sidebar.title('STOCKMART')
  st.sidebar.image(image)
  with open("stock.png") as file:

   START = "2010-01-01"
  TODAY = date.today().strftime("%Y-%m-%d")
     
  stocks = ('EURUSD=X', 'AAPL', 'MSFT', 'TSLA', 'AMZN','GOOG','NVDA','META','WMT','JNJ','NFLX','AMD','KO','IBM','INTC','F','NOK')
  selected_stock = st.sidebar.selectbox('Select dataset for prediction', stocks)
  n_years = st.sidebar.slider('Years of prediction:', 1, 4)
  period = n_years * 365


  @st.cache_data
  def download_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

	
  data_load_state = st.text('Loading data...')
  data = download_data(selected_stock)
  data_load_state.text('Loading data... done!')

  st.subheader('Raw data')
  st.write(data.tail(30))

 # Plot raw data
  def plot_raw_data():
   fig = go.Figure()
   fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
   fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
   fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
   st.plotly_chart(fig)
	
  plot_raw_data()

  # Predict forecast with Prophet.
  df_train = data[['Date','Close']]
  df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

  m = Prophet()
  m.fit(df_train)
  future = m.make_future_dataframe(periods=period)
  forecast = m.predict(future)

  # Show and plot forecast
  st.subheader('Predicted data')
  st.write(forecast.tail(30))
    
  st.write(f'Predicted plot for {n_years} years')
  fig1 = plot_plotly(m, forecast)
  st.plotly_chart(fig1)

  st.write("Predicted components")
  fig2 = m.plot_components(forecast)
  st.write(fig2)


  import streamlit as st  # pip install streamlit

  st.sidebar.header(":mailbox: Get In Touch With Us!")
  contact_form = """
  <form action="https://formsubmit.co/nadishsmart77@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value=<"false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
  </form>
  """

  st.sidebar.markdown(contact_form, unsafe_allow_html=True)

  # Use Local CSS File
  def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


  local_css("style/style.css.txt")

  st.header( "OUR TEAM MEMBERS")
  ("720820103072 [NADISH KS](https://www.linkedin.com/in/nadish-ks-10276b255)")
  ("720820103077 [NAVEEN S](https://www.instagram.com/_dio_kid_naveentrinks?igsh=MTZhOXJlN3p4cHNzeA==)")
  ("720820103076 [NAVEEN R](https://www.instagram.com/ft.crushxx_?igsh=eW90Yzhsbndkemhl)")
  ("720820103306 [KISHORE CHAKKARAVARTHY A](https://www.linkedin.com/in/kishore-chakkaravarthy-54a0812b2?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)")
