# Does not adjust for inflation
import requests
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from bs4 import BeautifulSoup
import array as arr 

#percent_list = arr.array('d', [])
#years_list = arr.array('i', [])

app = Flask(__name__)

ENV = 'prod'

if ENV == 'dev':
    app.debug=True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ipp95FmQ6jN@localhost/stock'
else:
    app.debug=False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://nhpdtcsmzpwihg:06bb44b3937433a7bbc3408c211aa78bdbaacd4cc5d8a82bffba0a7c88a5820c@ec2-18-235-109-97.compute-1.amazonaws.com:5432/ddejuj26ko5dee'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class stock(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    start_year = db.Column(db.Integer)
    end_year = db.Column(db.Integer)
    def __init__(self, start_year, end_year):
            self.end_year = end_year
            self.start_year = start_year
    

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/home')
def home():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/submit', methods=['POST'])
def submit():
    
    percent_list = arr.array('d', [])
    years_list = arr.array('i', [])
    p1num1 = 0
    p2num1 = 0
    p3num1 = 0
    p1num2 = 0
    p2num2 = 0
    p3num2 = 0
    p1num3 = 0
    p2num3 = 0
    p3num3 = 0
    p1num4 = 0
    p2num4 = 0
    p3num4 = 0

    if request.method == 'POST':
        initial = request.form['initial value']
        start = request.form['start year']
        end = request.form['end year']

        asset1 = request.form['stock ticker 1']
        percent_row_1_col_2 = request.form['percent row 1 col 2']
        percent_row_2_col_2 = request.form['percent row 2 col 2']
        percent_row_3_col_2 = request.form['percent row 3 col 2']
        percent_row_4_col_2 = request.form['percent row 4 col 2']
        asset1 = asset1.upper()

        asset2 = request.form['stock ticker 2']
        asset2 = asset2.upper()

        asset3 = request.form['stock ticker 3']
        asset3 = asset3.upper()

        asset4 = request.form['stock ticker 4']
        asset4 = asset4.upper()

        percent_row_1_col_3 = request.form['percent row 1 col 3']
        percent_row_2_col_3 = request.form['percent row 2 col 3']
        percent_row_3_col_3 = request.form['percent row 3 col 3']
        percent_row_4_col_3 = request.form['percent row 4 col 3']

        percent_row_1_col_4 = request.form['percent row 1 col 4']
        percent_row_1_col_4 = request.form['percent row 1 col 4']
        percent_row_1_col_4 = request.form['percent row 1 col 4']
        percent_row_1_col_4 = request.form['percent row 1 col 4']
        
        percent_total1 = int(percent_row_1_col_2) + int(percent_row_2_col_2) + int(percent_row_3_col_2) + int(percent_row_4_col_2)
        percent_total2 = int(percent_row_1_col_3) + int(percent_row_2_col_3) + int(percent_row_3_col_3) + int(percent_row_4_col_3)
        if percent_total1 != 100 and percent_total2 != 100:
            return "Percent total does not add up to 100"

        if asset1 == "GOOGL":
            p1num1 = getGoogle(initial, start, end, years_list, percent_list, percent_row_1_col_2)
            p2num1 = getGoogle(initial, start, end, years_list, percent_list, percent_row_1_col_3)
            p3num1 = getGoogle(initial, start, end, years_list, percent_list, percent_row_1_col_4)

        elif asset1 == "AAPL":
            p1num1 = getApple(initial, start, end, years_list, percent_list, percent_row_1_col_2)
            p2num1 = getApple(initial, start, end, years_list, percent_list, percent_row_1_col_3)
            p3num1 = getApple(initial, start, end, years_list, percent_list, percent_row_1_col_4)

        elif asset1 == "AMZN":
            p1num1 = getAmazon(initial, start, end, years_list, percent_list, percent_row_1_col_2)
            p2num1 = getAmazon(initial, start, end, years_list, percent_list, percent_row_1_col_3)
            p3num1 = getAmazon(initial, start, end, years_list, percent_list, percent_row_1_col_4)
        elif asset1 == "BRKB":
            p1num1 = getBerkshire(initial, start, end, years_list, percent_list, percent_row_1_col_2)
            p2num1 = getBerkshire(initial, start, end, years_list, percent_list, percent_row_1_col_3)
            p3num1 = getBerkshire(initial, start, end, years_list, percent_list, percent_row_1_col_4)
        elif asset1 == "JNJ":
            p1num1 = getJohnson(initial, start, end, years_list, percent_list, percent_row_1_col_2)
            p2num1 = getJohnson(initial, start, end, years_list, percent_list, percent_row_1_col_3)
            p3num1 = getJohnson(initial, start, end, years_list, percent_list, percent_row_1_col_4)
            
        elif asset1 == "MSFT":
            p1num1 = getMicrosoft(initial, start, end, years_list, percent_list, percent_row_1_col_2)
            p2num1 = getMicrosoft(initial, start, end, years_list, percent_list, percent_row_1_col_3)
            p3num1 = getMicrosoft(initial, start, end, years_list, percent_list, percent_row_1_col_4)

        elif asset1 == "FB":
            p1num1 = getFacebook(initial, start, end, years_list, percent_list, percent_row_1_col_2)
            p2num2 = getFacebook(initial, start, end, years_list, percent_list, percent_row_1_col_3)
            p3num1 = getFacebook(initial, start, end, years_list, percent_list, percent_row_1_col_4)

        if asset2 == "GOOGL":
            del percent_list[:]
            del years_list[:]
            p1num2 = getGoogle(initial, start, end, years_list, percent_list, percent_row_2_col_2)
            p2num2 = getGoogle(initial, start, end, years_list, percent_list, percent_row_2_col_3)
            p3num2 = getGoogle(initial, start, end, years_list, percent_list, percent_row_2_col_4)

        elif asset2 == "AAPL":
            del percent_list[:]
            del years_list[:]
            p1num2 = getApple(initial, start, end, years_list, percent_list, percent_row_2_col_2)
            p2num2 = getApple(initial, start, end, years_list, percent_list, percent_row_2_col_3)
            p3num2 = getApple(initial, start, end, years_list, percent_list, percent_row_2_col_4)

        elif asset2 == "AMZN":
            del percent_list[:]
            del years_list[:]
            p1num2 = getAmazon(initial, start, end, years_list, percent_list, percent_row_2_col_2)
            p2num2 = getAmazon(initial, start, end, years_list, percent_list, percent_row_2_col_3)
            p3num2 = getAmazon(initial, start, end, years_list, percent_list, percent_row_2_col_4)

        elif asset2 == "BRKB":
            del percent_list[:]
            del years_list[:]
            p1num2 = getBerkshire(initial, start, end, years_list, percent_list, percent_row_2_col_2)
            p2num2 = getBerkshire(initial, start, end, years_list, percent_list, percent_row_2_col_3)
            p3num2 = getBerkshire(initial, start, end, years_list, percent_list, percent_row_2_col_4)

        elif asset2 == "JNJ":
            del percent_list[:]
            del years_list[:]
            p1num2 = getJohnson(initial, start, end, years_list, percent_list, percent_row_2_col_2)
            p2num2 = getJohnson(initial, start, end, years_list, percent_list, percent_row_2_col_3)
            p3num2 = getJohnson(initial, start, end, years_list, percent_list, percent_row_2_col_4)

        elif asset2 == "MSFT":
            del percent_list[:]
            del years_list[:]
            p1num2 = getMicrosoft(initial, start, end, years_list, percent_list, percent_row_2_col_2)
            p2num2 = getMicrosoft(initial, start, end, years_list, percent_list, percent_row_2_col_3)
            p3num2 = getMicrosoft(initial, start, end, years_list, percent_list, percent_row_2_col_4)

        elif asset2 == "FB":
            del percent_list[:]
            del years_list[:]
            p1num2 = getFacebook(initial, start, end, years_list, percent_list, percent_row_2_col_2)
            p2num2 = getFacebook(initial, start, end, years_list, percent_list, percent_row_2_col_3)
            p3num2 = getFacebook(initial, start, end, years_list, percent_list, percent_row_2_col_4)
            
        if asset3 == "GOOGL":
            del percent_list[:]
            del years_list[:]
            p1num3 = getGoogle(initial, start, end, years_list, percent_list, percent_row_3_col_2)
            p2num3 = getGoogle(initial, start, end, years_list, percent_list, percent_row_3_col_3)
            p3num3 = getGoogle(initial, start, end, years_list, percent_list, percent_row_3_col_4)

        elif asset3 == "AAPL":
            del percent_list[:]
            del years_list[:]
            p1num3 = getApple(initial, start, end, years_list, percent_list, percent_row_3_col_2)
            p2num3 = getApple(initial, start, end, years_list, percent_list, percent_row_3_col_3)
            p3num3 = getApple(initial, start, end, years_list, percent_list, percent_row_3_col_4)

        elif asset3 == "AMZN":
            del percent_list[:]
            del years_list[:]
            p1num3 = getAmazon(initial, start, end, years_list, percent_list, percent_row_3_col_2)
            p2num3 = getAmazon(initial, start, end, years_list, percent_list, percent_row_3_col_3)
            p3num3 = getAmazon(initial, start, end, years_list, percent_list, percent_row_3_col_4)

        elif asset3 == "BRKB":
            del percent_list[:]
            del years_list[:]
            p1num3 = getBerkshire(initial, start, end, years_list, percent_list, percent_row_3_col_2)
            p2num3 = getBerkshire(initial, start, end, years_list, percent_list, percent_row_3_col_3)
            p3num3 = getBerkshire(initial, start, end, years_list, percent_list, percent_row_3_col_4)

        elif asset3 == "JNJ":
            del percent_list[:]
            del years_list[:]
            p1num3 = getAmazon(initial, start, end, years_list, percent_list, percent_row_3_col_2)
            p2num3 = getAmazon(initial, start, end, years_list, percent_list, percent_row_3_col_3)
            p3num3 = getAmazon(initial, start, end, years_list, percent_list, percent_row_3_col_4)

        elif asset3 == "MSFT":
            del percent_list[:]
            del years_list[:]
            p1num3 = getMicrosoft(initial, start, end, years_list, percent_list, percent_row_3_col_2)
            p2num3 = getMicrosoft(initial, start, end, years_list, percent_list, percent_row_3_col_3)
            p3num3 = getMicrosoft(initial, start, end, years_list, percent_list, percent_row_3_col_4)

        elif asset3 == "FB":
            del percent_list[:]
            del years_list[:]
            p1num3 = getFacebook(initial, start, end, years_list, percent_list, percent_row_3_col_2)
            p2num3 = getFacebook(initial, start, end, years_list, percent_list, percent_row_3_col_3)
            p3num3 = getFacebook(initial, start, end, years_list, percent_list, percent_row_3_col_4)

        if asset4 == "GOOGL":
            del percent_list[:]
            del years_list[:]
            p1num4 = getGoogle(initial, start, end, years_list, percent_list, percent_row_4_col_2)
            p2num4 = getGoogle(initial, start, end, years_list, percent_list, percent_row_4_col_3)
            p3num4 = getGoogle(initial, start, end, years_list, percent_list, percent_row_4_col_4)

        elif asset4 == "AAPL":
            del percent_list[:]
            del years_list[:]
            p1num4 = getApple(initial, start, end, years_list, percent_list, percent_row_4_col_2)
            p2num4 = getApple(initial, start, end, years_list, percent_list, percent_row_4_col_3)
            p3num4 = getApple(initial, start, end, years_list, percent_list, percent_row_4_col_4)

        elif asset4 == "AMZN":
            del percent_list[:]
            del years_list[:]
            p1num4 = getAmazon(initial, start, end, years_list, percent_list, percent_row_4_col_2)
            p2num4 = getAmazon(initial, start, end, years_list, percent_list, percent_row_4_col_3)
            p3num4 = getAmazon(initial, start, end, years_list, percent_list, percent_row_4_col_4)


        elif asset4 == "BRKB":
            del percent_list[:]
            del years_list[:]
            p1num4 = getBerkshire(initial, start, end, years_list, percent_list, percent_row_4_col_2)
            p2num4 = getBerkshire(initial, start, end, years_list, percent_list, percent_row_4_col_3)
            p3num4 = getBerkshire(initial, start, end, years_list, percent_list, percent_row_4_col_4)


        elif asset4 == "JNJ":
            del percent_list[:]
            del years_list[:]
            p1num4 = getJohnson(initial, start, end, years_list, percent_list, percent_row_4_col_2)
            p2num4 = getJohnson(initial, start, end, years_list, percent_list, percent_row_4_col_3)
            p3num4 = getJohnson(initial, start, end, years_list, percent_list, percent_row_4_col_4)


        elif asset4 == "MSFT":
            del percent_list[:]
            del years_list[:]
            p1num4 = getMicrosoft(initial, start, end, years_list, percent_list, percent_row_4_col_2)
            p2num4 = getMicrosoft(initial, start, end, years_list, percent_list, percent_row_4_col_3)
            p3num4 = getMicrosoft(initial, start, end, years_list, percent_list, percent_row_4_col_4)

        elif asset4 == "FB":
            del percent_list[:]
            del years_list[:]
            p1num4 = getFacebook(initial, start, end, years_list, percent_list, percent_row_4_col_2)
            p2num4 = getFacebook(initial, start, end, years_list, percent_list, percent_row_4_col_3)
            p3num4 = getFacebook(initial, start, end, years_list, percent_list, percent_row_4_col_4)


        total1 = float(p1num1) + float(p1num2) + float(p1num3) + float(p1num4)
        total2 = float(p2num1) + float(p2num2) + float(p2num3) + float(p2num4)
        total3 = float(p3num1) + float(p3num2) + float(p3num3) + float(p3num4)

        



        
    #data = stock(start, end)
    #db.session.add(data)
    #db.session.commit()    
    #return str(total)
    return "Portfolio 1: ${:.2f}".format(total1) + " Portfolio 2: ${:.2f}".format(total2) + " Portfolio 3: ${:.2f}".format(total3)
def getGoogle(initial, start, end, years_list, percent_list, percent1):

    result = requests.get("http://www.1stock1.com/1stock1_178.htm")
    src = result.content
    soup = BeautifulSoup(src, 'lxml')

    #port1 = calculate(initial, start, end, years_list, percent_list, percent1, result, src, soup)
    #port2 = calculate(initial, start, end, years_list, percent_list, percent2, result, src, soup)
    return calculate(initial, start, end, years_list, percent_list, percent1, result, src, soup)

def getApple(initial, start, end, years_list, percent_list, percent1):

    result = requests.get("http://www.1stock1.com/1stock1_148.htm")
    src = result.content
    soup = BeautifulSoup(src, 'lxml')

    return calculate(initial, start, end, years_list, percent_list, percent1, result, src, soup)

def getAmazon(initial, start, end, years_list, percent_list, percent1):
    result = requests.get("http://www.1stock1.com/1stock1_146.htm")
    src = result.content
    soup = BeautifulSoup(src, 'lxml')

    return calculate(initial, start, end, years_list, percent_list, percent1, result, src, soup)
def getBerkshire(initial, start, end, years_list, percent_list, percent1):

    result = requests.get("http://www.1stock1.com/1stock1_897.htm")
    src = result.content
    soup = BeautifulSoup(src, 'lxml')

    return calculate(initial, start, end, years_list, percent_list, percent1, result, src, soup)

def getJohnson(initial, start, end, years_list, percent_list, percent1):

    result = requests.get("http://www.1stock1.com/1stock1_235.htm")
    src = result.content
    soup = BeautifulSoup(src, 'lxml')

    return calculate(initial, start, end, years_list, percent_list, percent1, result, src, soup)

def getMicrosoft(initial, start, end, years_list, percent_list, percent1):
    result = requests.get("http://www.1stock1.com/1stock1_215.htm")
    src = result.content
    soup = BeautifulSoup(src, 'lxml')

    return calculate(initial, start, end, years_list, percent_list, percent1, result, src, soup)

def getFacebook(initial, start, end, years_list, percent_list, percent1):
    result = requests.get("http://www.1stock1.com/1stock1_577.htm")
    src = result.content
    soup = BeautifulSoup(src, 'lxml')

    return calculate(initial, start, end, years_list, percent_list, percent1, result, src, soup)


def calculate(initial, start_year, end_year, years_list, percent_list, percent1, result, src, soup):
    #result = requests.get("http://www.1stock1.com/1stock1_178.htm")
    #src = result.content
    #soup = BeautifulSoup(src, 'lxml')

    initial = float(initial) * (int(percent1) / 100)
    print(initial)

    table = soup.findAll('table', cellspacing="0")

    count1 = 0
    for years in table:
        single_year = years.findAll('tr')
        for data in single_year:
            name1 = data.findAll('td')
            for n in name1:
         
                info = n.text
                info = info.strip()
           
                if info[len(info) - 1] == '%':
                    percent_list.append(float(info[:-1]))
                    count1+1
                elif "." not in info:
                    if "e" not in info:
                        if "o" not in info:
                            #print(info)
                            single_year = int(info)
                            years_list.append(single_year)

    
    count2 = 0
    j = 0
    #years_list_length = len(years_list)
    for i in percent_list:
       
        # print(years_list[count2])
        
        if years_list[count2] < int(start_year):
            count2+=1
            
        elif years_list[count2] == int(end_year):
            print(i)
            final = (int(initial)*((1 + (i /100))**1))

            # final has more than 2 decimals changing the values
            initial = final
   
            # print(years_list[count2], "${:.2f}".format(final))
            count2+=1
            break

        else:
            print(i)
            final = (int(initial)*((1 + (i /100))**1))

            # final has more than 2 decimals changing the values
            initial = final
   
            # print(years_list[count2], "${:.2f}".format(final))
            count2+=1
    hey = 'h'
    # print("${:.2f}".format(final))
    # return "{:.2f}".format(final)
    return str(final)


if __name__ == '__main__':
    
    app.run()