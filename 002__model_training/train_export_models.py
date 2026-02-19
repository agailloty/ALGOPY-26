#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pathlib import Path
import os

dataset_folder = Path(".") / "dataset"

if not os.path.exists(dataset_folder):
    import utils
    utils.download_dataset()


# In[2]:


import polars as pl


# In[3]:


data = pl.read_csv("dataset/train.csv")


# In[4]:


data.shape


# In[5]:


data.head()


# In[6]:


data.null_count()


# In[7]:


data.describe()


# In[8]:


data["Occupation"].value_counts()


# In[9]:


data = data.with_columns(
    pl.col("Occupation").fill_null("Unknown")
)


# In[10]:


data["Occupation"].value_counts()


# In[11]:


data = data.drop(["Policy Start Date", "id", "Customer Feedback", "Credit Score"])


# In[12]:


data = data.drop_nulls()


# In[13]:


data.shape


# In[14]:


import polars.selectors as cs


# In[15]:


df = data.to_dummies(cs.string(), separator = "_", drop_first = True)


# In[16]:


df.shape


# In[17]:


y = df["Premium Amount"]
X = df.drop("Premium Amount")


# In[18]:


X.shape


# In[27]:


X.columns


# In[20]:


y.shape


# In[19]:


from sklearn.linear_model import LinearRegression


# In[20]:


lin_reg = LinearRegression()
lin_reg.fit(X, y)


# In[21]:


lin_reg.coef_


# In[22]:


from sklearn.linear_model import ElasticNet
eln_reg = ElasticNet()
eln_reg.fit(X, y)


# In[23]:


eln_reg.coef_


# In[24]:


from sklearn.ensemble import GradientBoostingRegressor
gb_model = GradientBoostingRegressor()
import time
start_time = time.time()
gb_model.fit(X, y)
print("--- %s seconds ---" % (time.time() - start_time))


# In[25]:


from sklearn.ensemble import AdaBoostRegressor

adab_model = AdaBoostRegressor()
import time
start_time = time.time()
adab_model.fit(X, y)
print("--- %s seconds ---" % (time.time() - start_time))


# In[26]:


# Enregistrer les modèles
from pathlib import Path
import os
model_location = Path(".").parent / "models"
if not os.path.exists(model_location):
  os.mkdir(model_location)

import pickle

model_export_names = ["LinearReg_Model.pkl", "ElasticNet_Model.pkl", "GradientB_Model.pkl", "AdaBoost_Model.pkl"]

for model, export_name in zip([lin_reg, eln_reg, gb_model, adab_model], model_export_names):
  with open(model_location / export_name, "wb") as f:
    pickle.dump(model, f)

# Exporter les noms de features en JSON
import json
feature_names = X.columns
with open(model_location / "feature_names.json", "w") as f:
    json.dump(feature_names, f, indent=2)

