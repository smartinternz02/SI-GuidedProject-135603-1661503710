from flask import Flask
from flask import request, render_template
from flask_cors import CORS
import joblib

app=Flask(__name__,static_url_path='')
CORS(app)

@app.route('/',methods=['GET'])
def sendhomepage():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predictEmployeepromotion():
    D=request.form['D']
    R=request.form['R']
    E=request.form['E']
    G=request.form['G']
    RC=request.form['RC']
    T=int(request.form['T'])
    A=float(request.form['A'])
    PYR=float(request.form['PYR'])
    LOS=float(request.form['LOS'])
    KPI=int(request.form['KPI'])
    AW=int(request.form['AW'])
    AVS=int(request.form['AVS'])
    X =[[D,R,E,G,RC,T,A,PYR,LOS,KPI,AW,AVS]]
    model=joblib.load('model.pkl')
    promotion=model.predict(X)[0]
    return render_template('predict.html',predict=promotion)

if __name__=='__main__':
    app.run(debug=False)


