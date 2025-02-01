from flask import render_template, request, url_for, g, flash, Blueprint, session, redirect

auth_bp = Blueprint('auth',__name__, url_prefix='/auth')


"""
While writing the function make sure that return data as python dictionary in string

eg: return '{'status':'success','user_id':123456, 'friends_list':[123145,2165,1315,],
 'chat_history':[some chat data from database]}'

 This type of format is known as json.

 At first we won't have database so you need to assume that in near future you will call a 
 function which will return the data in the format specified above. First write the function 
 somewhere else, then make data on your own or by use of Gemini after that test the function
  if it runs successfully then implement it in the project.

  eg:
def recomendation_generator():
    try:
        data = get_data_from_database()
        running some algorithm........
        return {'status':'success', 'recomendation_data':[data1,data2....]}
    except Exception as e:
        return {'status':'error', 'message':e}
    
"""

@auth_bp.route('/signup', methods=["GET", "POST"])
def signup():
    return "This is signup page"


@auth_bp.route('/signin', methods=["GET","POST"])
def signin():
    return "This is signup page"

@auth_bp.route('/logout')
def logout():
    # session.clear()
    return redirect(url_for('main.home'))