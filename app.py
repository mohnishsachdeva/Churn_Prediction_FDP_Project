import numpy as np
# from flask import Flask, request, jsonify, render_template
import pickle
import streamlit as st

# app = Flask(__name__)
model = pickle.load(open('logisticregression.pkl','rb')) 

# @app.route('/')
# def home():
  
#     return render_template("index.html")
  
# @app.route('/predict',methods=['GET'])
def predict(tenure,login_device,city_tier,warehouse_to_home,preferred_payment_mode,gender,hour_spend_on_app,number_of_device_registered,prefered_order_cat,
satisfaction_score,marital_status,number_of_address,complain,order_amount_hike_from_last_year,coupon_used,order_count,
day_since_last_order,cash_back_amount):
    

    def prefered_order_cat_code(prefered_order_cat):
        switcher = {
            "Laptop & Accessory": [1,0,0,0,0,0],
            "Mobile Phone":[0,0,1,0,0,0],
            "Fashion":[0,0,0,0,1,0],
            "Mobile":[0,1,0,0,0,0], 
            "Grocery":[0,0,0,0,0,1],
            "Others":[0,0,0,1,0,0]
        }
        return switcher.get(prefered_order_cat, "nothing")

    prefered_order_category = prefered_order_cat_code(prefered_order_cat)
    
    if gender == 'Female':
       gender_code = 0
    else:
        gender_code = 1


    if complain == 'Yes':
       complain_code = 1
    else:
        complain_code = 0


    if marital_status == 'Single':
       marital_status_code = [1,0,0]
    elif marital_status == 'Married':
        marital_status_code = [0,0,1]
    else:
        marital_status_code = [0,1,0]


    if login_device == 'Mobile Phone':
       login_device_code = [1,0,0]
    elif login_device == 'Computer':
        login_device_code = [0,0,1]
    else:
        login_device_code = [0,1,0]


    if preferred_payment_mode == 'Debit Card':
       preferred_payment_mode_code = [1,0,0,0,0,0,0]
    elif preferred_payment_mode == 'Credit Card':
        preferred_payment_mode_code = [0,0,0,0,0,0,1]
    elif preferred_payment_mode == 'E wallet':
        preferred_payment_mode_code = [0,0,0,0,1,0,0]
    elif preferred_payment_mode == 'UPI':
        preferred_payment_mode_code = [0,1,0,0,0,0,0]
    elif preferred_payment_mode == 'COD':
        preferred_payment_mode_code = [0,0,0,0,0,1,0]
    elif preferred_payment_mode == 'CC':
        preferred_payment_mode_code = [0,0,1,0,0,0,0]
    else:
        preferred_payment_mode_code = [0,0,0,1,0,0,0] # cash on deleivery
    # '''
    # For rendering results on HTML GUI
    # '''
    # exp = float(request.args.get('exp'))
    
    prediction = int(model.predict([[float(tenure),float(login_device_code[0]),
                                    float(login_device_code[2]),
                                    float(login_device_code[1]),
                                    float(city_tier),
                                    float(warehouse_to_home),
                                    float(preferred_payment_mode_code[0]),
                                    float(preferred_payment_mode_code[1]),
                                    float(preferred_payment_mode_code[2]),
                                    float(preferred_payment_mode_code[3]),
                                    float(preferred_payment_mode_code[4]),
                                    float(preferred_payment_mode_code[5]),
                                    float(preferred_payment_mode_code[6]),
                                    float(gender_code),
                                    float(hour_spend_on_app),
                                    float(number_of_device_registered),
                                    float(prefered_order_category[0]),
                                    float(prefered_order_category[1]),
                                    float(prefered_order_category[2]),
                                    float(prefered_order_category[3]),
                                    float(prefered_order_category[4]),
                                    float(prefered_order_category[5]),
                                    float(satisfaction_score),
                                    float(marital_status_code[0]),
                                    float(marital_status_code[1]),
                                    float(marital_status_code[2]),
                                    float(number_of_address),
                                    float(complain_code),
                                    float(order_amount_hike_from_last_year),
                                    float(coupon_used),
                                    float(order_count),
                                    float(day_since_last_order),
                                    float(cash_back_amount)]]))
    
        
    # return render_template('index.html', prediction_text='Regression Model  has predicted salary for given experinace is Rs.  : {}'.format(prediction))
    # return tenure,login_device,city_tier,warehouse_to_home,preferred_payment_mode,gender,hour_spend_on_app,prefered_order_cat,satisfaction_score,marital_status,number_of_address,complain,order_amount_hike_from_last_year,coupon_used,order_count,day_since_last_order,cash_back_amount
    if prediction == 0:
        text = "No Churn"
    else:
        text = "Churn"

    return text

def main():

    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Churn Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    # exp = st.number_input('Experience', 2, 40)
    tenure = st.number_input('Tenure',step =1., format="%.2f")
    login_device = st.radio('Preferred Login Device', ['Mobile Phone', 'Computer','Phone'])
    city_tier = st.number_input('City Tier', 1, 3)
    warehouse_to_home = st.number_input('Warehouse To Home', 5, 127)
    preferred_payment_mode = st.selectbox('Preferred Payment Mode', ['Debit Card', 'Credit Card','E wallet','UPI', 'COD','CC','Cash on Delivery'])
    gender = st.radio('Gender', ['Male', 'Female'])
    hour_spend_on_app = st.number_input('Hour Spend on App', 1, 5)
    number_of_device_registered = st.number_input('Number_of_Device_Registered', 1, 6)
    prefered_order_cat = st.selectbox('Prefered Order Cat', ['Laptop & Accessory', 'Mobile Phone','Fashion','Mobile', 'Grocery','Others'])
    satisfaction_score = st.slider('Satisfication', 1,5)
    marital_status = st.radio('Marital Status', ['Single', 'Married','Divorced'])
    number_of_address = st.number_input('Number of Address', 1, 22)
    complain = st.radio('Complain', ['Yes', 'No'])
    order_amount_hike_from_last_year = st.number_input('Increase in Order', 11, 26)
    coupon_used = st.number_input('Coupon Used', 0, 16)
    order_count = st.number_input('Order Count', 1, 16)
    day_since_last_order  = st.number_input('Day Since Last Order', 0, 46)
    cash_back_amount  = st.number_input('Cash Back Amount', step =1., format="%.2f")

    result=""
    if st.button("Predict"):
        result=predict(float(tenure),login_device,float(city_tier),float(warehouse_to_home),preferred_payment_mode,gender,hour_spend_on_app,number_of_device_registered,
        prefered_order_cat,satisfaction_score,marital_status,number_of_address,complain,order_amount_hike_from_last_year,coupon_used,
        order_count,day_since_last_order,cash_back_amount)
    st.success(result)

    if st.button("About me"):
        st.text("By Mohnish Sachdeva")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
