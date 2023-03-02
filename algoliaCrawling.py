from flask import Flask, render_template, request
app = Flask("SuperScrapper")
import requests

import os
os.system("clear")

base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new_url = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popular_url = f"{base_url}/search?tags=story"

data_bage_new = []
in_new = []
data_bage_popular = []
in_popular = []
data_bage_com = []

# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
def popular_data_get():
  popular = requests.get(popular_url)
  popular_dic = popular.json()
  for i in popular_dic['hits']:
    if i['num_comments'] != 0 and i['title'] != None:
      if i['objectID'] not in in_popular:
        in_popular.append(i['objectID'])
        data_bage_popular.append(i)
  return data_bage_popular

def new_data_get():
  new = requests.get(new_url)
  popular_dic = new.json()
  for i in popular_dic['hits']:
    if i['title'] != None:
      if i['objectID'] not in in_new:
        in_new.append(i['objectID'])
        data_bage_new.append(i)
  return data_bage_new

@app.route("/")
def home():
  order_by = request.args.get('order_by')
  print(order_by)
  if order_by == "new":
    if data_bage_new:
      data_bage = data_bage_new
    else:
      data_bage = new_data_get()
    return render_template("detail.html",data=data_bage,order = order_by)
  elif order_by == "popular":
    if data_bage_popular:
      data_bage = data_bage_popular
    else:
      data_bage = popular_data_get()
    return render_template("detail.html", data=data_bage,order = order_by)
  else:
    if data_bage_popular:
      data_bage = data_bage_popular
    else:
      data_bage = popular_data_get()
    return render_template("detail.html", data=data_bage,order = order_by)
  
@app.route("/<number>")
def comment(number):
  com = requests.get(f"{base_url}/items/{number}")
  com_dic = com.json()
  return render_template("index.html",data = com_dic)

def start_over():
  app.run(host="0.0.0.0")

start_over()  


  

        #return f"{base_url}/items/{id}"

db = {}
app = Flask("DayNine")


# app.run(host="0.0.0.0")