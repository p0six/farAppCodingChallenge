from flask import Flask, render_template
import requests
import mysql.connector
from flask_bootstrap import Bootstrap

# from flask_oauth import OAuth # My issue fixed by updating Werkzeug=0.16.1

# create table users (id INT not null auto_increment primary key, firstName varchar(100),
# lastName varchar(100), email varchar(100), phone varchar(100))
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sl4shd0t",
  database = 'farApp'
)
mycursor = mydb.cursor()

# response = requests.get('https://randomuser.me/api/?nat=us&results=1000')
# for result in response.json()['results']:
#     first = result['name']['first']
#     last = result['name']['last']
#     email = result['email']
#     phone = result['phone']
#     sql = "INSERT INTO users (firstName, lastName, email, phone) VALUES (%s, %s, %s, %s)"
#     params = str(first), str(last), str(email), str(phone)
#     mycursor.execute(sql, params)
#     mydb.commit()


app = Flask(__name__)
Bootstrap(app)


# oauth = OAuth()
# faceBook = oauth.remote_app('twitter',
#     base_url='https://api.twitter.com/1/',
#     request_token_url='https://api.twitter.com/oauth/request_token',
#     access_token_url='https://www.linkedin.com/oauth/v2/accessToken',
#     authorize_url='https://www.linkedin.com/oauth/v2/authorization',
#     consumer_key='86phs8639euokq',
#     consumer_secret='3BpMK70aPbWuI9YG'
# )

# api key is 'S34M-BYYP-TUMN-GFSC'

@app.route('/')
def hello_world():
    mycursor.execute("SELECT * FROM users")
    users = mycursor.fetchall()
    return render_template('index.html', users=users)
    # users = ''
    # for x in myresult:
    #     users += x[1] + ',' + x[2] + ',' + x[3] + ',' + x[4] + '<br>'
    # return(users)


if __name__ == '__main__':
    app.run()

