from flask import Flask,render_template,request
import pickle
app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
	if request.method =="POST":
		f=None
		model=None
		try:
			f=open("diabetes.model","rb")
			model=pickle.load(f)
		except Exception as e:
			msg="f issue" +str(e)
			return render_template("home.html",msg=msg)
		finally:
			if f is not None:
				f.close()
		if model is not None:
			fs=float(request.form["fs"])
			fu=request.form["fu"]
			if fu ==1:
				data=[[fs,1,0]]
			else:
				data=[[fs,0,1]]
			ans=model.predict(data)
			msg="ans =" +ans
			return render_template("home.html",msg=msg)
		else:
			return render_template("home.html",msg="model issue")
	else:
		return render_template("home.html")

if __name__=="__main__":
	app.run(debug=True,use_reloader=True)