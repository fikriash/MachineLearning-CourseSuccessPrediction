from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle
import json
from sqlalchemy import create_engine

## Joblib untuk Load Model
import joblib

# untuk membuat route
app = Flask(__name__)


###############
###  HOME   ###
###############
@app.route('/')
def home():
    return render_template('home.html')

####################
## ABOUT PROJECT  ##
####################
@app.route('/Project')
def index():
    return render_template('index.html')

####################
## VISUALIZATION  ##
####################
@app.route('/visualization')
def visualization():
    return render_template('plot.html')

###############
## UPDATE DB ##
###############
@app.route('/db_fn')
def db_fn():
    sqlengine = create_engine('mysql+pymysql://fikri:fikri1234@127.0.0.1/final_project', pool_recycle=3605)
    engine = sqlengine.raw_connection()
    cursor = engine.cursor()
    cursor.execute("SELECT * FROM udemy")
    data = cursor.fetchall()
    return render_template('update.html', data=data)

@app.route('/update_fn', methods=['POST', 'GET'])
def update_fn():

    if request.method == 'POST':
        input = request.form
        
        icourse_id = int(input['ucourse_id'])
        iprice=float(input['uprice'])
        inum_subscribers = int(input['unum_subscribers'])
        inum_reviews = int(input['unum_reviews'])
        inum_lectures=int(input['unum_lectures'])
        icontent_duration=float(input['ucontent_duration'])
        iyear_p=int(input['uyear_p'])
        imonth_p= int(input['umonth_p'])
        idate_p=int(input['udate_p'])

        ilevel = input['ulevel']
        
        if input['uis_paid'] == "True":
            iis_paid = True
        else:
            iis_paid = False
        
        isubject = input['usubject']
        
        if input['uis_success'] == '1':
            iis_success = 1
        else:
            iis_success = 0

        ## Memasukkan data ke Tabel SQL
        new_df = pd.DataFrame({
            'course_id' : [icourse_id],
            'is_paid' : [iis_paid],
            'price' : [iprice],
            'num_subscribers' : [inum_subscribers],
            'num_reviews' : [inum_reviews],
            'num_lectures' : [inum_lectures],
            'level' : [ilevel],
            'content_duration' : [icontent_duration],
            'subject' : [isubject],
            'year_p': [iyear_p],
            'month_p' : [imonth_p],
            'date_p' : [idate_p],
            'is_success': [iis_success]
        })
        new_df.to_sql('udemy', con=dbConnection, if_exists='append', index=False)
        return render_template('success.html',
            course_id= icourse_id,
            is_paid= iis_paid,
            price= iprice,
            num_subscribers= inum_subscribers,
            num_reviews= inum_reviews,
            num_lectures= inum_lectures,
            level= ilevel,
            content_duration= icontent_duration,
            subject= isubject,
            year_p= iyear_p,
            month_p= imonth_p,
            date_p= idate_p,
            is_success= iis_success
            )

################
## PREDICT DB ##
################
@app.route('/pred_lr')
def pred_lr():
    sqlengine = create_engine('mysql+pymysql://fikri:fikri1234@127.0.0.1/final_project', pool_recycle=3605)
    engine = sqlengine.raw_connection()
    cursor = engine.cursor()
    cursor.execute("SELECT * FROM udemy")
    data = cursor.fetchall()
    return render_template('predict.html', data=data)

@app.route('/pred_result', methods=['POST', 'GET'])
def pred_result():

    if request.method == 'POST':
    ## Untuk Predict
        input = request.form
        
        course_id = int(input['course_id'])
        price=float(input['price'])
        num_lectures=int(input['num_lectures'])
        content_duration=float(input['content_duration'])
        year_p=int(input['year_p'])
        month_p = int(input['month_p'])
        date_p=int(input['date_p'])

        level_enc = ''
        if input['level'] == "0":
            level_enc = 0
        elif input['level'] == "1":
            level_enc = 1
        elif input['level'] == "2":
            level_enc = 2
        else:
            level_enc = 3
        
        is_paid_False = ''
        if price == 0:
            if input['is_paid'] == 'no':
                is_paid_False = 1
            elif input['is_paid'] == 'yes':
                is_paid_False = 0
        else:
            is_paid_False = 1
            
        is_paid_True = ''
        if price != 0:
            if input['is_paid'] == 'no':
                is_paid_True = 0
            elif input['is_paid'] == 'yes':
                is_paid_True = 1
        else:
            is_paid_True = 0
        
        business_subject = ''
        if input['subject'] == 'business':
            business_subject = 1
        else:
            business_subject = 0
        
        graphic_subject = ''
        if input['subject'] == 'graphic':
            graphic_subject = 1
        else:
            graphic_subject = 0
        
        music_subject = ''
        if input['subject'] == 'music':
            music_subject = 1
        else:
            music_subject = 0
        
        webdev_subject = ''
        if input['subject'] == 'web':
            webdev_subject = 1
        else:
            webdev_subject = 0

        sample = pd.DataFrame(
            columns=[course_id],
            index=[
                'price', 'num_lectures', 'content_duration', 'year_p', 'month_p',
                'date_p', 'level_enc', 'is_paid_False', 'is_paid_True',
                'business_subject', 'graphic_subject', 'music_subject',
                'webdev_subject'
            ],
            data = [price,num_lectures,content_duration,year_p,month_p,date_p,level_enc,is_paid_False,is_paid_True,business_subject,graphic_subject,music_subject,webdev_subject]
        ).T
        pred = model.predict_proba(sample)
        hasil_pred = round(pred[0][1], 3)

        ## Untuk Isi Data
        course_id2 = int(input['course_id'])
        price2=float(input['price'])
        num_lectures2=int(input['num_lectures'])
        content_duration2=float(input['content_duration'])
        year_p2=int(input['year_p'])
        month_p2= int(input['month_p'])
        date_p2 = int(input['date_p'])

        level_enc2 = ''
        if input['level'] == "0":
            level_enc2 = 'All Levels'
        elif input['level'] == "1":
            level_enc2 = 'Beginner Level'
        elif input['level'] == "2":
            level_enc2 = "Intermediate Level"
        else:
            level_enc2 = 'Expert Level'

        subject2 = ''
        if input['subject'] == "web":
            subject2 = 'Web Development'
        elif input['subject'] == "graphic":
            subject2 = 'Graphic Design'
        elif input['subject'] == "music":
            subject2 = "Musical Instrument"
        else:
            subject2 = 'Business Finance'

        is_paid2 = ''
        if input['is_paid'] == 'yes':
            is_paid2 = True
        else:
            is_paid2 = False

        return render_template('result.html',
            course_id=course_id2,
            price=price2,
            num_lectures=num_lectures2,
            content_duration=content_duration2,
            level=level_enc2,
            year_p=year_p2,
            month_p=month_p2,
            date_p=date_p2,
            is_paid=is_paid2,
            subject=subject2,
            pred_result = f"{round((hasil_pred*100),2)} % Success"
            )

################
## LOAD MODEL ##
################
if __name__ == '__main__':
    ## Me-Load data dari Database
    sqlengine = create_engine('mysql+pymysql://fikri:fikri1234@127.0.0.1/final_project', pool_recycle=3605)
    dbConnection = sqlengine.connect()
    engine = sqlengine.raw_connection()
    cursor = engine.cursor()
    udemy = pd.read_sql("select * from udemy", dbConnection)
    ## Load Model
    # with open ('xgbus.json', 'rb') as model:
    #     mod = pickle.load(model)
    model = joblib.load('xgbase')
    app.run(debug=True)