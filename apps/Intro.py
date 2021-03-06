# -*- coding: utf-8 -*-
"""
Created on Wed May 25 14:20:18 2022

@author: Priya
"""
import streamlit as st
import base64
import streamlit.components.v1 as components
from PIL import Image
def app():
    
    st.sidebar.markdown("<br>",unsafe_allow_html=True)
    
    image = Image.open('files/wuhan.JPG')
    st.sidebar.image(image,width=250)
    st.sidebar.markdown("<br>",unsafe_allow_html=True)
    image = Image.open('files/Capture2.JPG')
    st.sidebar.image(image,width=250)
    st.sidebar.markdown("<br>",unsafe_allow_html=True)
    file_ = open("files/giphy.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    st.markdown("<marquee style='width:100%; direction:left;height:100%;color: black; font-weight: bold;behavior:scroll;'>WELCOME TO THE COVID-19 DISEASE ASSISTANT WEBSITE !!!</marquee>",unsafe_allow_html=True)
    
    temp = """

                  
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
</head>
<body>

<div class="container">
  
  <div id="myCarousel" class="carousel slide" data-ride="carousel">
    <!-- Indicators -->
   

    <!-- Wrapper for slides -->
    <div class="carousel-inner">

      <div class="item active">
        <img src="https://storage.googleapis.com/proudcity/holyokema/uploads/2020/04/1582659092Addaheading.png"  style="display: block; margin-left: auto; margin-right: auto; width: 50%;">
        
      </div>
       <div class="item">
          <img src="https://static.india.com/wp-content/uploads/2020/12/Coronavirus-vaccine-dry-run.png?impolicy=Medium_Resize&w=1200&h=800" style="display: block; margin-left: auto; margin-right: auto; width: 50%;">
        
      </div>
      
       
     
    
      <div class="item">
        <img src="https://media1.thehungryjpeg.com/thumbs2/800_3741120_cfsrka1k1ub99arb3s9afbtrdkxpnvoz6yzx2hpi_watercolor-quarantine-virus-self-isolation-epidemic-covid-clipart-png.jpg" style="display: block; margin-left: auto; margin-right: auto; width: 50%;">
        
      </div>
       <div class="item">
          <img src="https://img.freepik.com/free-vector/get-your-vaccine-font-with-many-kids-waiting-queue-get-covid-19-vaccine_1308-59879.jpg?w=2000" style="display: block; margin-left: auto; margin-right: auto; width: 50%;">
        
      </div>
      
  <div class="item">
          <img src="https://cdn3.vectorstock.com/i/1000x1000/70/97/coronavirus-poster-design-with-sick-children-vector-30427097.jpg" style="display: block; margin-left: auto; margin-right: auto; width: 50%;">
        
      </div>
        <div class="item">
          <img src="https://asset-a.grid.id/crop/0x0:0x0/700x465/photo/2020/07/06/3498610560.png" style="display: block; margin-left: auto; margin-right: auto; width: 50%;">
        
      </div>
        
      
    </div>

   
  </div>
</div>

			"""
    components.html(temp,height=350)
        
    st.sidebar.markdown(f'<img src="data:image/gif;base64,{data_url}"  width=250 height=250>',unsafe_allow_html=True,
            )
    st.markdown("<h5 style='text-align: center; color:green; font-weight: bold;font-style: italic;font-size: xx-large;'>???A \U0001F637 can save your life!!???</h5>", unsafe_allow_html=True) 
    
    col1, col2= st.columns(2)

    with col1:
        
        image = Image.open('files/save.JPG')

        st.image(image,use_column_width=True)
        
    with col2:
        st.markdown("<h3 style='text-align: center; color: purple;font-size: xx-large;'>About COVID-19 Virus</h3>", unsafe_allow_html=True) 
        st.markdown("<h5 style='font-size:150%;font-family:'Times New Roman';'>Coronavirus disease 2019 (COVID-19) is a contagious disease caused by a virus, the severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). The first known case was identified in Wuhan, China, in December 2019.The disease spread worldwide, leading to the COVID-19 pandemic.</h5>", unsafe_allow_html=True) 
        #st.markdown("<br>",unsafe_allow_html=True)   
        st.markdown("<h5 style='font-size:150%;font-family:'Times New Roman';'>Symptoms of COVID???19 are variable, but often include fever,cough, headache,fatigue, breathing difficulties, loss of smell, and loss of taste. Symptoms may begin one to fourteen days after exposure to the virus. At least a third of people who are infected do not develop noticeable symptoms.Of those people who develop symptoms noticeable enough to be classed as patients, most (81%) develop mild to moderate symptoms (up to mild pneumonia), while 14% develop severe symptoms (dyspnea, hypoxia, or more than 50% lung involvement on imaging), and 5% develop critical symptoms (respiratory failure, shock, or multiorgan dysfunction).Older people are at a higher risk of developing severe symptoms. Some people continue to experience a range of effects (long COVID) for months after recovery, and damage to organs has been observed. Multi-year studies are underway to further investigate the long-term effects of the disease.</h5>", unsafe_allow_html=True) 
    
    
    st.markdown("<br>", unsafe_allow_html=True)    
    st.markdown("<h5 style='text-align: center; color: black;font-weight: bold;font-style: italic;'>Keep safe, keep well And most of all Keep the Faith. We will get through this together</h5>", unsafe_allow_html=True)
    
    footer_temp = """

	 <!-- CSS  -->
	  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
	  <link href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css" type="text/css" rel="stylesheet" media="screen,projection"/>
	  <link href="static/css/style.css" type="text/css" rel="stylesheet" media="screen,projection"/>
	   <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">


	 <footer class="page-footer grey darken-4">
	    <div class="container" id="aboutapp">
	      <div class="row">
	        <div class="col l6 s12">
	          <h5 class="white-text">CONTACT US</h5>
	          <p class="grey-text text-lighten-4">Address : Twinkle Building, 361 Strawberry Road, Mumabi-22</p>
               <p class="grey-text text-lighten-4">Mobile : (+91) 9988112290</p>
                <p class="grey-text text-lighten-4">Mail To : adamincda@gmail.com</p>


	        </div>
	      
	   <div class="col l3 s12">
	          <h5 class="white-text">Connect With Me</h5>
	          <ul>
	           
	           <a href="https://github.com/NADARPRIYAEBANEZAR" target="_blank" class="white-text">
	            <i class="fab fa-github-square fa-4x"></i>
	          </a>
	          </ul>
	        </div>
	      </div>
	    </div>
	    
	  </footer>

	"""
    components.html(footer_temp,height=300)
    
    
        

       
    
        
