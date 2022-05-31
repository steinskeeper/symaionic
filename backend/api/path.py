import imp
from this import s
from fastapi import APIRouter
from fastapi import Request, FastAPI
import pymongo
from bson import json_util, ObjectId
import os
from dotenv import load_dotenv
import json
import bcrypt
import nltk
import tensorflow as tf
import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from tensorflow.keras.layers import Input, Conv2D, Dense, Flatten, Dropout
from tensorflow.keras.layers import GlobalMaxPooling2D, MaxPooling2D
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.models import Model
from tensorflow.keras.models import load_model
from sklearn.feature_extraction.text import TfidfVectorizer
path = APIRouter()

load_dotenv()
mongourl = "mongodb://localhost:27017"


myclient = pymongo.MongoClient(
    mongourl,)
db = myclient["sym"]
col = db["flow"]
col1 = db["user"]


@path.post("/createflow")
async def creat(request: Request):
    re = (await request.json())
    x = col.insert_one(re)

    return {"id": str(x.inserted_id)}


@path.get("/getflow/{id}")
async def oneflow(request: Request, id: str):
    re = col.find_one({"_id": ObjectId(id)})
    return re


@path.get("/getflows")
async def allflows(request: Request):
    re = col.find()
    return re


@path.post("/signup")
async def signup(request: Request):
    re = (await request.json())
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(re["password"].encode('utf-8'), salt)
    re["password"] = hashed

    x = col1.insert_one(re)

    return {"id": str(x.inserted_id)}


@path.post("/signin")
async def signin(request: Request):
    re = await request.json()
    print(re)
    user = col1.find_one({"email": re["email"]})
    if re is None:
        return {"message": "Email not found"}
    if bcrypt.checkpw(re["password"].encode('utf-8'), user["password"]):
        return {"status": "success"}
    else:
        return {"message": "Wrong password"}


@path.post("/getresult")
async def getresult(request: Request):
    re = await request.json()
    print(re)
    model = load_model(
        '/home/dp/Music/mini/symaionic/symaionic-backend/api/feedback_clfr.h5')
    print(model.summary())
    test = ["Hello"]
    test = pd.DataFrame(test, columns=['text'])
   
    
    stop = stopwords.words('english')
    text = []
    none = test['text'].map(lambda x: text.append(' '.join
                                                  ([word for word in str(x).strip().split() if not word in set(stop)])))
    
   
    tfid=TfidfVectorizer(strip_accents=None,lowercase=False,preprocessor=None)
    x_features_test=tfid.fit_transform(text).toarray()
    x_features_test = tfid.transform(text).toarray()
    x_features_test = pd.DataFrame(x_features_test)
    results = model.predict(x_features_test)
    results = np.argmax(results, axis=1)
    results = pd.DataFrame(results, columns=['Category'])
    int_category = {0: 'Bug', 1: 'comments',
                    2: 'complaints', 3: 'meaningless', 4: 'requests'}
    results['Category'] = results['Category'].apply(lambda x: int_category[x])
    results['text'] = test['text']
    print(results)


# @notmule.post("/previous-orders")
# async def prevv(request: Request):
#     re = (await request.json())
#     print(re)
#     orders = []
#     dat = db.orders.find({"buyerid": re["userid"]})
#     dat_san = json.loads(json_util.dumps(dat))

#     for x in dat_san:
#         orders.append(x)

#     for user in orders:

#         buy = db.users.find_one({"_id": ObjectId(user["buyerid"])}, {'_id': 0})
#         user["sellerName"] = buy["username"]

#     for item in orders:
#         listing = db.users.find_one({"_id": ObjectId(
#             item["sellerid"]), "listings.id": item["listingid"]}, {"listings.$": 1, '_id': 0})
#         item["title"] = listing["listings"][0]["oname"]
#         item["price"] = listing["listings"][0]["oprice"]
#         item["imgURL"] = listing["listings"][0]["opic"]

#     return orders


# @notmule.post("/orderstat")
# async def stat(request: Request):
#     re = (await request.json())
#     print(re)
#     db.orders.update_one({"_id": ObjectId(re["orderid"])}, {
#                          "$set": {"status": re["status"]}})

#     return {"message": "success"}

# @notmule.post("/teams")
# async def teams(request: Request):
#     re = (await request.json())
#     print(re)
#     teams = []
#     dat = db.users.find({"skill": (re["skill"])})
#     dat_san = json.loads(json_util.dumps(dat))

#     for x in dat_san:
#         del x["password"]
#         teams.append(x)


#     return teams
