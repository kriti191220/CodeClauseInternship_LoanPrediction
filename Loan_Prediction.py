#!/usr/bin/env python
# coding: utf-8

# # Loan Prediction Model

# In[10]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


# In[16]:


df = pd.read_csv(r'C:\Users\1234\OneDrive\Desktop\INTERNSHIPS ETC\CODECLAUSE\PROJECT 1\data\Loan_Data.csv')


# In[15]:


df.head()


# In[17]:


data=df.copy()


# ## Categorical Classification

# In[18]:


data[data["Loan_Status"] == "Y"]["Gender"].value_counts()


# ### Loan Approval Status

# In[19]:


import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
type_ = ["Y", "N"]
fig = make_subplots(rows=1, cols=1)

fig.add_trace(go.Pie(labels=type_, values=data['Loan_Status'].value_counts(), name="Loan_Status"))

# Use of `hole` to create a donut-like pie chart
fig.update_traces(hole=.4, hoverinfo="label+percent+name", textfont_size=16)

fig.update_layout(
    title_text="Loan Approval Status",
    # Add annotations in the center of the donut pies.
    annotations=[dict(text='loan_status', x=0.5, y=0.5, font_size=20, showarrow=False)])
fig.show()


# ### Loan Approval with respect to Gender

# In[21]:


plt.figure(figsize=(6, 6))
labels =["Loan_Status: No","Loan_Status:Yes"]
values = [data.Loan_Status[data.Loan_Status == "Y"].groupby(by = data.Gender).count().Female + data.Loan_Status[data.Loan_Status == "Y"].groupby(by = data.Gender).count().Male,
          data.Loan_Status[data.Loan_Status == "N"].groupby(by = data.Gender).count().Female + data.Loan_Status[data.Loan_Status == "N"].groupby(by = data.Gender).count().Male]
labels_gender = ["F","M","F","M"]
sizes_gender = [data.Loan_Status[data.Loan_Status == "Y"].groupby(by = data.Gender).count().Female,
                data.Loan_Status[data.Loan_Status == "Y"].groupby(by = data.Gender).count().Male,
                data.Loan_Status[data.Loan_Status == "N"].groupby(by = data.Gender).count().Female,
                data.Loan_Status[data.Loan_Status == "N"].groupby(by = data.Gender).count().Male]

colors = ['#66b3ff','#ff6666']
colors_gender = ['#c2c2f0','#ffb3e6', '#c2c2f0','#ffb3e6']
explode = (0.3,0.3) 
explode_gender = (0.1,0.1,0.1,0.1)
textprops = {"fontsize":15}
#Plot
plt.pie(values, labels=labels,autopct='%1.1f%%',pctdistance=1.08, labeldistance=0.8,colors=colors, startangle=90,frame=True, explode=explode,radius=10, textprops =textprops, counterclock = True, )
plt.pie(sizes_gender,labels=labels_gender,colors=colors_gender,startangle=90, explode=explode_gender,radius=7, textprops =textprops, counterclock = True, )
#Draw circle
centre_circle = plt.Circle((0,0),5,color='black', fc='white',linewidth=0)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title('Loan approval w.r.t Gender: Male(M), Female(F)', fontsize=15, y=1.1)

# show plot 
 
plt.axis('equal')
plt.tight_layout()
plt.show()


# ### Loan Approval based on Number of Dependents

# In[23]:


color_map = {"Y": "#00EEEE", "N": "#DC143C"}
fig = px.histogram(data, x="Dependents", color="Loan_Status", barmode="group", title="<b>Loan approval based on Dependents</b>", color_discrete_map=color_map)
fig.update_layout(width=700, height=500, bargap=0.1)
fig.show()


# ### Loan Approval based on Self Employment Status

# In[25]:


color_map = {"Y": "#698B69", "N": "#483D8B"}
fig = px.histogram(data, x="Self_Employed", color="Loan_Status", barmode="group", title="<b>Loan approval based on Self employment status</b>", color_discrete_map=color_map)
fig.update_layout(width=700, height=500, bargap=0.1)
fig.show()


# ### Loan approval based on Education status

# In[27]:


color_map = {"Y": "#698B69", "N": "#483D8B"}
fig = px.histogram(data, x="Loan_Status", color="Education", barmode="group", title="<b>Loan approval based on Education</b>", color_discrete_map=color_map)
fig.update_layout(width=700, height=500, bargap=0.1)
fig.show()


# ### Loan Approval based on Marital Status

# In[29]:


color_map = {"Y": "#FF97FF", "N": "#AB63FA"}
fig = px.histogram(data, x="Married", color="Loan_Status", barmode="group", title="<b>Loan approval based on Marital status</b>", color_discrete_map=color_map)
fig.update_layout(width=700, height=500, bargap=0.1)
fig.show()


# ### Loan Approval based on Property / Collateral 
# 

# In[30]:


color_map = {"Y": "#FF97FF", "N": "#AB63FA"}
fig = px.histogram(data, x="Loan_Status", color="Property_Area", barmode="group", title="<b>Loan approval based on property area</b>", color_discrete_map=color_map)
fig.update_layout(width=700, height=500, bargap=0.1)
fig.show()


# In[ ]:




