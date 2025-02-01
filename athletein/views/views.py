from flask import Blueprint, render_template, redirect, url_for

views_bp = Blueprint("views", __name__)


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
@views_bp.route("/")
def views():
    return "This is homepage"