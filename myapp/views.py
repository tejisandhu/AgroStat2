from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
from django.core.mail import send_mail
from django.utils.safestring import mark_safe
import random
from myapp.models import Agriculture_Universities
from myapp.models import Agriculture_News
from myapp.models import Agriculture_Videos
from myapp.models import Agriculture_Crop
from myapp.models import Agriculture_Call_centre
from myapp.models import Agriculture_Farmer_Scheme
from myapp.models import Latest_Technology
from myapp.models import Indian_Agriculture_University
from myapp.models import myreview
from myapp.models import support
from myapp.models import contact
from myapp.models import register
from myapp.models import agri_crops_details
from myapp.models import disease_solution
from myapp.models import newsletter
from myapp.models import dealers
import numpy as np
import country_converter as cc
import warnings
import itertools
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
import pandas as pd
import statsmodels.api as sm
import matplotlib
import plotly.graph_objects as go
from .models import ChatMessage
from django.http import JsonResponse
import json
import plotly.express as px
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model




def f1(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("fertilizers.csv")
          country=request.POST.get("country")
          #filtering the dataset
          df1=df[df["Entity"]==country]
          
          
          fig = go.Figure()   
          fig.add_traces(go.Scatter(x=df1["Year"],y=df1["Nutrient nitrogen N (total) | 00003102 || Use per area of cropland | 005159 || kilograms per hectare"],mode="lines",name=country,
                                   line=dict(color="#001f3f",width=2),
                            fill='tozeroy',  
    
                                   
                                   ))
          
          
          fig.update_layout(xaxis_title="Year", yaxis_title="Nitrogen used kg/ha", title=f"Nutrient Nitrogen(N) Used Kilogram per Hectare of {country}", xaxis_type="category",plot_bgcolor= "white",
          height=600,
          width=1200,
          #paper_bgcolor="#f8b28b",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=True, showline=True,gridcolor="Lightgray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))  
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
          
     else:
          data=pd.read_csv("fertilizers.csv")
          word_to_exclude = '(FAO)'

# Filter rows that DON'T contain the word and assign the result back to the DataFrame
          data = data[~data['Entity'].str.contains(word_to_exclude)]
          column=data["Entity"].drop_duplicates().tolist()
          
          column=data["Entity"].drop_duplicates().tolist()
          return render(request,"md1.html",{"data":column})
def f2(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("fertilizers.csv")
          year=int(request.POST.get("year"))
          print(year)
          #filtering the dataset
          df1=df[df["Year"]==year]
          #print(df1)
          
          
          word_to_exclude = '(FAO)'

# Filter rows that DON'T contain the word and assign the result back to the DataFrame
          df1 = df1[~df1['Entity'].str.contains(word_to_exclude)]

          
          
          fig=px.bar(df1,y="Nutrient nitrogen N (total) | 00003102 || Use per area of cropland | 005159 || kilograms per hectare",x="Entity"
          #labels={"Nutrient nitrogen N (total) | 00003102 || Use per area of cropland | 005159 || kilograms per hectare":"Nitrogen kilograms per hectar"},
          )
          fig.update_layout(xaxis_title="Country", yaxis_title="Nitrogen used kg/ha", title=f"Nutrient Nitrogen(N) Used Kilogram per Hectare in {year}", xaxis_type="category",plot_bgcolor= "white",
          height=600,
          width=1200,
          paper_bgcolor="lightsteelblue",title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=False, showline=True, linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))
          fig.update_traces(
               hovertemplate="%{y} kg/ha<br>Country: %{x}",marker_color="black"
          )
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
          
     else:
          data=pd.read_csv("fertilizers.csv")
          word_to_exclude = '(FAO)'

# Filter rows that DON'T contain the word and assign the result back to the DataFrame
          data = data[~data['Entity'].str.contains(word_to_exclude)]
          column=data["Entity"].drop_duplicates().tolist()
          
          column=data["Year"].drop_duplicates().tolist()
          return render(request,"md2.html",{"data":column})
def f3(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("fertilizers.csv")
          country=request.POST.get("country")
          print(country)
          startyear=int(request.POST.get("startyear"))
          print(startyear)
          endyear=int(request.POST.get("endyear"))
          print(endyear)
         
          #filtering the dataset
          df1=df[df['Entity'] == country]
          print(df1)
          
          df1=df1[(df1["Year"]>=startyear) & (df1["Year"]<=endyear)]
          
          print(df1)
          
          fig=px.scatter(df1,y="Nutrient nitrogen N (total) | 00003102 || Use per area of cropland | 005159 || kilograms per hectare",x="Year",size="Nutrient nitrogen N (total) | 00003102 || Use per area of cropland | 005159 || kilograms per hectare",size_max=40,color="Year"
          )
          fig.update_layout(xaxis_title="Year", yaxis_title="Nitrogen used kg/ha", title=f"Nutrient Nitrogen(N) Used Kilogram per Hectare from {startyear} to {endyear}", xaxis_type="category",plot_bgcolor= "lightsteelblue",
          height=600,
          width=1200,
          #paper_bgcolor="#f8b28b",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=True, showline=True,gridcolor="Lightgray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))
         
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
          
     else:
          data=pd.read_csv("fertilizers.csv")
          word_to_exclude = '(FAO)'

# Filter rows that DON'T contain the word and assign the result back to the DataFrame
          data = data[~data['Entity'].str.contains(word_to_exclude)]
          column=data["Entity"].drop_duplicates().tolist()
          
          
          column=data["Entity"].drop_duplicates().tolist()
          column1=data["Year"].drop_duplicates().tolist()
          return render(request,"md3.html",{"data":column,"year":column1})
def f4(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("fertilizers.csv")
          
          
          
          country1=request.POST.get("country1")
          country2=request.POST.get("country2")
          df1=df[df['Entity']==country1]
          df2=df[df['Entity']==country2]
         
          
          fig = go.Figure()

          # Create bar traces for each country
          fig.add_trace(go.Bar(
          x=df1["Year"],  # X-axis data (categories)
          y=df1["Nutrient nitrogen N (total) | 00003102 || Use per area of cropland | 005159 || kilograms per hectare"],  # Y-axis data (values)
          name=country1,
          marker=dict(color="#001f3f"),  # Bar color
          ))

          fig.add_trace(go.Bar(
          x=df2["Year"],
          y=df2["Nutrient nitrogen N (total) | 00003102 || Use per area of cropland | 005159 || kilograms per hectare"],
          name=country2,
          marker=dict(color="#0041a4"),
          ))

          # Update layout for a bar chart
          fig.update_layout(
          barmode='group',
          xaxis_title="Year",
          yaxis_title="Nitrogen used kg/ha",
          title=f"Nutrient Nitrogen(N) Used Kilogram per Hectare of {country1} and {country2}",
          plot_bgcolor="lightsteelblue",
          height=600,
          width=1200,
          title_font_size=25,
          font=dict(family="Verdana", size=18, color="black"),
          title_x=0.5,
          xaxis_title_font_size=25,
          yaxis_title_font_size=25,
          xaxis=dict(showgrid=True, showline=True, gridcolor="Lightgray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"),
          xaxis_type="category",  # Set x-axis for categorical data (Year)
          )
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
     
     else:
          data=pd.read_csv("fertilizers.csv")
          
          word_to_exclude = '(FAO)'

# Filter rows that DON'T contain the word and assign the result back to the DataFrame
          data = data[~data['Entity'].str.contains(word_to_exclude)]
          
          column=data["Entity"].drop_duplicates().tolist()
          

          
          return render(request,"md4.html",{"data":column})
def f5(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("fertilizers.csv")
          country1=request.POST.get("country1")
          country2=request.POST.get("country2")
          country3=request.POST.get("country3")
          df1=df[df['Entity']==country1]
          df2=df[df['Entity']==country2]
          df3=df[df['Entity']==country3]
          
          fig = go.Figure()
          fig.add_traces(go.Scatter(x=df1["Year"],y=df1["Nutrient nitrogen N (total) | 00003102 || Use per area of cropland | 005159 || kilograms per hectare"],mode="lines",name=country1,
                                   line=dict(color="#001f3f",width=3),
                                   ))
          fig.add_traces(go.Scatter(x=df2["Year"],y=df2["Nutrient nitrogen N (total) | 00003102 || Use per area of cropland | 005159 || kilograms per hectare"],mode="lines+markers",name=country2,
                                   line=dict(color="#0041a4",width=3),marker=dict(symbol="square")
                                   ))
          fig.add_traces(go.Scatter(x=df3["Year"],y=df3["Nutrient nitrogen N (total) | 00003102 || Use per area of cropland | 005159 || kilograms per hectare"],mode="lines+markers",name=country3,
                                   line=dict(color="#f8b28b",width=3),marker=dict(symbol="circle")
                                   ))
          fig.update_layout(xaxis_title="Year", yaxis_title="Nitrogen used kg/ha", title=f"Nutrient Nitrogen(N) Used Kilogram per Hectare of {country1}, {country2} and {country3}", xaxis_type="category",plot_bgcolor= "lightsteelblue",
          height=600,
          width=1200,
          #paper_bgcolor="#f8b28b",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=True, showline=True,gridcolor="Lightgray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))    
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
     
     else:
          data=pd.read_csv("fertilizers.csv")
          word_to_exclude = '(FAO)'

# Filter rows that DON'T contain the word and assign the result back to the DataFrame
          data = data[~data['Entity'].str.contains(word_to_exclude)]
          column=data["Entity"].drop_duplicates().tolist()
          
          return render(request,"md5.html",{"data":column})
def f6(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("fertilizers.csv")
          country1=request.POST.get("country1")
          country2=request.POST.get("country2")
          country3=request.POST.get("country3")
          startyear=int(request.POST.get("startyear"))
          endyear=int(request.POST.get("endyear"))
          df1=df[df['Entity']==country1]
          df1=df1[(df1["Year"]>=startyear) & (df1["Year"]<=endyear)]
          df2=df[df['Entity']==country2]
          df2=df2[(df2["Year"]>=startyear) & (df2["Year"]<=endyear)]
          df3=df[df['Entity']==country3]
          df3=df3[(df3["Year"]>=startyear) & (df3["Year"]<=endyear)]
         
          
          fig = go.Figure()
          fig.add_traces(go.Bar(x=df1["Year"],y=df1["Nutrient nitrogen N (total) | 00003102 || Use per area of cropland | 005159 || kilograms per hectare"],
          name=country1,
          marker=dict(color="#001f3f")
                                   ))
          fig.add_traces(go.Bar(x=df2["Year"],y=df2["Nutrient nitrogen N (total) | 00003102 || Use per area of cropland | 005159 || kilograms per hectare"],name=country2,
          marker=dict(color="#0041a4")
                                    
                                   ))
          fig.add_traces(go.Bar(x=df3["Year"],y=df3["Nutrient nitrogen N (total) | 00003102 || Use per area of cropland | 005159 || kilograms per hectare"],name=country3,
          marker=dict(color="#698b90")
                                    
                                   ))
          fig.update_layout(xaxis_title="Year", yaxis_title="Nitrogen used kg/ha", title=f"Nutrient Nitrogen(N) Used Kilogram per Hectare of {country1}, {country2} and {country3}", xaxis_type="category",plot_bgcolor= "lightsteelblue",
          height=600,
          width=1200,
          #paper_bgcolor="#f8b28b",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=True, showline=True,gridcolor="Lightgray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))    
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
     
     else:
          data=pd.read_csv("fertilizers.csv")
          word_to_exclude = '(FAO)'
          data = data[~data['Entity'].str.contains(word_to_exclude)]
          column=data["Entity"].drop_duplicates().tolist()
          
          column1=data["Year"].drop_duplicates().tolist()
          return render(request,"md6.html",{"data":column,"year":column1})
def f7(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("fertilizers.csv")
          year=int(request.POST.get("year"))
          df1=df[df['Year']==year]
          df1=df1.dropna()
          df1=df1.sort_values(by="Nutrient nitrogen N (total) | 00003102 || Use per area of cropland | 005159 || kilograms per hectare",ascending=False)
          n=int(request.POST.get("n"))
          dfmax=df1.head(n)
          
          fig = go.Figure()
          fig.add_trace(go.Pie(labels=dfmax["Entity"],values=dfmax["Nutrient nitrogen N (total) | 00003102 || Use per area of cropland | 005159 || kilograms per hectare"], textinfo='percent',hole=.3
                               
                                   ))
          fig.update_layout(
                   title=f"Nutrient Nitrogen(N) Used Kilogram per Hectare by top {n} countries in {year}", plot_bgcolor= "lightsteelblue",
          height=600,
          width=1200,
          paper_bgcolor="lightsteelblue",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,)    
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
     
     else:
          data=pd.read_csv("fertilizers.csv")
          column=data["Entity"].drop_duplicates().tolist()
          column1=data["Year"].drop_duplicates().tolist()
          return render(request,"md7.html",{"data":column,"year":column1})
def f8(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     a=mark_safe('<iframe src="https://ourworldindata.org/explorers/fertilizers?time=2021&facet=none&Input=Synthetic+fertilizer&Nutrient=Nitrogen&Metric=Applied+%28per+hectare%29&Share+of+world+total=false&hideControls=true&tab=map" loading="lazy" style="width: 110%; height: 630px; border: 0px none; margin-left: -140px;overflow: hidden;"></iframe>')
          
     return render(request,"fertilizer_result_worldmap.html",{'map':a})



def fertilizer_link(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     user=register.objects.get(email=request.session['email'])     
     return render(request,'fertilizers_link.html',{'user':user})

def phosphorous1(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("phosphate-application-per-hectare-of-cropland.csv")
          country=request.POST.get("country")
          #filtering the dataset
          df1=df[df["Entity"]==country]
          
          
          fig = go.Figure()   
          fig.add_traces(go.Scatter(x=df1["Year"],y=df1["Nutrient phosphate P2O5 (total) | 00003103 || Use per area of cropland | 005159 || Kilograms per hectare"],mode="lines",name=country,
                                   line=dict(color="#001f3f",width=2),
                            fill='tozeroy',  
    
                                   
                                   ))
          
          
          fig.update_layout(xaxis_title="Year", yaxis_title="Phosphate used kg/ha", title=f"Phosphate fertilizer use per hectare of cropland by {country}", xaxis_type="category",plot_bgcolor= "white",
          height=600,
          width=1200,
          #paper_bgcolor="#f8b28b",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=True, showline=True,gridcolor="Lightgray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))  
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
          
     else:
          data=pd.read_csv("phosphate-application-per-hectare-of-cropland.csv")
          word_to_exclude = '(FAO)'

# Filter rows that DON'T contain the word and assign the result back to the DataFrame
          data = data[~data['Entity'].str.contains(word_to_exclude)]
          column=data["Entity"].drop_duplicates().tolist()
          
          return render(request,"phosphorous1.html",{"data":column})
def phosphorous2(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("phosphate-application-per-hectare-of-cropland.csv")
          year=int(request.POST.get("year"))
          print(year)
          #filtering the dataset
          df1=df[df["Year"]==year]
          #print(df1)
          
          
          word_to_exclude = '(FAO)'

# Filter rows that DON'T contain the word and assign the result back to the DataFrame
          df1 = df1[~df1['Entity'].str.contains(word_to_exclude)]

          
          
          fig=px.bar(df1,y="Nutrient phosphate P2O5 (total) | 00003103 || Use per area of cropland | 005159 || Kilograms per hectare",x="Entity"
          #labels={"Nutrient nitrogen N (total) | 00003102 || Use per area of cropland | 005159 || kilograms per hectare":"Nitrogen kilograms per hectar"},
          )
          fig.update_layout(xaxis_title="Country", yaxis_title="Phosphate used kg/ha", title=f"Phosphate fertilizer use per hectare of cropland, {year}", xaxis_type="category",plot_bgcolor= "white",
          height=600,
          width=1200,
          paper_bgcolor="lightsteelblue",title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=False, showline=True, linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))
          fig.update_traces(
               hovertemplate="%{y} kg/ha<br>Country: %{x}",marker_color="black"
          )
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
          
     else:
          data=pd.read_csv("phosphate-application-per-hectare-of-cropland.csv")
          word_to_exclude = '(FAO)'

# Filter rows that DON'T contain the word and assign the result back to the DataFrame
          data = data[~data['Entity'].str.contains(word_to_exclude)]
          column=data["Entity"].drop_duplicates().tolist()
          
          column=data["Year"].drop_duplicates().tolist()
          return render(request,"phosphorous2.html",{"data":column})
def phosphorous3(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("phosphate-application-per-hectare-of-cropland.csv")
          country=request.POST.get("country")
          print(country)
          startyear=int(request.POST.get("startyear"))
          print(startyear)
          endyear=int(request.POST.get("endyear"))
          print(endyear)
         
          #filtering the dataset
          df1=df[df['Entity'] == country]
          print(df1)
          
          df1=df1[(df1["Year"]>=startyear) & (df1["Year"]<=endyear)]
          
          print(df1)
          
          fig=px.scatter(df1,y="Nutrient phosphate P2O5 (total) | 00003103 || Use per area of cropland | 005159 || Kilograms per hectare",x="Year",size="Nutrient phosphate P2O5 (total) | 00003103 || Use per area of cropland | 005159 || Kilograms per hectare",size_max=40,color="Year"
          )
          fig.update_layout(xaxis_title="Year", yaxis_title="Phosphate used kg/ha", title=f"Phosphate fertilizer use per hectare of cropland from {startyear} to {endyear}", xaxis_type="category",plot_bgcolor= "lightsteelblue",
          height=600,
          width=1200,
          #paper_bgcolor="#f8b28b",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=True, showline=True,gridcolor="Lightgray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))
         
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
          
     else:
          data=pd.read_csv("phosphate-application-per-hectare-of-cropland.csv")
          word_to_exclude = '(FAO)'

# Filter rows that DON'T contain the word and assign the result back to the DataFrame
          data = data[~data['Entity'].str.contains(word_to_exclude)]
          column=data["Entity"].drop_duplicates().tolist()
          
          
          column=data["Entity"].drop_duplicates().tolist()
          column1=data["Year"].drop_duplicates().tolist()
          return render(request,"phosphorous3.html",{"data":column,"year":column1})
def phosphorous4(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("phosphate-application-per-hectare-of-cropland.csv")
          
          
          
          country1=request.POST.get("country1")
          country2=request.POST.get("country2")
          df1=df[df['Entity']==country1]
          df2=df[df['Entity']==country2]
         
          
          fig = go.Figure()

          # Create bar traces for each country
          fig.add_trace(go.Bar(
          x=df1["Year"],  # X-axis data (categories)
          y=df1["Nutrient phosphate P2O5 (total) | 00003103 || Use per area of cropland | 005159 || Kilograms per hectare"],  # Y-axis data (values)
          name=country1,
          marker=dict(color="#001f3f"),  # Bar color
          ))

          fig.add_trace(go.Bar(
          x=df2["Year"],
          y=df2["Nutrient phosphate P2O5 (total) | 00003103 || Use per area of cropland | 005159 || Kilograms per hectare"],
          name=country2,
          marker=dict(color="#0041a4"),
          ))

          # Update layout for a bar chart
          fig.update_layout(
          barmode='group',
          xaxis_title="Year",
          yaxis_title="Phosphate used kg/ha",
          title=f"Phosphate fertilizer use per hectare of cropland by {country1} and {country2}",
          plot_bgcolor="lightsteelblue",
          height=600,
          width=1200,
          title_font_size=25,
          font=dict(family="Verdana", size=18, color="black"),
          title_x=0.5,
          xaxis_title_font_size=25,
          yaxis_title_font_size=25,
          xaxis=dict(showgrid=True, showline=True, gridcolor="Lightgray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"),
          xaxis_type="category",  # Set x-axis for categorical data (Year)
          )
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
     
     else:
          data=pd.read_csv("phosphate-application-per-hectare-of-cropland.csv")
          
          word_to_exclude = '(FAO)'

# Filter rows that DON'T contain the word and assign the result back to the DataFrame
          data = data[~data['Entity'].str.contains(word_to_exclude)]
          
          column=data["Entity"].drop_duplicates().tolist()
          

          
          return render(request,"phosphorous4.html",{"data":column})
def phosphorous5(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("phosphate-application-per-hectare-of-cropland.csv")
          country1=request.POST.get("country1")
          country2=request.POST.get("country2")
          country3=request.POST.get("country3")
          df1=df[df['Entity']==country1]
          df2=df[df['Entity']==country2]
          df3=df[df['Entity']==country3]
          
          fig = go.Figure()
          fig.add_traces(go.Scatter(x=df1["Year"],y=df1["Nutrient phosphate P2O5 (total) | 00003103 || Use per area of cropland | 005159 || Kilograms per hectare"],mode="lines",name=country1,
                                   line=dict(color="#001f3f",width=3),
                                   ))
          fig.add_traces(go.Scatter(x=df2["Year"],y=df2["Nutrient phosphate P2O5 (total) | 00003103 || Use per area of cropland | 005159 || Kilograms per hectare"],mode="lines+markers",name=country2,
                                   line=dict(color="#0041a4",width=3),marker=dict(symbol="square")
                                   ))
          fig.add_traces(go.Scatter(x=df3["Year"],y=df3["Nutrient phosphate P2O5 (total) | 00003103 || Use per area of cropland | 005159 || Kilograms per hectare"],mode="lines+markers",name=country3,
                                   line=dict(color="#f8b28b",width=3),marker=dict(symbol="circle")
                                   ))
          fig.update_layout(xaxis_title="Year", yaxis_title="Phosphate used kg/ha", title=f"Phosphate fertilizer use per hectare of cropland by {country1}, {country2} and {country3}", xaxis_type="category",plot_bgcolor= "lightsteelblue",
          height=600,
          width=1200,
          #paper_bgcolor="#f8b28b",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=True, showline=True,gridcolor="Lightgray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))    
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
     
     else:
          data=pd.read_csv("phosphate-application-per-hectare-of-cropland.csv")
          word_to_exclude = '(FAO)'

# Filter rows that DON'T contain the word and assign the result back to the DataFrame
          data = data[~data['Entity'].str.contains(word_to_exclude)]
          column=data["Entity"].drop_duplicates().tolist()
          
          return render(request,"phosphorous5.html",{"data":column})
def phosphorous6(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("phosphate-application-per-hectare-of-cropland.csv")
          country1=request.POST.get("country1")
          country2=request.POST.get("country2")
          country3=request.POST.get("country3")
          startyear=int(request.POST.get("startyear"))
          endyear=int(request.POST.get("endyear"))
          df1=df[df['Entity']==country1]
          df1=df1[(df1["Year"]>=startyear) & (df1["Year"]<=endyear)]
          df2=df[df['Entity']==country2]
          df2=df2[(df2["Year"]>=startyear) & (df2["Year"]<=endyear)]
          df3=df[df['Entity']==country3]
          df3=df3[(df3["Year"]>=startyear) & (df3["Year"]<=endyear)]
         
          
          fig = go.Figure()
          fig.add_traces(go.Bar(x=df1["Year"],y=df1["Nutrient phosphate P2O5 (total) | 00003103 || Use per area of cropland | 005159 || Kilograms per hectare"],
          name=country1,
          marker=dict(color="#001f3f")
                                   ))
          fig.add_traces(go.Bar(x=df2["Year"],y=df2["Nutrient phosphate P2O5 (total) | 00003103 || Use per area of cropland | 005159 || Kilograms per hectare"],name=country2,
          marker=dict(color="#0041a4")
                                    
                                   ))
          fig.add_traces(go.Bar(x=df3["Year"],y=df3["Nutrient phosphate P2O5 (total) | 00003103 || Use per area of cropland | 005159 || Kilograms per hectare"],name=country3,
          marker=dict(color="#698b90")
                                    
                                   ))
          fig.update_layout(xaxis_title="Year", yaxis_title="Phosphate used kg/ha", title=f"Phosphate fertilizer use per hectare of cropland by {country1}, {country2} and {country3}", xaxis_type="category",plot_bgcolor= "lightsteelblue",
          height=600,
          width=1200,
          #paper_bgcolor="#f8b28b",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=True, showline=True,gridcolor="Lightgray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))    
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
     
     else:
          data=pd.read_csv("phosphate-application-per-hectare-of-cropland.csv")
          word_to_exclude = '(FAO)'
          data = data[~data['Entity'].str.contains(word_to_exclude)]
          column=data["Entity"].drop_duplicates().tolist()
          
          column1=data["Year"].drop_duplicates().tolist()
          return render(request,"phosphorous6.html",{"data":column,"year":column1})
def phosphorous7(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("phosphate-application-per-hectare-of-cropland.csv")
          year=int(request.POST.get("year"))
          df1=df[df['Year']==year]
          df1=df1.dropna()
          df1=df1.sort_values(by="Nutrient phosphate P2O5 (total) | 00003103 || Use per area of cropland | 005159 || Kilograms per hectare",ascending=False)
          n=int(request.POST.get("n"))
          dfmax=df1.head(n)
          
          fig = go.Figure()
          fig.add_trace(go.Pie(labels=dfmax["Entity"],values=dfmax["Nutrient phosphate P2O5 (total) | 00003103 || Use per area of cropland | 005159 || Kilograms per hectare"], textinfo='percent',hole=.3
                               
                                   ))
          fig.update_layout(
                   title=f"Phosphate fertilizer use per hectare of cropland by top {n} countries in {year}", plot_bgcolor= "lightsteelblue",
          height=600,
          width=1200,
          paper_bgcolor="lightsteelblue",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,)    
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
     
     else:
          data=pd.read_csv("phosphate-application-per-hectare-of-cropland.csv")
          column=data["Entity"].drop_duplicates().tolist()
          column1=data["Year"].drop_duplicates().tolist()
          return render(request,"phosphorous7.html",{"data":column,"year":column1})
def phosphorous8(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     a=mark_safe('<iframe src="https://ourworldindata.org/explorers/fertilizers?time=2021&facet=none&pickerSort=asc&hideControls=true&Input=Synthetic+fertilizer&Nutrient=Phosphorous&Metric=Applied+%28per+hectare%29&Share+of+world+total=false&country=Eastern+Asia~OWID_WRL&tab=map" loading="lazy" style="width: 110%; height: 630px; border: 0px none; margin-left: -140px;overflow: hidden;"></iframe>')
     
     
          
     return render(request,"fertilizer_result_worldmap.html",{'map':a})


def phosphorous_link(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     user=register.objects.get(email=request.session['email'])     
     return render(request,'phosphorous_link.html',{'user':user})


def potassium1(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("potash-fertilizer-application-per-hectare-of-cropland.csv")
          country=request.POST.get("country")
          #filtering the dataset
          df1=df[df["Entity"]==country]
          
          
          fig = go.Figure()   
          fig.add_traces(go.Scatter(x=df1["Year"],y=df1["Nutrient potash K2O (total) | 00003104 || Use per area of cropland | 005159 || Kilograms per hectare"],mode="lines",name=country,
                                   line=dict(color="#001f3f",width=2),
                            fill='tozeroy',  
    
                                   
                                   ))
          
          
          fig.update_layout(xaxis_title="Year", yaxis_title="Potash used kg/ha", title=f"Potash fertilizer use per hectare of cropland by {country}", xaxis_type="category",plot_bgcolor= "white",
          height=600,
          width=1200,
          #paper_bgcolor="#f8b28b",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=True, showline=True,gridcolor="Lightgray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))  
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
          
     else:
          data=pd.read_csv("potash-fertilizer-application-per-hectare-of-cropland.csv")
          word_to_exclude = '(FAO)'

# Filter rows that DON'T contain the word and assign the result back to the DataFrame
          data = data[~data['Entity'].str.contains(word_to_exclude)]
          column=data["Entity"].drop_duplicates().tolist()
          
          return render(request,"potassium1.html",{"data":column})
def potassium2(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("potash-fertilizer-application-per-hectare-of-cropland.csv")
          year=int(request.POST.get("year"))
          print(year)
          #filtering the dataset
          df1=df[df["Year"]==year]
          #print(df1)
          
          
          word_to_exclude = '(FAO)'

# Filter rows that DON'T contain the word and assign the result back to the DataFrame
          df1 = df1[~df1['Entity'].str.contains(word_to_exclude)]

          
          
          fig=px.bar(df1,y="Nutrient potash K2O (total) | 00003104 || Use per area of cropland | 005159 || Kilograms per hectare",x="Entity"
          #labels={"Nutrient nitrogen N (total) | 00003102 || Use per area of cropland | 005159 || kilograms per hectare":"Nitrogen kilograms per hectar"},
          )
          fig.update_layout(xaxis_title="Country", yaxis_title="Potash used kg/ha", title=f"Potash fertilizer use per hectare of cropland, {year}", xaxis_type="category",plot_bgcolor= "white",
          height=600,
          width=1200,
          paper_bgcolor="lightsteelblue",title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=False, showline=True, linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))
          fig.update_traces(
               hovertemplate="%{y} kg/ha<br>Country: %{x}",marker_color="black"
          )
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
          
     else:
          data=pd.read_csv("potash-fertilizer-application-per-hectare-of-cropland.csv")
          word_to_exclude = '(FAO)'

# Filter rows that DON'T contain the word and assign the result back to the DataFrame
          data = data[~data['Entity'].str.contains(word_to_exclude)]
          column=data["Entity"].drop_duplicates().tolist()
          
          column=data["Year"].drop_duplicates().tolist()
          return render(request,"potassium2.html",{"data":column})
def potassium3(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("potash-fertilizer-application-per-hectare-of-cropland.csv")
          country=request.POST.get("country")
          print(country)
          startyear=int(request.POST.get("startyear"))
          print(startyear)
          endyear=int(request.POST.get("endyear"))
          print(endyear)
         
          #filtering the dataset
          df1=df[df['Entity'] == country]
          print(df1)
          
          df1=df1[(df1["Year"]>=startyear) & (df1["Year"]<=endyear)]
          
          print(df1)
          
          fig=px.scatter(df1,y="Nutrient potash K2O (total) | 00003104 || Use per area of cropland | 005159 || Kilograms per hectare",x="Year",size="Nutrient potash K2O (total) | 00003104 || Use per area of cropland | 005159 || Kilograms per hectare",size_max=40,color="Year"
          )
          fig.update_layout(xaxis_title="Year", yaxis_title="Potash used kg/ha", title=f"Potash fertilizer use per hectare of cropland from {startyear} to {endyear}", xaxis_type="category",plot_bgcolor= "lightsteelblue",
          height=600,
          width=1200,
          #paper_bgcolor="#f8b28b",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=True, showline=True,gridcolor="Lightgray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))
         
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
          
     else:
          data=pd.read_csv("potash-fertilizer-application-per-hectare-of-cropland.csv")
          word_to_exclude = '(FAO)'

# Filter rows that DON'T contain the word and assign the result back to the DataFrame
          data = data[~data['Entity'].str.contains(word_to_exclude)]
          column=data["Entity"].drop_duplicates().tolist()
          
          
          column=data["Entity"].drop_duplicates().tolist()
          column1=data["Year"].drop_duplicates().tolist()
          return render(request,"potassium3.html",{"data":column,"year":column1})
def potassium4(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("potash-fertilizer-application-per-hectare-of-cropland.csv")
          
          
          
          country1=request.POST.get("country1")
          country2=request.POST.get("country2")
          df1=df[df['Entity']==country1]
          df2=df[df['Entity']==country2]
         
          
          fig = go.Figure()

          # Create bar traces for each country
          fig.add_trace(go.Bar(
          x=df1["Year"],  # X-axis data (categories)
          y=df1["Nutrient potash K2O (total) | 00003104 || Use per area of cropland | 005159 || Kilograms per hectare"],  # Y-axis data (values)
          name=country1,
          marker=dict(color="#001f3f"),  # Bar color
          ))

          fig.add_trace(go.Bar(
          x=df2["Year"],
          y=df2["Nutrient potash K2O (total) | 00003104 || Use per area of cropland | 005159 || Kilograms per hectare"],
          name=country2,
          marker=dict(color="#0041a4"),
          ))

          # Update layout for a bar chart
          fig.update_layout(
          barmode='group',
          xaxis_title="Year",
          yaxis_title="Potash used kg/ha",
          title=f"Potash fertilizer use per hectare of cropland by {country1} and {country2}",
          plot_bgcolor="lightsteelblue",
          height=600,
          width=1200,
          title_font_size=25,
          font=dict(family="Verdana", size=18, color="black"),
          title_x=0.5,
          xaxis_title_font_size=25,
          yaxis_title_font_size=25,
          xaxis=dict(showgrid=True, showline=True, gridcolor="Lightgray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"),
          xaxis_type="category",  # Set x-axis for categorical data (Year)
          )
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
     
     else:
          data=pd.read_csv("potash-fertilizer-application-per-hectare-of-cropland.csv")
          
          word_to_exclude = '(FAO)'

# Filter rows that DON'T contain the word and assign the result back to the DataFrame
          data = data[~data['Entity'].str.contains(word_to_exclude)]
          
          column=data["Entity"].drop_duplicates().tolist()
          

          
          return render(request,"potassium4.html",{"data":column})
def potassium5(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("potash-fertilizer-application-per-hectare-of-cropland.csv")
          country1=request.POST.get("country1")
          country2=request.POST.get("country2")
          country3=request.POST.get("country3")
          df1=df[df['Entity']==country1]
          df2=df[df['Entity']==country2]
          df3=df[df['Entity']==country3]
          
          fig = go.Figure()
          fig.add_traces(go.Scatter(x=df1["Year"],y=df1["Nutrient potash K2O (total) | 00003104 || Use per area of cropland | 005159 || Kilograms per hectare"],mode="lines",name=country1,
                                   line=dict(color="#001f3f",width=3),
                                   ))
          fig.add_traces(go.Scatter(x=df2["Year"],y=df2["Nutrient potash K2O (total) | 00003104 || Use per area of cropland | 005159 || Kilograms per hectare"],mode="lines+markers",name=country2,
                                   line=dict(color="#0041a4",width=3),marker=dict(symbol="square")
                                   ))
          fig.add_traces(go.Scatter(x=df3["Year"],y=df3["Nutrient potash K2O (total) | 00003104 || Use per area of cropland | 005159 || Kilograms per hectare"],mode="lines+markers",name=country3,
                                   line=dict(color="#f8b28b",width=3),marker=dict(symbol="circle")
                                   ))
          fig.update_layout(xaxis_title="Year", yaxis_title="Potash used kg/ha", title=f"Potash fertilizer use per hectare of cropland by {country1}, {country2} and {country3}", xaxis_type="category",plot_bgcolor= "lightsteelblue",
          height=600,
          width=1200,
          #paper_bgcolor="#f8b28b",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=True, showline=True,gridcolor="Lightgray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))    
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
     
     else:
          data=pd.read_csv("potash-fertilizer-application-per-hectare-of-cropland.csv")
          word_to_exclude = '(FAO)'

# Filter rows that DON'T contain the word and assign the result back to the DataFrame
          data = data[~data['Entity'].str.contains(word_to_exclude)]
          column=data["Entity"].drop_duplicates().tolist()
          
          return render(request,"potassium5.html",{"data":column})
def potassium6(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("potash-fertilizer-application-per-hectare-of-cropland.csv")
          country1=request.POST.get("country1")
          country2=request.POST.get("country2")
          country3=request.POST.get("country3")
          startyear=int(request.POST.get("startyear"))
          endyear=int(request.POST.get("endyear"))
          df1=df[df['Entity']==country1]
          df1=df1[(df1["Year"]>=startyear) & (df1["Year"]<=endyear)]
          df2=df[df['Entity']==country2]
          df2=df2[(df2["Year"]>=startyear) & (df2["Year"]<=endyear)]
          df3=df[df['Entity']==country3]
          df3=df3[(df3["Year"]>=startyear) & (df3["Year"]<=endyear)]
         
          
          fig = go.Figure()
          fig.add_traces(go.Bar(x=df1["Year"],y=df1["Nutrient potash K2O (total) | 00003104 || Use per area of cropland | 005159 || Kilograms per hectare"],
          name=country1,
          marker=dict(color="#001f3f")
                                   ))
          fig.add_traces(go.Bar(x=df2["Year"],y=df2["Nutrient potash K2O (total) | 00003104 || Use per area of cropland | 005159 || Kilograms per hectare"],name=country2,
          marker=dict(color="#0041a4")
                                    
                                   ))
          fig.add_traces(go.Bar(x=df3["Year"],y=df3["Nutrient potash K2O (total) | 00003104 || Use per area of cropland | 005159 || Kilograms per hectare"],name=country3,
          marker=dict(color="#698b90")
                                    
                                   ))
          fig.update_layout(xaxis_title="Year", yaxis_title="Potash used kg/ha", title=f"Potash fertilizer use per hectare of cropland by {country1}, {country2} and {country3}", xaxis_type="category",plot_bgcolor= "lightsteelblue",
          height=600,
          width=1200,
          #paper_bgcolor="#f8b28b",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=True, showline=True,gridcolor="Lightgray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))    
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
     
     else:
          data=pd.read_csv("potash-fertilizer-application-per-hectare-of-cropland.csv")
          word_to_exclude = '(FAO)'
          data = data[~data['Entity'].str.contains(word_to_exclude)]
          column=data["Entity"].drop_duplicates().tolist()
          
          column1=data["Year"].drop_duplicates().tolist()
          return render(request,"potassium6.html",{"data":column,"year":column1})
def potassium7(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("potash-fertilizer-application-per-hectare-of-cropland.csv")
          year=int(request.POST.get("year"))
          df1=df[df['Year']==year]
          df1=df1.dropna()
          df1=df1.sort_values(by="Nutrient potash K2O (total) | 00003104 || Use per area of cropland | 005159 || Kilograms per hectare",ascending=False)
          n=int(request.POST.get("n"))
          dfmax=df1.head(n)
          
          fig = go.Figure()
          fig.add_trace(go.Pie(labels=dfmax["Entity"],values=dfmax["Nutrient potash K2O (total) | 00003104 || Use per area of cropland | 005159 || Kilograms per hectare"], textinfo='percent',hole=.3
                               
                                   ))
          fig.update_layout(
                   title=f"Potash fertilizer use per hectare of cropland by top {n} countries in {year}", plot_bgcolor= "lightsteelblue",
          height=600,
          width=1200,
          paper_bgcolor="lightsteelblue",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,)    
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
     
     else:
          data=pd.read_csv("potash-fertilizer-application-per-hectare-of-cropland.csv")
          column=data["Entity"].drop_duplicates().tolist()
          column1=data["Year"].drop_duplicates().tolist()
          return render(request,"potassium7.html",{"data":column,"year":column1})
def potassium8(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     a=mark_safe('<iframe src="https://ourworldindata.org/explorers/fertilizers?time=2021&facet=none&pickerSort=asc&hideControls=true&Input=Synthetic+fertilizer&Nutrient=Potassium&Metric=Applied+%28per+hectare%29&Share+of+world+total=false&country=Eastern+Asia~OWID_WRL&tab=map" loading="lazy" style="width: 110%; height: 630px; border: 0px none; margin-left: -140px;overflow: hidden;" allow="web-share; clipboard-write"></iframe>')
     
     
          
     return render(request,"fertilizer_result_worldmap.html",{'map':a})


def potassium_link(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     user=register.objects.get(email=request.session['email'])     
     return render(request,'potassium_link.html',{'user':user})


def rice_link(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     user=register.objects.get(email=request.session['email'])       
     return render(request,'rice_link.html',{'user':user})

def rice1(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("rice-production.csv")
          country=request.POST.get("country")
          #filtering the dataset
          df1=df[df["Entity"]==country]
          
          fig = go.Figure()   
          fig.add_traces(go.Scatter(x=df1["Year"],y=df1["Production"],mode="lines",name=country,
                                   line=dict(color="#001f3f",width=5),
                            fill='tozeroy', 
                                   
                                   ))
          
          
          fig.update_layout(xaxis_title="Year", yaxis_title="Rice Production (in Tonnes)", title=f"Rice Production (in Tonnes) in {country}", xaxis_type="category",plot_bgcolor= "white",
          height=600,
          width=1200,
          #paper_bgcolor="#f8b28b",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=True, showline=True,gridcolor="Lightgray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black")) 
          
          
          
          
          
          fig.update_traces(
               hovertemplate="%{y} Tonnes<br>Year: %{x}", 
               line_color="black"
          )
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
          
     else:
          data=pd.read_csv("rice-production.csv")
          word_to_exclude = '(FAO)'
          data = data[~data['Entity'].str.contains(word_to_exclude)]
          column=data["Entity"].drop_duplicates().tolist()
          
          column=data["Entity"].drop_duplicates().tolist()
          return render(request,"rice1.html",{"data":column})


def rice2(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("rice-production.csv")
          year=int(request.POST.get("year"))
          print(year)
          #filtering the dataset
          df1=df[df["Year"]==year]
          
          word_to_exclude = '(FAO)'
          df1 = df1[~df1['Entity'].str.contains(word_to_exclude)]
          
          word_to_exclude = 'World'
          df1 = df1[~df1['Entity'].str.contains(word_to_exclude)]
          
          word_to_exclude = 'Asia'
          df1 = df1[~df1['Entity'].str.contains(word_to_exclude)]
          
          
          fig=px.bar(df1,y="Production",x="Entity"
         )
          fig.update_layout(xaxis_title="Country", yaxis_title="Production (in Tonnes)", title=f"Rice Production (in Tonnes) in {year}", xaxis_type="category",plot_bgcolor= "white",
          height=600,
          width=1200,
          paper_bgcolor="lightsteelblue",title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=False, showline=True, linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))
          fig.update_traces(
               hovertemplate="%{y} Tonnes<br>Year: %{x}",marker_color="black"
          )
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
          
     else:
          data=pd.read_csv("rice-production.csv")
          column=data["Year"].drop_duplicates().tolist()
          return render(request,"rice2.html",{"data":column})

def rice3(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("rice-production.csv")
          country=request.POST.get("country")
          print(country)
          startyear=int(request.POST.get("startyear"))
          print(startyear)
          endyear=int(request.POST.get("endyear"))
          print(endyear)
         
          #filtering the dataset
          df1=df[df['Entity'] == country]
          print(df1)
          
          df1=df1[(df1["Year"]>=startyear) & (df1["Year"]<=endyear)]
          
          print(df1)
          
          fig=px.scatter(df1,y="Production",x="Year",size="Production",size_max=40,color="Production"
          )
          fig.update_layout(xaxis_title="Year", yaxis_title="Production (in Tonnes)", title=f"Rice Production (in Tonnes) of {country} from {startyear} to {endyear}", xaxis_type="category",plot_bgcolor= "white",
          height=600,
          width=1200,
          paper_bgcolor="lightsteelblue",title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=False, showline=True, linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))
         
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
          
     else:
          data=pd.read_csv("rice-production.csv")
          word_to_exclude = '(FAO)'
          data = data[~data['Entity'].str.contains(word_to_exclude)]
          column=data["Entity"].drop_duplicates().tolist()
          
          return render(request,"rice3.html",{"data":column})

def rice4(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("rice-production.csv")
          country1=request.POST.get("country1")
          country2=request.POST.get("country2")
          df1=df[df['Entity']==country1]
          df2=df[df['Entity']==country2]
         
          
          fig = go.Figure()
          fig.add_traces(go.Bar(x=df1["Year"],y=df1["Production"],name=country1,marker_color="#001f3f"
                                   
                                   ))
          fig.add_traces(go.Bar(x=df2["Year"],y=df2["Production"],name=country2,marker_color="#0041a4"
                                   
                                   ))
          fig.update_layout(xaxis_title="Year", yaxis_title="Production (in Tonnes)", title=f" Rice Production (in Tonnes) of {country1} and {country2}", xaxis_type="category",plot_bgcolor= "lightsteelblue",
          height=600,
          width=1200,
          #paper_bgcolor="lightsteelblue",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=True, showline=True,gridcolor="Lightgray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))
          
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
     
     else:
          data=pd.read_csv("rice-production.csv")
          word_to_exclude = '(FAO)'
          data = data[~data['Entity'].str.contains(word_to_exclude)]
          
          column=data["Entity"].drop_duplicates().tolist()
          return render(request,"rice4.html",{"data":column})

def rice5(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("rice-production.csv")
          country1=request.POST.get("country1")
          country2=request.POST.get("country2")
          country3=request.POST.get("country3")
          df1=df[df['Entity']==country1]
          df2=df[df['Entity']==country2]
          df3=df[df['Entity']==country3]
         
          
          fig = go.Figure()
          fig.add_traces(go.Scatter(x=df1["Year"],y=df1["Production"],mode="lines",name=country1,
                                   line=dict(color="#001f3f",width=3),
                                   ))
          fig.add_traces(go.Scatter(x=df2["Year"],y=df2["Production"],mode="lines+markers",name=country2,
                                   line=dict(color="#0041a4",width=3),marker=dict(symbol="square")
                                   ))
          fig.add_traces(go.Scatter(x=df3["Year"],y=df3["Production"],mode="lines+markers",name=country3,
                                   line=dict(color="#f8b28b",width=3),marker=dict(symbol="circle")
                                   ))
          fig.update_layout(xaxis_title="Year", yaxis_title="Production (in Tonnes", title=f"Rice Production (in Tonnes) of {country1}, {country2} and {country3}", xaxis_type="category",plot_bgcolor= "lightsteelblue",
          height=600,
          width=1200,
          #paper_bgcolor="#f8b28b",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=True, showline=True,gridcolor="Lightgray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))    
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
     
     else:
          data=pd.read_csv("rice-production.csv")
          word_to_exclude = '(FAO)'
          data = data[~data['Entity'].str.contains(word_to_exclude)]
          
          column=data["Entity"].drop_duplicates().tolist()
          return render(request,"rice5.html",{"data":column})

def rice6(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("rice-production.csv")
          country1=request.POST.get("country1")
          country2=request.POST.get("country2")
          country3=request.POST.get("country3")
          startyear=int(request.POST.get("startyear"))
          endyear=int(request.POST.get("endyear"))
          df1=df[df['Entity']==country1]
          df1=df1[(df1["Year"]>=startyear) & (df1["Year"]<=endyear)]
          df2=df[df['Entity']==country2]
          df2=df2[(df2["Year"]>=startyear) & (df2["Year"]<=endyear)]
          df3=df[df['Entity']==country3]
          df3=df3[(df3["Year"]>=startyear) & (df3["Year"]<=endyear)]
         
          
          fig = go.Figure()
          fig.add_traces(go.Bar(x=df1["Year"],y=df1["Production"],name=country1,
          marker=dict(color="#001f3f")
                                   ))
          fig.add_traces(go.Bar(x=df2["Year"],y=df2["Production"],name=country2,
          marker=dict(color="#0041a4")
                                  
                                   ))
          fig.add_traces(go.Bar(x=df3["Year"],y=df3["Production"],name=country3,marker=dict(color="#698b90")
                                   
                                   ))
          fig.update_layout(xaxis_title="Year", yaxis_title="Production (in Tonnes     ", title=f"Rice Production (in Tonnes) of {country1}, {country2} and {country3} from {startyear} to {endyear}", xaxis_type="category",plot_bgcolor= "lightsteelblue",
          height=600,
          width=1200,
          barmode='group',
          #paper_bgcolor="#f8b28b",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=True, showline=True,gridcolor="Lightgray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))    
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
     
     else:
          data=pd.read_csv("rice-production.csv")
          word_to_exclude = '(FAO)'
          data = data[~data['Entity'].str.contains(word_to_exclude)]
          
          column=data["Entity"].drop_duplicates().tolist()
          return render(request,"rice6.html",{"data":column})

def rice7(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("rice-production.csv")
          year=int(request.POST.get("year"))
          df1=df[df['Year']==year]
          df1=df1.dropna()
          
          #Dropping World as a Entity from the dataframe
          index_names = df1[ df1['Entity'] == "World" ].index 
          df1.drop(index_names, inplace = True) 
          
          df1=df1.sort_values(by="Production",ascending=False)
          n=int(request.POST.get("n"))
          dfmax=df1.head(n)
          
          fig = go.Figure()
          fig.add_trace(go.Pie(labels=dfmax["Entity"],values=dfmax["Production"], textinfo='percent',hole=.3
                               
                                   ))
          fig.update_layout(xaxis_title="Country", yaxis_title="Production (in Tonnes)", title=f"Rice Production (in Tonnes) of top {n} countries in {year}", xaxis_type="category",plot_bgcolor= "lightsteelblue",
          height=600,
          width=1200,
          paper_bgcolor="lightsteelblue",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=True, showline=True,gridcolor="Lightgray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))    
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
     
     else:
          data=pd.read_csv("rice-production.csv")
          column=data["Entity"].drop_duplicates().tolist()
          return render(request,"rice7.html",{"data":column})

def rice8(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     a=mark_safe('<iframe src="https://ourworldindata.org/grapher/rice-production?tab=map" loading="lazy" style="width: 110%; height: 630px; border: 0px none; margin-left: -140px;overflow: hidden;"></iframe>')
          
     return render(request,"fertilizer_result_worldmap.html",{'map':a})


def maize_link(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     user=register.objects.get(email=request.session['email'])     

     return render(request,'maize_link.html',{'user':user})


def maize1(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("maize-production.csv")
          country=request.POST.get("country")
          #filtering the dataset
          df1=df[df["Entity"]==country]
          fig = go.Figure()   
          fig.add_traces(go.Scatter(x=df1["Year"],y=df1["Maize | 00000056 || Production | 005510 || tonnes"],mode="lines",name=country,
                                   line=dict(color="#001f3f",width=3),
                            fill='tonexty',  
               )
                                   
                                   )
          
          fig.update_layout(xaxis_title="Year", yaxis_title="Maize Production (in Tonnes)", title=f"Maize Production (in Tonnes) of {country}", xaxis_type="category",plot_bgcolor= "white",
                            height=600,
          width=1200,
          paper_bgcolor="white",title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=False, showline=True, linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"),)
          fig.update_traces(
               hovertemplate="%{y} kg/ha<br>Year: %{x}", 
               line_color="black"
          )
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
          
     else:
          data=pd.read_csv("maize-production.csv")
          word_to_exclude = '(FAO)'
          data = data[~data['Entity'].str.contains(word_to_exclude)]
          
          column=data["Entity"].drop_duplicates().tolist()
          return render(request,"maize1.html",{"data":column})
     
def maize2(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("maize-production.csv")
          year=int(request.POST.get("year"))
          print(year)
          #filtering the dataset
          df1=df[df["Year"]==year]
          print(df1)
          word_to_exclude = '(FAO)'
          df1 = df1[~df1['Entity'].str.contains(word_to_exclude)]
          
          word_to_exclude = 'World'
          df1 = df1[~df1['Entity'].str.contains(word_to_exclude)]
          
          word_to_exclude = 'Asia'
          df1 = df1[~df1['Entity'].str.contains(word_to_exclude)]
          word_to_exclude = 'Democratic Republic of Congo'
          df1 = df1[~df1['Entity'].str.contains(word_to_exclude)]
          word_to_exclude = 'Saint Vincent and the Grenadines'
          df1 = df1[~df1['Entity'].str.contains(word_to_exclude)]
          
          
          fig=px.bar(df1,y="Maize | 00000056 || Production | 005510 || tonnes",x="Entity"
          )
          fig.update_layout(xaxis_title="Country", yaxis_title="Maize Production (in tonnes)", title=f"Maize Production (in tonnes) {year}", xaxis_type="category",plot_bgcolor= "white",
          height=600,
          width=1200,
          paper_bgcolor="lightsteelblue",title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=False, showline=True, linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))
          fig.update_traces(
               hovertemplate="%{y} kg/ha<br>Country: %{x}",marker_color="black"
          )
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
          
     else:
          return render(request,"maize2.html")
     

def maize3(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("maize-production.csv")
          country=request.POST.get("country")
          print(country)
          startyear=int(request.POST.get("startyear"))
          print(startyear)
          endyear=int(request.POST.get("endyear"))
          print(endyear)
         
          #filtering the dataset
          df1=df[df['Entity'] == country]
          print(df1)
          
          df1=df1[(df1["Year"]>=startyear) & (df1["Year"]<=endyear)]
          
          print(df1)
          
          fig=px.scatter(df1,y="Maize | 00000056 || Production | 005510 || tonnes",x="Year",size="Maize | 00000056 || Production | 005510 || tonnes",size_max=40,color="Year"
          )
          fig.update_layout(xaxis_title="Country", yaxis_title="Maize Production (in tonnes)", title=f"Maize Production (in tonnes) from {startyear} to {endyear}", xaxis_type="category",plot_bgcolor= "white",
          height=600,
          width=1200,
          paper_bgcolor="lightsteelblue",title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=False, showline=True, linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))
         
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
          
     else:
          data=pd.read_csv("maize-production.csv")
          word_to_exclude = '(FAO)'
          data = data[~data['Entity'].str.contains(word_to_exclude)]
          
          column=data["Entity"].drop_duplicates().tolist()
          column1=data["Year"].drop_duplicates().tolist()
          return render(request,"maize3.html",{"data":column,"year":column1})
     



def maize4(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("maize-production.csv")
          country1=request.POST.get("country1")
          country2=request.POST.get("country2")
          df1=df[df['Entity']==country1]
          df2=df[df['Entity']==country2]
         
          
          fig = go.Figure()
          fig.add_traces(go.Bar(x=df1["Year"],y=df1["Maize | 00000056 || Production | 005510 || tonnes"],name=country1,marker_color="#001f3f"
                                   
                                   ))
          fig.add_traces(go.Bar(x=df2["Year"],y=df2["Maize | 00000056 || Production | 005510 || tonnes"],name=country2,marker_color="#0041a4"
                                   
                                   ))
          fig.update_layout(xaxis_title="Year", yaxis_title="Maize Production (in Tonnes)", title=f" Mazie Production (in Tonnes) of {country1} and {country2}", xaxis_type="category",plot_bgcolor= "lightsteelblue",
          height=600,
          width=1200,
          #paper_bgcolor="lightsteelblue",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=True, showline=True,gridcolor="Lightgray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))    
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
     
     else:
          data=pd.read_csv("maize-production.csv")
          word_to_exclude = '(FAO)'
          data = data[~data['Entity'].str.contains(word_to_exclude)]
          
          column=data["Entity"].drop_duplicates().tolist()
          return render(request,"maize4.html",{"data":column})


def maize5(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("maize-production.csv")
          country1=request.POST.get("country1")
          country2=request.POST.get("country2")
          country3=request.POST.get("country3")
          df1=df[df['Entity']==country1]
          df2=df[df['Entity']==country2]
          df3=df[df['Entity']==country3]
         
          
          fig = go.Figure()
          fig.add_traces(go.Scatter(x=df1["Year"],y=df1["Maize | 00000056 || Production | 005510 || tonnes"],mode="lines",name=country1,
                                   line=dict(color="#001f3f",width=3),
                                   ))
          fig.add_traces(go.Scatter(x=df2["Year"],y=df2["Maize | 00000056 || Production | 005510 || tonnes"],mode="lines+markers",name=country2,
                                   line=dict(color="#0041a4",width=3),marker=dict(symbol="square")
                                   ))
          fig.add_traces(go.Scatter(x=df3["Year"],y=df3["Maize | 00000056 || Production | 005510 || tonnes"],mode="lines+markers",name=country3,
                                   line=dict(color="#f8b28b",width=3),marker=dict(symbol="circle")
                                   ))
          fig.update_layout(xaxis_title="Country", yaxis_title="Maize Production in tonnes", title=f"Maize  Production in Tonnes of {country1} , {country2} and {country3}", xaxis_type="category",plot_bgcolor= "lightsteelblue",
          height=600,
          width=1200,
          #paper_bgcolor="#f8b28b",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=True, showline=True,gridcolor="Lightgray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))    
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
     
     else:
          data=pd.read_csv("maize-production.csv")
          word_to_exclude = '(FAO)'
          data = data[~data['Entity'].str.contains(word_to_exclude)]
          
          column=data["Entity"].drop_duplicates().tolist()
          return render(request,"maize5.html",{"data":column})
     

def maize6(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("maize-production.csv")
          country1=request.POST.get("country1")
          country2=request.POST.get("country2")
          country3=request.POST.get("country3")
          startyear=int(request.POST.get("startyear"))
          endyear=int(request.POST.get("endyear"))
          df1=df[df['Entity']==country1]
          df1=df1[(df1["Year"]>=startyear) & (df1["Year"]<=endyear)]
          df2=df[df['Entity']==country2]
          df2=df2[(df2["Year"]>=startyear) & (df2["Year"]<=endyear)]
          df3=df[df['Entity']==country3]
          df3=df3[(df3["Year"]>=startyear) & (df3["Year"]<=endyear)]
         
          
          fig = go.Figure()
          fig.add_traces(go.Scatter(x=df1["Year"],y=df1["Maize | 00000056 || Production | 005510 || tonnes"],mode="lines",name=country1,
                                   line=dict(color="#001f3f",width=4),
                                   ))
          fig.add_traces(go.Scatter(x=df2["Year"],y=df2["Maize | 00000056 || Production | 005510 || tonnes"],mode="lines+markers",name=country2,
                                   line=dict(color="#0041a4",width=4),marker=dict(symbol="square")
                                   ))
          fig.add_traces(go.Scatter(x=df3["Year"],y=df3["Maize | 00000056 || Production | 005510 || tonnes"],mode="lines+markers",name=country3,
                                   line=dict(color="#698b90",width=4),marker=dict(symbol="circle")
                                   ))
          fig.update_layout(xaxis_title="Country", yaxis_title="Maize Production (in tonnes)", title=f"Maize Production in Tonnes of {country1} , {country2} and {country3}", xaxis_type="category",plot_bgcolor= "lightsteelblue",
          height=600,
          width=1200,
          #paper_bgcolor="#f8b28b",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=True, showline=True,gridcolor="Lightgray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))    
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
     
     else:
          data=pd.read_csv("maize-production.csv")
          word_to_exclude = '(FAO)'
          data = data[~data['Entity'].str.contains(word_to_exclude)]
          
          column=data["Entity"].drop_duplicates().tolist()
          column1=data["Year"].drop_duplicates().tolist()
          return render(request,"maize6.html",{"data":column,"year":column1})

def maize7(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("maize-production.csv")
          year=int(request.POST.get("year"))
          
          df1=df[df['Year']==year]
          index_names = df1[ df1['Entity'] == "World" ].index 
          df1.drop(index_names, inplace = True) 
          
          df1=df1.dropna()
          df1=df1.sort_values(by="Maize | 00000056 || Production | 005510 || tonnes",ascending=False)
          n=int(request.POST.get("n"))
          dfmax=df1.head(n)
          
          fig = go.Figure()
          fig.add_trace(go.Pie(labels=dfmax["Entity"],values=dfmax["Maize | 00000056 || Production | 005510 || tonnes"], textinfo='percent',hole=.3
                                   ))
          fig.update_layout(xaxis_title="Country", yaxis_title="Maize Production in tonnes", title=f"Maize Production in tonnes of top {n} countries in {year}", xaxis_type="category",plot_bgcolor= "lightsteelblue",
          height=600,
          width=1200,
          paper_bgcolor="lightsteelblue",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=True, showline=True,gridcolor="Lightgray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))    
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
     
     else:
          data=pd.read_csv("maize-production.csv")
          column=data["Entity"].drop_duplicates().tolist()
          column1=data["Year"].drop_duplicates().tolist()
          return render(request,"maize7.html",{"data":column,"year":column1})


def maize8(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     a=mark_safe('<iframe src="https://ourworldindata.org/grapher/maize-production?tab=map" loading="lazy" style="width: 110%; height: 630px; border: 0px none; margin-left: -140px;overflow: hidden;"></iframe>')
          
     return render(request,"fertilizer_result_worldmap.html",{'map':a})



def wheat_link(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     user=register.objects.get(email=request.session['email']) 
     return render(request,'wheat_link.html',{'user':user})

def wheat1(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("wheat-production.csv")
          country=request.POST.get("country")
          #filtering the dataset
          df1=df[df["Entity"]==country]
          fig = go.Figure()   
          fig.add_traces(go.Scatter(x=df1["Year"],y=df1["Wheat | 00000015 || Production | 005510 || tonnes"],mode="lines",name=country,
                                   line=dict(color="#001f3f",width=3),
                            fill='tonexty', ))
          
          fig.update_layout(xaxis_title="Year", yaxis_title="Wheat Production (in tonnes)", title=f"Wheat Production (in tonnes) of {country}", xaxis_type="category",plot_bgcolor= "white",
          width=1200,height=600,
          paper_bgcolor="lightsteelblue",title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=False, showline=True, linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"),)
          fig.update_traces(
               hovertemplate="%{y} kg/ha<br>Year: %{x}", 
               line_color="black"
          )
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
          
     else:
          data=pd.read_csv("wheat-production.csv")
          word_to_exclude = '(FAO)'
          data = data[~data['Entity'].str.contains(word_to_exclude)]
          column=data["Entity"].drop_duplicates().tolist()
          return render(request,"wheat1.html",{"data":column})
     
def wheat2(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("wheat-production.csv")
          year=int(request.POST.get("year"))
          print(year)
          #filtering the dataset
          df1=df[df["Year"]==year]
          print(df1)
          word_to_exclude = '(FAO)'
          df1 = df1[~df1['Entity'].str.contains(word_to_exclude)]
          
          word_to_exclude = 'World'
          df1 = df1[~df1['Entity'].str.contains(word_to_exclude)]
          
          word_to_exclude = 'Asia'
          df1 = df1[~df1['Entity'].str.contains(word_to_exclude)]
          
          fig=px.bar(df1,y="Wheat | 00000015 || Production | 005510 || tonnes",x="Entity"
          )
          fig.update_layout(xaxis_title="Country", yaxis_title="Wheat Production (in tonnes) ", title=f"Wheat Production (in tonnes) in {year}", xaxis_type="category",plot_bgcolor= "white",
          height=600,
          width=1200,
          paper_bgcolor="lightsteelblue",title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=False, showline=True, linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))
          fig.update_traces(
               hovertemplate="%{y} kg/ha<br>Country: %{x}",marker_color="black"
          )
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
          
     else:
          return render(request,"wheat2.html")
     

def wheat3(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("wheat-production.csv")
          country=request.POST.get("country")
          print(country)
          startyear=int(request.POST.get("startyear"))
          print(startyear)
          endyear=int(request.POST.get("endyear"))
          print(endyear)
         
          #filtering the dataset
          df1=df[df['Entity'] == country]
          print(df1)
          
          df1=df1[(df1["Year"]>=startyear) & (df1["Year"]<=endyear)]
          
          print(df1)
          
          fig=px.scatter(df1,y="Wheat | 00000015 || Production | 005510 || tonnes",x="Year",size="Wheat | 00000015 || Production | 005510 || tonnes",size_max=40,color="Year"
          )
          fig.update_layout(xaxis_title="Country", yaxis_title="Wheat Production (in tonnes)", title=f"Wheat Production (in tonnes) from {startyear} to {endyear}", xaxis_type="category",plot_bgcolor= "white",
          height=600,
          width=1200,
          paper_bgcolor="lightsteelblue",title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=False, showline=True, linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))
         
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
          
     else:
          data=pd.read_csv("wheat-production.csv")
          word_to_exclude = '(FAO)'
          data = data[~data['Entity'].str.contains(word_to_exclude)]
          
          column=data["Entity"].drop_duplicates().tolist()
          column1=data["Year"].drop_duplicates().tolist()
          return render(request,"wheat3.html",{"data":column,"year":column1})
     

def wheat4(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("wheat-production.csv")
          country1=request.POST.get("country1")
          country2=request.POST.get("country2")
          df1=df[df['Entity']==country1]
          df2=df[df['Entity']==country2]
         
          fig = go.Figure()
          fig.add_traces(go.Bar(x=df1["Year"],y=df1["Wheat | 00000015 || Production | 005510 || tonnes"],name=country1,marker_color="#001f3f"
                                   
                                   ))
          fig.add_traces(go.Bar(x=df2["Year"],y=df2["Wheat | 00000015 || Production | 005510 || tonnes"],name=country2,marker_color="#0041a4"
                                   
                                   ))
          fig.update_layout(xaxis_title="Year", yaxis_title="Wheat Production (in Tonnes)", title=f" Wheat Production (in Tonnes) of {country1} and {country2}", xaxis_type="category",plot_bgcolor= "lightsteelblue",
          height=600,
          width=1200,
          #paper_bgcolor="lightsteelblue",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=True, showline=True,gridcolor="Lightgray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black")) 
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
     
     else:
          data=pd.read_csv("wheat-production.csv")
          word_to_exclude = '(FAO)'
          df1 = df1[~df1['Entity'].str.contains(word_to_exclude)]
          
          column=data["Entity"].drop_duplicates().tolist()
          return render(request,"wheat4.html",{"data":column})
     
def wheat5(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("wheat-production.csv")
          country1=request.POST.get("country1")
          country2=request.POST.get("country2")
          country3=request.POST.get("country3")
          df1=df[df['Entity']==country1]
          df2=df[df['Entity']==country2]
          df3=df[df['Entity']==country3]
         
          
          fig = go.Figure()
          fig.add_traces(go.Scatter(x=df1["Year"],y=df1["Wheat | 00000015 || Production | 005510 || tonnes"],mode="lines",name=country1,
                                   line=dict(color="#001f3f",width=3),
                                   ))
          fig.add_traces(go.Scatter(x=df2["Year"],y=df2["Wheat | 00000015 || Production | 005510 || tonnes"],mode="lines+markers",name=country2,
                                   line=dict(color="#0041a4",width=3),marker=dict(symbol="square")
                                   ))
          fig.add_traces(go.Scatter(x=df3["Year"],y=df3["Wheat | 00000015 || Production | 005510 || tonnes"],mode="lines+markers",name=country3,
                                   line=dict(color="#f8b28b",width=3),marker=dict(symbol="circle")
                                   ))
          fig.update_layout(xaxis_title="Country", yaxis_title="Wheat Production (in tonnes)", title=f"Wheat Production (in tonnes) of {country1} , {country2} and {country3}", xaxis_type="category",plot_bgcolor= "lightsteelblue",
          height=600,
          width=1200,
          #paper_bgcolor="#f8b28b",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=True, showline=True,gridcolor="Lightgray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))    
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
     
     else:
          data=pd.read_csv("wheat-production.csv")
          word_to_exclude = '(FAO)'
          data = data[~data['Entity'].str.contains(word_to_exclude)]
          column=data["Entity"].drop_duplicates().tolist()
          return render(request,"wheat5.html",{"data":column})
     

def wheat6(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("wheat-production.csv")
          country1=request.POST.get("country1")
          country2=request.POST.get("country2")
          country3=request.POST.get("country3")
          startyear=int(request.POST.get("startyear"))
          endyear=int(request.POST.get("endyear"))
          df1=df[df['Entity']==country1]
          df1=df1[(df1["Year"]>=startyear) & (df1["Year"]<=endyear)]
          df2=df[df['Entity']==country2]
          df2=df2[(df2["Year"]>=startyear) & (df2["Year"]<=endyear)]
          df3=df[df['Entity']==country3]
          df3=df3[(df3["Year"]>=startyear) & (df3["Year"]<=endyear)]
         
          fig = go.Figure()
          fig.add_traces(go.Bar(x=df1["Year"],y=df1["Wheat | 00000015 || Production | 005510 || tonnes"],name=country1,
          marker=dict(color="#001f3f")
                                   ))
          fig.add_traces(go.Bar(x=df2["Year"],y=df2["Wheat | 00000015 || Production | 005510 || tonnes"],name=country2,
          marker=dict(color="#0041a4")
                                  
                                   ))
          fig.add_traces(go.Bar(x=df3["Year"],y=df3["Wheat | 00000015 || Production | 005510 || tonnes"],name=country3,marker=dict(color="#698b90")
                                   
                                   ))
          fig.update_layout(xaxis_title="Year", yaxis_title="Wheat Production (in Tonnes)", title=f"Wheat Production (in Tonnes) of {country1}, {country2} and {country3} from {startyear} to {endyear}", xaxis_type="category",plot_bgcolor= "lightsteelblue",
          height=600,
          width=1200,
          barmode='group',
          #paper_bgcolor="#f8b28b",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=True, showline=True,gridcolor="Lightgray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))    
          
          
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
     
     else:
          data=pd.read_csv("wheat-production.csv")
          word_to_exclude = '(FAO)'
          data = data[~data['Entity'].str.contains(word_to_exclude)]
          column=data["Entity"].drop_duplicates().tolist()
          column1=data["Year"].drop_duplicates().tolist()
          return render(request,"wheat6.html",{"data":column,"year":column1})

def wheat7(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("wheat-production.csv")
          year=int(request.POST.get("year"))
          df1=df[df['Year']==year]
          index_names = df1[ df1['Entity'] == "World" ].index 
          df1.drop(index_names, inplace = True) 
          
          df1=df1.dropna()
          df1=df1.sort_values(by="Wheat | 00000015 || Production | 005510 || tonnes",ascending=False)
          n=int(request.POST.get("n"))
          dfmax=df1.head(n)
          fig = go.Figure()

          fig.add_trace(go.Pie(labels=dfmax["Entity"],values=dfmax["Wheat | 00000015 || Production | 005510 || tonnes"], textinfo='percent',hole=.3
                               
                                   ))
          
          fig.update_layout(xaxis_title="Country", yaxis_title="Wheat Production (in tonnes)", title=f"Wheat Production (in tonnes) of top {n} countries in {year}", xaxis_type="category",plot_bgcolor= "lightsteelblue",
          height=600,
          width=1200,
          paper_bgcolor="lightsteelblue",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=True, showline=True,gridcolor="Lightgray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))    
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
     
     else:
          data=pd.read_csv("wheat-production.csv")
          column=data["Entity"].drop_duplicates().tolist()
          return render(request,"wheat7.html",{"data":column})


def wheat8(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     a=mark_safe('<iframe src="https://ourworldindata.org/grapher/wheat-production?tab=map" loading="lazy" style="width: 110%; height: 630px; border: 0px none; margin-left: -140px;overflow: hidden;"></iframe>')
      
     return render(request,"fertilizer_result_worldmap.html",{'map':a})

def population_link(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     user=register.objects.get(email=request.session['email'])     
     return render(request,'population_link .html',{'user':user})

def population1(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("share_of_the_.population_in_agriculture.csv")
          country=request.POST.get("country")
          #filtering the dataset
          df1=df[df["Entity"]==country]
          
          fig = go.Figure()   
          fig.add_traces(go.Scatter(x=df1["Year"],y=df1["share_employed_agri"],mode="lines",name=country,
                                   line=dict(color="#001f3f",width=3),
                            fill='tonexty',  ))
          
          fig.update_layout(xaxis_title="Year", yaxis_title="Labor force employed (%)", title=f"Agriculturalist trend of {country}", xaxis_type="category",plot_bgcolor= "white",
          width=1200,height=600,
          paper_bgcolor="white",title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=True, showline=True, linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"),)
          fig.update_traces(
               hovertemplate="%{y} kg/ha<br>Year: %{x}", 
               line_color="black"
          )
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
          
     else:
          data=pd.read_csv("share_of_the_.population_in_agriculture.csv")
          column=data["Entity"].drop_duplicates().tolist()
          return render(request,"population1.html",{"data":column})
     
def population2(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("share_of_the_.population_in_agriculture.csv")
          year=int(request.POST.get("year"))
          print(year)
          #filtering the dataset
          
          df1=df[df["Year"]==year]
          print(df1)
          
          word_to_exclude = '(FAO)'
          df1 = df1[~df1['Entity'].str.contains(word_to_exclude)]
          
          word_to_exclude = 'IBRD'
          df1 = df1[~df1['Entity'].str.contains(word_to_exclude)]
          
          word_to_exclude = 'income'
          df1 = df1[~df1['Entity'].str.contains(word_to_exclude)]
          fig=px.bar(df1,y="share_employed_agri",x="Entity"
          )
          fig.update_layout(xaxis_title="Country", yaxis_title="Labor force employed (%)", title=f"Agriculturalist trend of world {year}", xaxis_type="category",plot_bgcolor= "white",
          height=600,
          width=1200,
          paper_bgcolor="lightsteelblue",title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=False, showline=True, linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))
          fig.update_traces(
               hovertemplate="%{y} kg/ha<br>Country: %{x}",marker_color="black"
          )
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
          
     else:
          return render(request,"population2.html")
     

def population3(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("share_of_the_.population_in_agriculture.csv")
          country=request.POST.get("country")
          print(country)
          startyear=int(request.POST.get("startyear"))
          print(startyear)
          endyear=int(request.POST.get("endyear"))
          print(endyear)
         
          #filtering the dataset
          df1=df[df['Entity'] == country]
          print(df1)
          
          df1=df1[(df1["Year"]>=startyear) & (df1["Year"]<=endyear)]
          
          print(df1)
          
          
          fig=px.scatter(df1,y="share_employed_agri",x="Year",size="share_employed_agri",size_max=40,color="Year"
          )
          fig.update_layout(xaxis_title="Year", yaxis_title="Labor force employed (%)", title=f"Agriculturalist trend of {country} from {startyear} to {endyear}", xaxis_type="category",plot_bgcolor= "white",
          height=600,
          width=1200,
          paper_bgcolor="lightsteelblue",title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=False, showline=True, linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))
         
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
          
     else:
          data=pd.read_csv("share_of_the_.population_in_agriculture.csv")
          column=data["Entity"].drop_duplicates().tolist()
          
          return render(request,"population3.html",{"data":column})
     

def population4(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("share_of_the_.population_in_agriculture.csv")
          country1=request.POST.get("country1")
          country2=request.POST.get("country2")
          df1=df[df['Entity']==country1]
          df2=df[df['Entity']==country2]
         
          fig = go.Figure()
          fig.add_traces(go.Bar(x=df1["Year"],y=df1["share_employed_agri"],name=country1,marker_color="#001f3f"
                                   
                                   ))
          fig.add_traces(go.Bar(x=df2["Year"],y=df2["share_employed_agri"],name=country2,marker_color="#0041a4"
                                   
                                   ))
          
          fig.update_layout(xaxis_title="Year", yaxis_title="Labor force employed (%)", title=f"Agriculturalist trend of {country1} and {country2}", xaxis_type="category",plot_bgcolor= "lightsteelblue",
          height=600,
          width=1200,
          #paper_bgcolor="#f8b28b",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=True, showline=True,gridcolor="Lightgray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))    
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
     
     else:
          data=pd.read_csv("share_of_the_.population_in_agriculture.csv")
          column=data["Entity"].drop_duplicates().tolist()
          return render(request,"population4.html",{"data":column})
     
def population5(request):     
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("share_of_the_.population_in_agriculture.csv")
          country1=request.POST.get("country1")
          country2=request.POST.get("country2")
          country3=request.POST.get("country3")
          df1=df[df['Entity']==country1]
          df2=df[df['Entity']==country2]
          df3=df[df['Entity']==country3]
         
          
          fig = go.Figure()
          fig.add_traces(go.Scatter(x=df1["Year"],y=df1["share_employed_agri"],mode="lines",name=country1,
                                   line=dict(color="#001f3f",width=3),
                                   ))
          fig.add_traces(go.Scatter(x=df2["Year"],y=df2["share_employed_agri"],mode="lines+markers",name=country2,
                                   line=dict(color="#0041a4",width=3),marker=dict(symbol="square")
                                   ))
          fig.add_traces(go.Scatter(x=df3["Year"],y=df3["share_employed_agri"],mode="lines+markers",name=country3,
                                   line=dict(color="#f8b28b",width=3),marker=dict(symbol="circle")
                                   ))
          fig.update_layout(xaxis_title="Year", yaxis_title="Labor force employed (%)", title=f"Agriculturalist trend of {country1}, {country2} and {country3}", xaxis_type="category",plot_bgcolor= "lightsteelblue",
          height=600,
          width=1200,
          #paper_bgcolor="#f8b28b",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=True, showline=True,gridcolor="Lightgray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))    
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
     
     else:
          data=pd.read_csv("share_of_the_.population_in_agriculture.csv")
          column=data["Entity"].drop_duplicates().tolist()
          return render(request,"population5.html",{"data":column})
     

def population6(request):     
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("share_of_the_.population_in_agriculture.csv")
          country1=request.POST.get("country1")
          country2=request.POST.get("country2")
          country3=request.POST.get("country3")
          startyear=int(request.POST.get("startyear"))
          endyear=int(request.POST.get("endyear"))
          df1=df[df['Entity']==country1]
          df1=df1[(df1["Year"]>=startyear) & (df1["Year"]<=endyear)]
          df2=df[df['Entity']==country2]
          df2=df2[(df2["Year"]>=startyear) & (df2["Year"]<=endyear)]
          df3=df[df['Entity']==country3]
          df3=df3[(df3["Year"]>=startyear) & (df3["Year"]<=endyear)]
         
          fig = go.Figure()
          fig.add_traces(go.Bar(x=df1["Year"],y=df1["share_employed_agri"],name=country1,
          marker=dict(color="#001f3f")
                                   ))
          fig.add_traces(go.Bar(x=df2["Year"],y=df2["share_employed_agri"],name=country2,
          marker=dict(color="#0041a4")
                                  
                                   ))
          fig.add_traces(go.Bar(x=df3["Year"],y=df3["share_employed_agri"],name=country3,marker=dict(color="#698b90")
                                   
                                   ))
          
          fig.update_layout(xaxis_title="Year", yaxis_title="Labor force employed (%)", title=f"Agriculturalist trend of {country1}, {country2} and {country3} from {startyear} to {endyear}", xaxis_type="category",plot_bgcolor= "lightsteelblue",
          height=600,
          width=1200,
          #paper_bgcolor="#f8b28b",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=True, showline=True,gridcolor="Lightgray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))    
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
     
     else:
          data=pd.read_csv("share_of_the_.population_in_agriculture.csv")
          column=data["Entity"].drop_duplicates().tolist()
          column1=data["Year"].drop_duplicates().tolist()
          return render(request,"population6.html",{"data":column,"year":column1})

def population7(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=="POST":
          df=pd.read_csv("share_of_the_.population_in_agriculture.csv")
          year=int(request.POST.get("year"))
          df1=df[df['Year']==year]
          df1=df1.dropna()
          df1=df1.sort_values(by="share_employed_agri",ascending=False)
          n=int(request.POST.get("n"))
          dfmax=df1.head(n)
          fig = go.Figure()

          fig.add_trace(go.Pie(labels=dfmax["Entity"],values=dfmax["share_employed_agri"], textinfo='percent',hole=.3
                               
                                   ))
          fig.update_layout(xaxis_title="Country", yaxis_title="Labor force employed (%)", title=f"Agriculturalist trend of top {n} countries in {year}", xaxis_type="category",plot_bgcolor= "lightsteelblue",
          height=600,
          width=1200,
          paper_bgcolor="lightsteelblue",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=True, showline=True,gridcolor="Lightgray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))    
          graph=fig.to_html
          return render(request,"f1result.html",{"graph":graph})
     
     else:
          data=pd.read_csv("share_of_the_.population_in_agriculture.csv")
          column=data["Entity"].drop_duplicates().tolist()
          column1=data["Year"].drop_duplicates().tolist()
          return render(request,"population7.html",{"data":column,"year":column1})


def population8(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     a=mark_safe('<iframe src="https://ourworldindata.org/grapher/share-of-the-labor-force-employed-in-agriculture?time=2019&tab=map" loading="lazy" style="width: 110%; height: 630px; border: 0px none; margin-left: -140px;overflow: hidden;"></iframe>')
          
     return render(request,"fertilizer_result_worldmap.html",{'map':a})

def fertilizers_use_analysis(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     user=register.objects.get(email=request.session['email'])
     return render(request,"fertilizers_use_analysis .html",{'user':user})

def fertilizers_use_prediction(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     user=register.objects.get(email=request.session['email'])
     return render(request,"fertilizers_use_prediction.html",{'user':user})


def crops_production_analysis(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     user=register.objects.get(email=request.session['email'])
     return render(request,"crops_production_analysis.html",{'user':user})
def crops_production_prediction(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     user=register.objects.get(email=request.session['email'])
     return render(request,"crops_production_prediction.html",{'user':user})

# Create your views here.
def footer(request):
     if request.method == "POST":
          e=request.POST.get("newsletteremail")
          if newsletter.objects.filter(email=e).exists():
               subject="Welcome Back to AGROSTAT!"
               message='''Hi ,
Great to see you back! Your continued support fuels our passion for empowering farmers with data-driven agriculture.
We're constantly enhancing AGROSTAT:
          # New features: The dashboard gets better, offering more powerful analysis and prediction tools.
          # Fresh insights: Stay ahead of the curve with our expert-authored blog posts on agricultural intelligence.
          # Exclusive events: Gain access to upcoming webinars and workshops with renowned agricultural specialists.
Maximize your experience:
          # Explore our website: [Your Website URL]
          # Read our blog for insights: [Link to a relevant blog post, if available]
          # Connect with us: Your feedback matters!
We're committed to your success. Stay tuned for exciting updates!
Sincerely,
The AGROSTAT Team
'''
               email_from=settings.EMAIL_HOST_USER
               recipient_list=[e]  
               send_mail(subject,message,email_from,recipient_list)
                 
               return JsonResponse({"message":"You are already a subscriber"})
          elif e=="":
               return JsonResponse({"message":"Enter a valid Mail id"})
               
          else:
          
               x=newsletter()
               x.email=e
               x.save()
               subject="Welcome to AGROSTAT - Empowering Farmers with Knowledge and Technology!"
               message=f'''Hi,
     Welcome to the AGROSTAT community! We're thrilled to have you join us on your journey to harnessing the power of data and technology for informed agricultural decision-making.
     AGROSTAT is a website built by passionate individuals like you, aiming to empower farmers with knowledge and technology. 
     Through our innovative agriculture intelligence dashboard, we strive to:
               # Analyze agricultural data: Gain insights into crop production, Nutrient nitrogen use,agriculturalist trends and more.
               # Make data-driven predictions: Anticipate potential issues and optimize your farming strategies for improved yields.
               # Stay informed: Access valuable resources and news articles to stay ahead of the curve in the agricultural sector.
     As a subscriber, you'll receive regular updates about:
               # New features and functionalities on the AGROSTAT platform.
               # Informative blog posts and articles on agriculture intelligence and technology trends.
               # Exclusive access to webinars and workshops hosted by agricultural experts.
     We're excited to embark on this agricultural intelligence journey with you!
     Here are some ways to get started:
               # Visit our website
               # Explore the AGROSTAT dashboard 
               # Read our latest blog post
     Feel free to reach out to us if you have any questions or suggestions. We're always happy to hear from our subscribers!
     Sincerely,
     The AGROSTAT Team
     P.S. Don't forget to follow us on social media for even more updates and engagement!
     '''
               email_from=settings.EMAIL_HOST_USER
               recipient_list=[e]  
               send_mail(subject,message,email_from,recipient_list)
                         
               return JsonResponse({"message":"Thank you for subscribling"})
     return render (request,'footer.html')

def contactus(request):
     if request.method == "POST":
          x=contact()
          x.name=request.POST.get('name')
          x.email=request.POST.get('mail')
          x.message=request.POST.get('comment')
          x.save()
          return render (request,'contactus.html',{'msg':1})
     else:
          return render (request,'contactus.html')

def index(request):
     x=Agriculture_Universities.objects.all()
     import datetime
     from datetime import date
     from newsapi import NewsApiClient
     newsapi = NewsApiClient(api_key='b5bebd12136d4ecf8878f2060de6d277')

     json_data = newsapi.get_everything(q='Agriculture',language= 'en',from_param=str(date. today() - datetime. timedelta(days=29)),to=str (date.today()),page_size=21,page = 1,sort_by='relevancy')
     k=json_data['articles']
      
     return render (request,'index.html',{'data':x,'k':k})

def login(request):
     if request.method=="POST" :
          em=request.POST.get("email")
          pw=request.POST.get("password")
          
          user=register.objects.filter(email=em,password=pw)
          k=len(user)

          if k>0:
               request.session['email']=em
               return redirect('/dashboard')
          else:
               return render(request,'login.html',{'msg':1})
          
     else:
          return render (request,'login.html')

def userprofile(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     user=register.objects.get(email=request.session['email'])
     if request.method == 'POST':
          user.profile_picture=request.FILES['image']
         
          user.save()
          return render(request,'userprofile_s.html',{'user':user,'msg':'success'})
     else:          
          return render(request,'userprofile_s.html',{'user':user})

def navbar(request):
     return render (request,'navbar.html')

def registration(request):
     if request.method == "POST":
          n=request.POST.get("name")
          e=request.POST.get("email")
          p=request.POST.get("password")
          c=request.POST.get("cpass")
          if register.objects.filter(email=e).exists():
             
               return render (request,'registration.html',{'msg' : 1})
          else: 
               if p == c:
                    otp=random.randrange(1000,9999)
                    print(otp)

                    
                    j6="0123456789"
                    j7=random.sample(j6,6)
                    print(j7)

                    j8=""
                    for i in j7:
                         j8=j8+i
                       
                    subject="OTP"
                    message="Hi your OTP is '"+ j8 +"'"
                    email_from=settings.EMAIL_HOST_USER
                    recipient_list=[e]  
                    send_mail(subject,message,email_from,recipient_list)
                  
                    return render (request,'register_otp.html',{'msg' : 2,'name':n,'email':e,'password':p,'otp':j8})
               else:
                
                    return render (request,'registration.html',{'msg' : "3",'m1':'Password and Confirm Password does not match'})
     else:
          return render (request,'registration.html')
          
     
def register_otp(request):
     if request.method == "POST":
          n=request.POST.get("name")
          e=request.POST.get("email")
          p=request.POST.get("password")
          otp=request.POST.get("otp")
          generated_otp=request.POST.get("org")
          
          
          if  otp==generated_otp:
               #del request.session['otp']
               x=register()
               x.name=n
               x.email=e
               x.password=p
               x.save()
               
               return redirect('/login',{ 'msg' : 3,'m1':'User Registered' })
          else:
               return render(request,'register_otp.html',{ 'msg' : 4,'name':n,'email':e,'password':p,'otp':otp})
     else:
          return render(request,'register_otp.html')
               
               
               
          
               
     
     
                  

def base(request):
     if request.method == "POST":
          e=request.POST.get("email")
          x=newsletter()
          x.email=e
          x.save()
          return render(request,'login.html')
          
               
     return render(request,'base.html')

def e503(request):
     return render(request,'error503.html')

def base2(request):
     return render(request,'base2.html')

def Agri_call_center(request):
     x=Agriculture_Call_centre.objects.all()
     return  render(request, 'Agri_call_center.html',{'data':x})
def Agri_crops(request):
     x=Agriculture_Crop.objects.all()
     return  render(request, 'Agri_crops.html',{'data':x})

def crop_detail(request,name):
     
     x=agri_crops_details.objects.filter(crop_identity=name)
     return  render(request, 'Agri_crops_detail1.html',{'data':x,'name':name})

def crop_detail2(request,name):
     
     x=agri_crops_details.objects.filter(crop_head=name)
     return  render(request, 'Agri_crops_detail2.html',{'data':x})

def Agri_farmer_scheme(request):
     x=Agriculture_Farmer_Scheme.objects.all()
     return  render(request, 'Agri_farmer_scheme.html',{'data':x})
def Agri_indian_uni(request):
     x=Indian_Agriculture_University.objects.all()
     return  render(request, 'Agri_indian_uni.html',{'data':x})
def Agri_dealers(request):
     x=dealers.objects.all()
     return  render(request, 'Agri_Dealers.html',{'data':x})
def Agri_latest_technology(request):
     x=Latest_Technology.objects.all()
     return  render(request, 'Agri_latest_technology.html',{'data':x})
def Agri_news(request):
     x=Agriculture_News.objects.all()
     return  render(request, 'Agri_news.html',{'data':x})

def news_detail(request,name):
     x=Agriculture_News.objects.filter(title=name)
     return  render(request, 'news_detail.html',{'data':x})
def Agri_uni(request):
     x=Agriculture_Universities.objects.all()
     return  render(request, 'Agri_uni.html',{'data':x})
def Agri_videos(request):
     x=Agriculture_Videos.objects.all()
     return  render(request, 'Agri_videos.html',{'data':x})

def review(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     
     if request.method == "POST":
          x=myreview()
          x.title=request.POST.get('ti')
          x.message=request.POST.get('msg')
          x.save()
          user=register.objects.get(email=request.session['email'])     
          
          return render(request,'review.html',{'msg':1,'user':user})
     else:
          user=register.objects.get(email=request.session['email'])     
          return render(request,'review.html',{'user':user})

def sidebar(request):
     user=register.objects.get(email=request.session['email'])     
     return render(request,'sidebar.html',{'user':user})
def sidebar11(request):
     user=register.objects.get(email=request.session['email'])     
     return render(request,'sidebar11.html',{'user':user})
 
     
def change_password(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     user=register.objects.get(email=request.session['email'])     
     return render(request,'change_password.html',{'user':user})

def help_support(request):
     if not request.session.has_key('email'):
          return render(request,'/login')
     if request.method == 'POST':
          x=support()
          x.title = request.POST.get('tt')
          x.content = request.POST.get('ct')
          x.save()
          user=register.objects.get(email=request.session['email'])     
          return render(request,'help_support.html',{'msg':1,'user':user})
     else:
          user=register.objects.get(email=request.session['email'])     
          return render(request,'help_support.html',{'user':user})
          
          

def handle_uploaded_file(f,name):
     destination = open(name, 'wb+')
     for chunk in f.chunks():
          destination.write(chunk)
     destination.close()
     
def predict_phosphorous(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=='POST':
          df=pd.read_csv("phosphate-application-per-hectare-of-cropland.csv",parse_dates=['Year'])
          df.dtypes
          country=request.POST.get('country')
          
          print(country)
          #country='India'
          production=df[df['Entity']==country]
          production=production.loc[:,['Year','Nutrient phosphate P2O5 (total) | 00003103 || Use per area of cropland | 005159 || Kilograms per hectare']]
          production=production.sort_values('Year')
          production.isnull().sum()
          production=production.set_index('Year')
          production.index
          y=production
          p = d = q = range(0, 2)
          pdq = list(itertools.product(p, d, q))
          seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
          print('Examples of parameter combinations for Seasonal ARIMA...')
          print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
          print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
          print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
          print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

          min=99999999
          p1=[-1,-1,-1]
          p2=[-1,-1,-1,-1]
          for param in pdq:
               for param_seasonal in seasonal_pdq:
                    try:
                         mod = sm.tsa.statespace.SARIMAX(y,
                                                       order=param,
                                                       seasonal_order=param_seasonal,
                                                       enforce_stationarity=False,
                                                       enforce_invertibility=False)
                         results = mod.fit()
                         if results.aic<min:
                              min=results.aic
                              p1=param
                              p2=param_seasonal
                         print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
                    except:
                         continue
          print(p1)
          print(min)
          print(p2)
          # 12 is the interval for 12 months
          mod = sm.tsa.statespace.SARIMAX(y,
                                        order=(p1[0], p1[1], p1[2]),
                                        seasonal_order=(p2[0], p2[1], p2[2], 12),
                                        enforce_stationarity=False,
                                        enforce_invertibility=False)
          results = mod.fit()
          print(results.summary().tables[1])
          steps = int(request.POST.get('steps'))
          
          print("steps are",steps)
          pred_uc = results.get_forecast(steps=steps)
               # Create traces
          fig = go.Figure()
          fig.add_trace(go.Scatter(x=y.index, y=y['Nutrient phosphate P2O5 (total) | 00003103 || Use per area of cropland | 005159 || Kilograms per hectare'],
                              mode='lines',
                              name='Actual Value',fill='tozeroy'))
          type(pred_uc.predicted_mean)
          fig.add_trace(go.Scatter(x=pred_uc.predicted_mean.index, y=pred_uc.predicted_mean,
                              mode='lines',
                              name='Predicted Value',fill='tozeroy'))
          #fig.show()
          fig.update_layout(
          title="Phosphate fertilizer use prediction per hectare of cropland by "+country,
          xaxis_title="Year",
          yaxis_title="Phosphorous Use (Kg/Ha)",
          legend_title="Country",plot_bgcolor= "lightsteelblue",
          height=600,
          width=1200,
          #paper_bgcolor="#f8b28b",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=True, showline=True,gridcolor="Lightgray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))
          graph=fig.to_html()
          return render(request,'arima_result.html',{'graph':graph})

     
     else:
          data=pd.read_csv("phosphate-application-per-hectare-of-cropland.csv")
          column=data["Entity"].drop_duplicates().tolist()
          user=register.objects.get(email=request.session['email'])     

          return render(request,'phosphorous_prediction.html',{"data":column,"user":user})

def predict_potassium(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=='POST':
          df=pd.read_csv("potash-fertilizer-application-per-hectare-of-cropland.csv",parse_dates=['Year'])
          df.dtypes
          country=request.POST.get('country')
          
          print(country)
          #country='India'
          production=df[df['Entity']==country]
          production=production.loc[:,['Year','Nutrient potash K2O (total) | 00003104 || Use per area of cropland | 005159 || Kilograms per hectare']]
          production=production.sort_values('Year')
          production.isnull().sum()
          production=production.set_index('Year')
          production.index
          y=production
          p = d = q = range(0, 2)
          pdq = list(itertools.product(p, d, q))
          seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
          print('Examples of parameter combinations for Seasonal ARIMA...')
          print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
          print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
          print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
          print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

          min=99999999
          p1=[-1,-1,-1]
          p2=[-1,-1,-1,-1]
          for param in pdq:
               for param_seasonal in seasonal_pdq:
                    try:
                         mod = sm.tsa.statespace.SARIMAX(y,
                                                       order=param,
                                                       seasonal_order=param_seasonal,
                                                       enforce_stationarity=False,
                                                       enforce_invertibility=False)
                         results = mod.fit()
                         if results.aic<min:
                              min=results.aic
                              p1=param
                              p2=param_seasonal
                         print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
                    except:
                         continue
          print(p1)
          print(min)
          print(p2)
          # 12 is the interval for 12 months
          mod = sm.tsa.statespace.SARIMAX(y,
                                        order=(p1[0], p1[1], p1[2]),
                                        seasonal_order=(p2[0], p2[1], p2[2], 12),
                                        enforce_stationarity=False,
                                        enforce_invertibility=False)
          results = mod.fit()
          print(results.summary().tables[1])
          steps = int(request.POST.get('steps'))
          
          print("steps are",steps)
          pred_uc = results.get_forecast(steps=steps)
               # Create traces
          fig = go.Figure()
          fig.add_trace(go.Scatter(x=y.index, y=y['Nutrient potash K2O (total) | 00003104 || Use per area of cropland | 005159 || Kilograms per hectare'],
                              mode='lines',
                              name='Actual Value',fill='tozeroy'))
          type(pred_uc.predicted_mean)
          fig.add_trace(go.Scatter(x=pred_uc.predicted_mean.index, y=pred_uc.predicted_mean,
                              mode='lines',
                              name='Predicted Value',fill='tozeroy'))
          #fig.show()
          fig.update_layout(
          title="Potassium fertilizer use prediction per hectare of cropland by "+country,
          xaxis_title="Year",
          yaxis_title="Potassium Use (Kg/Ha)",
          legend_title="Country",plot_bgcolor= "lightsteelblue",
          height=600,
          width=1200,
          #paper_bgcolor="#f8b28b",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=True, showline=True,gridcolor="Lightgray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))
          graph=fig.to_html()
          return render(request,'arima_result.html',{'graph':graph})

     
     else:
          data=pd.read_csv("phosphate-application-per-hectare-of-cropland.csv")
          column=data["Entity"].drop_duplicates().tolist()
          user=register.objects.get(email=request.session['email'])     

          return render(request,'potassium_prediction.html',{"data":column,"user":user})


def predict_crop_rice(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=='POST':
          df=pd.read_csv("rice-production.csv",parse_dates=['Year'])
          df.dtypes
          country=request.POST.get('country')
          
          print(country)
          #country='India'
          production=df[df['Entity']==country]
          production=production.loc[:,['Year','Production']]
          production=production.sort_values('Year')
          production.isnull().sum()
          production=production.set_index('Year')
          production.index
          y=production
          p = d = q = range(0, 2)
          pdq = list(itertools.product(p, d, q))
          seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
          print('Examples of parameter combinations for Seasonal ARIMA...')
          print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
          print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
          print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
          print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

          min=99999999
          p1=[-1,-1,-1]
          p2=[-1,-1,-1,-1]
          for param in pdq:
               for param_seasonal in seasonal_pdq:
                    try:
                         mod = sm.tsa.statespace.SARIMAX(y,
                                                       order=param,
                                                       seasonal_order=param_seasonal,
                                                       enforce_stationarity=False,
                                                       enforce_invertibility=False)
                         results = mod.fit()
                         if results.aic<min:
                              min=results.aic
                              p1=param
                              p2=param_seasonal
                         print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
                    except:
                         continue
          print(p1)
          print(min)
          print(p2)
          # 12 is the interval for 12 months
          mod = sm.tsa.statespace.SARIMAX(y,
                                        order=(p1[0], p1[1], p1[2]),
                                        seasonal_order=(p2[0], p2[1], p2[2], 12),
                                        enforce_stationarity=False,
                                        enforce_invertibility=False)
          results = mod.fit()
          print(results.summary().tables[1])
          steps = int(request.POST.get('steps'))
          
          print("steps are",steps)
          pred_uc = results.get_forecast(steps=steps)
               # Create traces
          fig = go.Figure()
          fig.add_trace(go.Scatter(x=y.index, y=y['Production'],
                              mode='lines',
                              name='Actual Value',fill='tozeroy'))
          type(pred_uc.predicted_mean)
          fig.add_trace(go.Scatter(x=pred_uc.predicted_mean.index, y=pred_uc.predicted_mean,
                              mode='lines',
                              name='Predicted Value',fill='tozeroy'))
          #fig.show()
          fig.update_layout(
          title="Rice Production (in Tonnes) prediction of "+country,
          xaxis_title="Year",
          yaxis_title="Production (in Tonnes)",
          legend_title="Country",plot_bgcolor= "lightsteelblue",
          height=600,
          width=1200,
          #paper_bgcolor="#f8b28b",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=True, showline=True,gridcolor="Lightgray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))
          graph=fig.to_html()
          return render(request,'arima_result.html',{'graph':graph})

     
     else:
          data=pd.read_csv("rice-production.csv")
          column=data["Entity"].drop_duplicates().tolist()
          user=register.objects.get(email=request.session['email'])     

          return render(request,'rice_prediction.html',{"data":column,"user":user})
     

def predict_crop_maize(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=='POST':
          df=pd.read_csv("maize-production.csv",parse_dates=['Year'])
          df.dtypes
          country=request.POST.get('country')
          
          print(country)
          #country='India'
          production=df[df['Entity']==country]
          production=production.loc[:,['Year','Maize | 00000056 || Production | 005510 || tonnes']]
          production=production.sort_values('Year')
          production.isnull().sum()
          production=production.set_index('Year')
          production.index
          y=production
          p = d = q = range(0, 2)
          pdq = list(itertools.product(p, d, q))
          seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
          print('Examples of parameter combinations for Seasonal ARIMA...')
          print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
          print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
          print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
          print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

          min=99999999
          p1=[-1,-1,-1]
          p2=[-1,-1,-1,-1]
          for param in pdq:
               for param_seasonal in seasonal_pdq:
                    try:
                         mod = sm.tsa.statespace.SARIMAX(y,
                                                       order=param,
                                                       seasonal_order=param_seasonal,
                                                       enforce_stationarity=False,
                                                       enforce_invertibility=False)
                         results = mod.fit()
                         if results.aic<min:
                              min=results.aic
                              p1=param
                              p2=param_seasonal
                         print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
                    except:
                         continue
          print(p1)
          print(min)
          print(p2)
          # 12 is the interval for 12 months
          mod = sm.tsa.statespace.SARIMAX(y,
                                        order=(p1[0], p1[1], p1[2]),
                                        seasonal_order=(p2[0], p2[1], p2[2], 12),
                                        enforce_stationarity=False,
                                        enforce_invertibility=False)
          results = mod.fit()
          print(results.summary().tables[1])
          steps = int(request.POST.get('steps'))
          
          print("steps are",steps)
          pred_uc = results.get_forecast(steps=steps)
               # Create traces
          fig = go.Figure()
          fig.add_trace(go.Scatter(x=y.index, y=y['Maize | 00000056 || Production | 005510 || tonnes'],
                              mode='lines',
                              name='Actual Value',line=dict(width=3)))
          type(pred_uc.predicted_mean)
          fig.add_trace(go.Scatter(x=pred_uc.predicted_mean.index, y=pred_uc.predicted_mean,
                              mode='lines',
                              name='Predicted Value'))
          #fig.show()
          fig.update_layout(
          title="Maize Production of "+country,
          xaxis_title="Year",
          yaxis_title="Production",
          legend_title="Country",
          plot_bgcolor= "lightsteelblue",
          height=600,
          width=1200,
          paper_bgcolor="lightsteelblue",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=True, showline=True,gridcolor="Lightgray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="Lightgray", showline=True, linecolor="black"))
          graph=fig.to_html()
          return render(request,'arima_result.html',{'graph':graph})

     
     else:
          data=pd.read_csv("maize-production.csv")
          column=data["Entity"].drop_duplicates().tolist()
          user=register.objects.get(email=request.session['email'])     

          return render(request,'maize_prediction.html',{"data":column,"user":user})
     

def predict_fruit(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=='POST':
          fruit=request.POST.get('fruit')
          
          if fruit == 'Banana':
               address="banana-production.csv"
          elif  fruit == 'Orange':
               address="orange-production.csv"
          elif  fruit == 'Apple':
               address="apple-production.csv"
          elif  fruit == 'Avocado':
               address="avocado-production.csv"
               
          
          
          df=pd.read_csv(address,parse_dates=['Year'])
          df.dtypes
          country=request.POST.get('country')
          
          print(country)
          #country='India'
          production=df[df['Entity']==country]
          production=production.loc[:,['Year','Production']]
          production=production.sort_values('Year')
          production.isnull().sum()
          production=production.set_index('Year')
          production.index
          y=production
          p = d = q = range(0, 2)
          pdq = list(itertools.product(p, d, q))
          seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
          print('Examples of parameter combinations for Seasonal ARIMA...')
          print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
          print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
          print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
          print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

          min=99999999
          p1=[-1,-1,-1]
          p2=[-1,-1,-1,-1]
          for param in pdq:
               for param_seasonal in seasonal_pdq:
                    try:
                         mod = sm.tsa.statespace.SARIMAX(y,
                                                       order=param,
                                                       seasonal_order=param_seasonal,
                                                       enforce_stationarity=False,
                                                       enforce_invertibility=False)
                         results = mod.fit()
                         if results.aic<min:
                              min=results.aic
                              p1=param
                              p2=param_seasonal
                         print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
                    except:
                         continue
          print(p1)
          print(min)
          print(p2)
          # 12 is the interval for 12 months
          mod = sm.tsa.statespace.SARIMAX(y,
                                        order=(p1[0], p1[1], p1[2]),
                                        seasonal_order=(p2[0], p2[1], p2[2], 12),
                                        enforce_stationarity=False,
                                        enforce_invertibility=False)
          results = mod.fit()
          print(results.summary().tables[1])
          steps = int(request.POST.get('steps'))
          
          print("steps are",steps)
          pred_uc = results.get_forecast(steps=steps)
               # Create traces
          fig = go.Figure()
          fig.add_trace(go.Scatter(x=y.index, y=y['Production'],
                              mode='lines',
                              name='Actual Value'))
          type(pred_uc.predicted_mean)
          fig.add_trace(go.Scatter(x=pred_uc.predicted_mean.index, y=pred_uc.predicted_mean,
                              mode='lines',
                              name='Predicted Value'))
          #fig.show()
          fig.update_layout(
          title= fruit+ " Production of "+country,
          xaxis_title="Year",
          yaxis_title="Production",
          legend_title="Country",
          font=dict(
               family="Courier New, monospace",
               size=14,
               color="RebeccaPurple"))
          graph=fig.to_html()
          return render(request,'arima_result.html',{'graph':graph})

     
     else:
          return render(request,'fruit_prediction.html')
     
      
     
     
def predict_population(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=='POST':
          df=pd.read_csv("share_of_the_.population_in_agriculture.csv",parse_dates=['Year'])
          df.dtypes
          country=request.POST.get('country')
          
          print(country)
          #country='India'
          production=df[df['Entity']==country]
          production=production.loc[:,['Year','share_employed_agri']]
          production=production.sort_values('Year')
          production.isnull().sum()
          production=production.set_index('Year')
          production.index
          y=production
          p = d = q = range(0, 2)
          pdq = list(itertools.product(p, d, q))
          seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
          print('Examples of parameter combinations for Seasonal ARIMA...')
          print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
          print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
          print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
          print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

          min=99999999
          p1=[-1,-1,-1]
          p2=[-1,-1,-1,-1]
          for param in pdq:
               for param_seasonal in seasonal_pdq:
                    try:
                         mod = sm.tsa.statespace.SARIMAX(y,
                                                       order=param,
                                                       seasonal_order=param_seasonal,
                                                       enforce_stationarity=False,
                                                       enforce_invertibility=False)
                         results = mod.fit()
                         if results.aic<min:
                              min=results.aic
                              p1=param
                              p2=param_seasonal
                         print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
                    except:
                         continue
          print(p1)
          print(min)
          print(p2)
          # 12 is the interval for 12 months
          mod = sm.tsa.statespace.SARIMAX(y,
                                        order=(p1[0], p1[1], p1[2]),
                                        seasonal_order=(p2[0], p2[1], p2[2], 12),
                                        enforce_stationarity=False,
                                        enforce_invertibility=False)
          results = mod.fit()
          print(results.summary().tables[1])
          steps = int(request.POST.get('steps'))
          
          print("steps are",steps)
          pred_uc = results.get_forecast(steps=steps)
               # Create traces
          fig = go.Figure()
          fig.add_trace(go.Scatter(x=y.index, y=y['share_employed_agri'],
                              mode='lines',
                              name='Actual Value',fill='tozeroy',line=dict(width=5, color='rgb(0, 128, 128)') ))
          type(pred_uc.predicted_mean)
          pred_uc_year = pred_uc.predicted_mean.index.year

          fig.add_trace(go.Scatter(x=pred_uc_year, y=pred_uc.predicted_mean,
                              mode='lines',line=dict(width=5, color='rgb(53, 94, 59)'),
                              name='Predicted Value',fill='tozeroy'))
          #fig.show()
          fig.update_layout(
          title=f"Agriculturalist trend prediction of {country}",
          xaxis_title="Year",
          yaxis_title="Labor force employed (%)",
          legend_title="Legend",
          plot_bgcolor= "white",
          height=600,
          width=1200,
          #paper_bgcolor="#f8b28b",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=True, showline=True,gridcolor="gray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="gray", showline=True, linecolor="black"))
          graph=fig.to_html()
          return render(request,'arima_result.html',{'graph':graph})

     
     else:
          data=pd.read_csv("share_of_the_.population_in_agriculture.csv")
          column=data["Entity"].drop_duplicates().tolist()
          user=register.objects.get(email=request.session['email'])     

          return render(request,'population_prediction.html',{"data":column,"user":user})
          
def predict_crop_wheat(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=='POST':
          df=pd.read_csv("wheat-production.csv",parse_dates=['Year'])
          df.dtypes
          country=request.POST.get('country')
          
          print(country)
          #country='India'
          
          production=df[df['Entity']==country]
          production=production.loc[:,['Year','Wheat | 00000015 || Production | 005510 || tonnes']]
          production=production.sort_values('Year')
          production.isnull().sum()
          production=production.set_index('Year')
          production.index
          y=production
          p = d = q = range(0, 2)
          pdq = list(itertools.product(p, d, q))
          seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
          print('Examples of parameter combinations for Seasonal ARIMA...')
          print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
          print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
          print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
          print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

          min=99999999
          p1=[-1,-1,-1]
          p2=[-1,-1,-1,-1]
          for param in pdq:
               for param_seasonal in seasonal_pdq:
                    try:
                         mod = sm.tsa.statespace.SARIMAX(y,
                                                       order=param,
                                                       seasonal_order=param_seasonal,
                                                       enforce_stationarity=False,
                                                       enforce_invertibility=False)
                         results = mod.fit()
                         if results.aic<min:
                              min=results.aic
                              p1=param
                              p2=param_seasonal
                         print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
                    except:
                         continue
          print(p1)
          print(min)
          print(p2)
          # 12 is the interval for 12 months
          mod = sm.tsa.statespace.SARIMAX(y,
                                        order=(p1[0], p1[1], p1[2]),
                                        seasonal_order=(p2[0], p2[1], p2[2], 12),
                                        enforce_stationarity=False,
                                        enforce_invertibility=False)
          results = mod.fit()
          print(results.summary().tables[1])
          steps = int(request.POST.get('steps'))
          
          print("steps are",steps)
          pred_uc = results.get_forecast(steps=steps)
               # Create traces
          fig = go.Figure()
          fig.add_trace(go.Scatter(x=y.index, y=y['Wheat | 00000015 || Production | 005510 || tonnes'],
                              mode='lines',
                              name='Actual Value',line=dict(color="#DEB3F5",width=3)))
          type(pred_uc.predicted_mean)
          fig.add_trace(go.Scatter(x=pred_uc.predicted_mean.index, y=pred_uc.predicted_mean,
                              mode='lines',
                              name='Predicted Value',line=dict(color="#370F4D",width=3)))
          #fig.show()
          fig.update_layout(
          title="Wheat Production (in tonnes) of "+country,
          xaxis_title="Year",
          yaxis_title="Production (in tonnes)",
          legend_title="Country",
          plot_bgcolor= "#F5DEB3",
          height=600,
          width=1200,
          paper_bgcolor="#F5DEB3",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5,
          xaxis_title_font_size=25,yaxis_title_font_size=25, xaxis = dict(showgrid=True, showline=True,gridcolor="gray", linecolor="black"),
          yaxis=dict(showgrid=True, gridcolor="gray", showline=True, linecolor="black"))
          graph=fig.to_html()
          return render(request,'arima_result.html',{'graph':graph})

     
     else:
          data=pd.read_csv("wheat-production.csv")
          column=data["Entity"].drop_duplicates().tolist()
          user=register.objects.get(email=request.session['email'])     

          return render(request,'wheat_production.html',{"data":column,"user":user})
     

def fertilizer_detection(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     if request.method=='POST':
          df=pd.read_csv("fertilizers.csv",parse_dates=['Year'])
          df.dtypes
          country=request.POST.get('country')
          
          print(country)
          #country='India'
          production=df[df['Entity']==country]
          production=production.loc[:,['Year','Nutrient nitrogen N (total) | 00003102 || Use per area of cropland | 005159 || kilograms per hectare']]
          production=production.sort_values('Year')
          production.isnull().sum()
          production=production.set_index('Year')
          production.index
          y=production
          p = d = q = range(0, 2)
          pdq = list(itertools.product(p, d, q))
          seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
          print('Examples of parameter combinations for Seasonal ARIMA...')
          print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
          print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
          print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
          print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

          min=99999999
          p1=[-1,-1,-1]
          p2=[-1,-1,-1,-1]
          for param in pdq:
               for param_seasonal in seasonal_pdq:
                    try:
                         mod = sm.tsa.statespace.SARIMAX(y,
                                                       order=param,
                                                       seasonal_order=param_seasonal,
                                                       enforce_stationarity=False,
                                                       enforce_invertibility=False)
                         results = mod.fit()
                         if results.aic<min:
                              min=results.aic
                              p1=param
                              p2=param_seasonal
                         print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
                    except:
                         continue
          print(p1)
          print(min)
          print(p2)
          # 12 is the interval for 12 months
          mod = sm.tsa.statespace.SARIMAX(y,
                                        order=(p1[0], p1[1], p1[2]),
                                        seasonal_order=(p2[0], p2[1], p2[2], 12),
                                        enforce_stationarity=False,
                                        enforce_invertibility=False)
          results = mod.fit()
          print(results.summary().tables[1])
          steps = int(request.POST.get('steps'))
          
          print("steps are",steps)
          pred_uc = results.get_forecast(steps=steps)
               # Create traces
          fig = go.Figure()
          fig.add_trace(go.Scatter(x=y.index, y=y['Nutrient nitrogen N (total) | 00003102 || Use per area of cropland | 005159 || kilograms per hectare'],
                              mode='lines',
                              name='Actual Value'))
          type(pred_uc.predicted_mean)
          fig.add_trace(go.Scatter(x=pred_uc.predicted_mean.index, y=pred_uc.predicted_mean,
                              mode='lines',
                              name='Predicted Value'))
          #fig.show()
          fig.update_layout(
          xaxis_title="Year",
          yaxis_title="Use",
          legend_title="Country",
          title=f"Nutrient Nitrogen(N) Use Kilogram per Hectare prediction of {country}", plot_bgcolor= "lightsteelblue",
          height=600,
          width=1200,
          paper_bgcolor="lightsteelblue",
          title_font_size=25,
          font=dict(family="Verdana",size=18,color="black"), title_x=0.5)
          graph=fig.to_html()
          return render(request,'arima_result.html',{'graph':graph})

     
     else:
          data=pd.read_csv("fertilizers.csv")
          word_to_exclude = '(FAO)'
          data = data[~data['Entity'].str.contains(word_to_exclude)]
          column=data["Entity"].drop_duplicates().tolist()
          
          column=data["Entity"].drop_duplicates().tolist()
          user=register.objects.get(email=request.session['email'])     

          return render(request,'fertilizer_prediction.html',{"data":column,"user":user})
     
def disease_detection(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     
     if request.method=='POST':
    

          # Load the model from HDF5 file
          model = load_model("save1.h5")  # Replace this with the path to your model

          f = request.FILES['file1'] # here you get the files needed
          handle_uploaded_file(f,'STATIC/'+f.name)
          # Load the image you want to classify
          image_path = 'STATIC/'+f.name  # Replace this with the path to your image
          print('image_path',image_path)
          img = image.load_img(image_path, target_size=(256, 256))

          # Preprocess the image
          img_array = image.img_to_array(img)
          img_array = np.expand_dims(img_array, axis=0)
          img_array /= 255.  # Rescale to [0, 1] as done during training

          # Make predictions
          predictions = model.predict(img_array)
          classes=['Apple_Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']

          # Get the predicted class
          predicted_class_index = np.argmax(predictions)
          predicted_class = classes[predicted_class_index]
      

          print("Predicted class:", predicted_class)
      
          
          if predicted_class == 'Apple_Apple_scab':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Apple___Black_rot':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Apple___Cedar_apple_rust':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Apple___healthy':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Blueberry___healthy':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Cherry_(including_sour)___Powdery_mildew':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Cherry_(including_sour)___healthy':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Corn_(maize)___Common_rust_':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Corn_(maize)___Northern_Leaf_Blight':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Corn_(maize)___healthy':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Grape___Black_rot':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Grape___Esca_(Black_Measles)':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Grape___healthy':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Orange___Haunglongbing_(Citrus_greening)':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Peach___Bacterial_spot':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Peach___healthy':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Pepper,_bell___Bacterial_spot':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Pepper,_bell___healthy':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Potato___Early_blight':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Potato___Late_blight':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Potato___healthy':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Raspberry___healthy':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Soybean___healthy':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Squash___Powdery_mildew':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Strawberry___Leaf_scorch':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Strawberry___healthy':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Tomato___Bacterial_spot':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Tomato___Early_blight':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Tomato___Late_blight':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Tomato___Leaf_Mold':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Tomato___Septoria_leaf_spot':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Tomato___Spider_mites Two-spotted_spider_mite':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Tomato___Target_Spot':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Tomato___Tomato_Yellow_Leaf_Curl_Virus':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Tomato___Tomato_mosaic_virus':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Tomato___healthy':
               o=disease_solution.objects.filter(description=predicted_class)
          else:
               o="No Disease Detection"
          
          

          return render(request,'detection_result.html',{'data':o})
          
     else:
          user=register.objects.get(email=request.session['email'])     
          
          return render(request,'disease_detection.html',{'user':user})
     
# def detection_result(request):
#      return render(request,'detection_result.html')
     
     
def change_password(request):
     if request.method=='POST':
          o=request.POST.get('op')
          n=request.POST.get('np')
          c=request.POST.get('cp')
          
          if n==c:
               user=register.objects.get(email=request.session['email'])
               p=user.password
               
               if p==o:
                    user.password=n
                    user.save()
                    msg='Password successfully changed'
                    user=register.objects.get(email=request.session['email'])     
                    return render(request,'change_password.html',{'msg':1,'user':user})
               else:
                    msg='old password not correct'
                    user=register.objects.get(email=request.session['email'])     
                    return render(request,'change_password.html',{'msg':2,'user':user})
          else:
               msg='New pass and confirm pass not match'
               user=register.objects.get(email=request.session['email'])     
               return render(request,'change_password.html',{'msg':3,'user':user})
     else:
          user=register.objects.get(email=request.session['email'])     
          return render(request,'change_password.html',{'user':user})
               

def edit_profile_s(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     user=register.objects.get(email=request.session['email'])
     if request.method=='POST':
          user.name=request.POST.get("nm")
          user.email=request.POST.get("em")
          user.contact=request.POST.get("ph")
          user.address=request.POST.get("ad")
          user.gender=request.POST.get("gn")
          user.age=request.POST.get("ag")
          user.save()
          
          
          return redirect('/userprofile_s')
     else:
          return render (request,'edit_profile_s.html',{'user':user})
          

def forget(request):
     if (request.method == 'POST'):
          em=request.POST.get('email')
          user=register.objects.filter(email=em)
          if(len(user)>0):
               password=user[0].password
               subject="Password"
               message="Hi your password is '"+ password +"'"
               email_from=settings.EMAIL_HOST_USER
               recipient_list=[em]  
               send_mail(subject,message,email_from,recipient_list)
               return render(request,'login.html',{'message':2})
          else:
               return render(request,'forget.html',{'msg':2}) 
     else:
          return render(request,"forget.html")   


def logout(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     del request.session['email']
     return redirect('/login')

def live(request):
     import datetime
     from datetime import date
     from newsapi import NewsApiClient
     newsapi = NewsApiClient(api_key='b5bebd12136d4ecf8878f2060de6d277')

     json_data = newsapi.get_everything(q='Agriculture',language= 'en',from_param=str(date. today() - datetime. timedelta(days=29)),to=str (date.today()),page_size=21,page = 1,sort_by='relevancy')
     k=json_data['articles']
     return render (request,'live_news.html',{'k':k})
     

def dashboard(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     user=register.objects.get(email=request.session['email'])
     return render(request,'dashboard.html',{'user':user})


def sentence_similarity(sentence1, sentence2):
    # Process the sentences using spaCy
    #nlp = spacy.load('en_core_web_md')

    doc1 = nlp(sentence1)
    doc2 = nlp(sentence2)
   
    # Compute the similarity between the two sentences
    similarity_score = doc1.similarity(doc2)
   
    return similarity_score
def get_bot_response1(user_message):
     import google.generativeai as genai
     genai.configure(api_key="AIzaSyC619wTw72mLADW0vbxzrUdjApVWLiydKc")
     # Set up the model
     generation_config = {
     "temperature": 0.9,
     "top_p": 1,
     "top_k": 1,
     "max_output_tokens": 2048,
     }

     safety_settings = [
     {
     "category": "HARM_CATEGORY_HARASSMENT",
     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
     },
     {
     "category": "HARM_CATEGORY_HATE_SPEECH",
     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
     },
     {
     "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
     },
     {
     "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
     },
     ]

     model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)
     
     # user_prompt = "\nUser

     convo = model.start_chat()
     convo.send_message(user_message)
     answer=convo.last.text
     return answer

    # If no matching question is found, use a default response
    # return "I'm sorry, I don't understand that question."
def chat(request):
     if request.method == 'POST':
        # Parse the JSON content from the request body
        data = json.loads(request.body.decode('utf-8'))
       
        # Access the 'user_input' key from the JSON data
        user_message = data.get('message', '')
       
        # Now you can use user_message in your logic
        print("User Message:", user_message)
       
        #Get bot response based on user input
        bot_response = get_bot_response1(user_message)

        # Save user message to the database
        ChatMessage.objects.create(user='User', message=user_message)
        # Save bot response to the database
        ChatMessage.objects.create(user='Bot', message=bot_response)
        #bot_response=""
        return JsonResponse({'response': bot_response})
   
     messages = ChatMessage.objects.all()
     user=register.objects.get(email=request.session['email'])
     
     return render(request, 'chat.html', {'messages': messages,'user':user})



def chat1(request):
     if request.method == 'POST':
          import google.generativeai as genai

          genai.configure(api_key="AIzaSyCRQbHHFaxgY0OgqXX_6t8OTZyk_8TGO6I")

          # Set up the model
          generation_config = {
          "temperature": 0.9,
          "top_p": 1,
          "top_k": 1,
          "max_output_tokens": 2048,
          }

          safety_settings = [
          {
          "category": "HARM_CATEGORY_HARASSMENT",
          "threshold": "BLOCK_MEDIUM_AND_ABOVE"
          },
          {
          "category": "HARM_CATEGORY_HATE_SPEECH",
          "threshold": "BLOCK_MEDIUM_AND_ABOVE"
          },
          {
          "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
          "threshold": "BLOCK_MEDIUM_AND_ABOVE"
          },
          {
          "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
          "threshold": "BLOCK_MEDIUM_AND_ABOVE"
          },
          ]

          model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                        generation_config=generation_config,
                                        safety_settings=safety_settings)

          convo = model.start_chat(history=[
          {
          "role": "user",
          "parts": ["hi"]
          },
          {
          "role": "model",
          "parts": ["Hello! 👋 How can I help you today?"]
          },
          {
          "role": "user",
          "parts": ["hi"]
          },
          {
          "role": "model",
          "parts": ["Hey there! 👋 Is there anything I can assist you with today?"]
          },
          {
          "role": "user",
          "parts": ["yes"]
          },
          {
          "role": "model",
          "parts": ["Great! 😊 How can I help you?"]
          },
          ])
          msg=request.POST.get("msg")
          x=msg
          convo.send_message(x)
          print(convo.last.text)
          return render(request, 'chat1.html',{"result":convo.last.text})

     else:
          return render(request, 'chat1.html')
     


# add def fuction to the urls
#copy from admin.py the import lines
#then we have to make dictionary for the data in each table in views.py
#and then pass that dict into template file
