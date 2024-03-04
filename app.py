from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)
@app.route("/",methods=['POST','GET'])
def index():
    gpa = ''
    # template="templates/index.html"
    M=[]
    Grade_points=[]
    Credit_points=[3,4,4,3,1,3,1,1,0]
    GxC=[]
    if request.method=='POST':
        maths = float(request.form.get('maths'))
        dsdv = float(request.form.get('dsdv'))
        epc = float(request.form.get('epc'))
        na = float(request.form.get('na'))
        adsd = float(request.form.get('adsd'))
        coa = float(request.form.get('coa'))
        scr = float(request.form.get('scr'))
        labview = float(request.form.get('labview'))
        yoga = float(request.form.get('maths'))
        M = [maths,dsdv,epc,na,adsd,coa,scr,labview,yoga]
        for i in M:
            GP = Grade(i)
            Grade_points.append(GP)
        for j in range(len(Credit_points)):
            gxc = Grade_points[j]*Credit_points[j]
            GxC.append(gxc)
        gpa = sum(GxC)/sum(Credit_points)

        print(GxC)

    return render_template('index.html',gpa=gpa,M=M,Grade_points=Grade_points,GxC=GxC)

def Grade(marks):
    if marks>90:
        grade=10
    elif marks>80:
        grade=9
    elif marks>70:
        grade=8
    elif marks>60:
        grade=7
    elif marks>50:
        grade=6
    elif marks>45:
        grade=5
    elif marks>40:
        grade=4
    else:
        grade=0
    return grade

# if __name__=="__main__":
#     app.run()