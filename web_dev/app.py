from flask import Flask,redirect,render_template,request
app = Flask(__name__)


@app.route('/, methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('/login.html')
    elif request.method == 'POST':
        form = request.form
        email = form['email']
        password = form['password']
        print(email,password)

        if email == 'emanhbua@gmail.com' and password = '111':
            return redirect('/survey')
        else:
            print('login failed')
            return render_template('login.html')

@app.route('/thegioicuadaicabua')
def bua_day():
    return'chao mung chu em den voi the gioi cua dai ca bua'
@app.route('/redirect_to_tech')
def go_to_techwithtim():
    return redirect('https://www.youtube.com/channel/UC4JX40jDee_tINbkjycV4Sg')
@app.route('/ailaemanhbua/<string:name>')
def emanhbua(name):
    return '{} la em anh bua'.format(name)
@app.route('/add-number/<int:number_1>/<int:number_2>')
def get_sum(number_1,number_2):
    total = number_1 + number_2
    return 'the sum is {}'.format(str(total))
@app.route('/survey',methods =['GET','POST'])
def survey():
    if request.method == 'GET':
        return render_template('survey.html')
    elif request.method == 'POST':
        form = request.form
        answer_1= form['question1']
        answer_2= form['question2']
        user_agent = request.user_agent
        platform = user_agent.platform
        version = user_agent.browser
        language = user_agent.language
        submit_time = datetime.now()
        print(answer_1,answer_2)
        print(platform,version,browser,language,submit_time)
        return 'thank for your information'
if __name__ == '__main__':
    app.run()