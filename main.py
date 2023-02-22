import mysql.connector
from flask import Flask, request, redirect

app = Flask(__name__)
connection = mysql.connector.connect(user='Yousaf', password='readmymind3', host='localhost', port=3306,
 database='dexter')
def generate_single_option(row):
    return f'''<option value="{row['station_ID']}">{row['station_name']}</option>''' 
def generate_options(stations):   
        rows=""
        for station in stations: 
            rows+=generate_single_option(station)
            rows+='\n'
        return rows


def generate_single_payment(payment_row):
    return f"""
        <tr>
            <td>{payment_row['passenger_ID']}</td>
            <td>{payment_row['Payment_ID']}</td>
            <td>{payment_row['name']}</td>
            <td>{payment_row['fare']}</td>
            <td>{payment_row['ticket_generated']}</td>
        </tr>
    """


def generate_payment_rows(payment_rows):
    rows = ""
    for payment_row in payment_rows:
        rows += generate_single_payment(payment_row)
        rows += "\n"
    return rows

@app.route(f"/payments", methods=['GET'])
def get_payment_rows():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('''select ps.passenger_ID, p.Payment_ID, ps.name, p.fare, p.ticket_generated from payment p
                    inner join passenger ps on ps.passenger_ID = p.passenger_ID
                    order by 1 desc''')
        
    payment_rows = cursor.fetchall()
    print(payment_rows)
    
    # Close the connection
    cursor.close()
    connection.close()
    return f"""
        <strong>Successfully Booked</strong>
        <form method= "GET" align="center">
            <table align = "center">
            <thead align = "center">
            <th>passenger_ID</th>
            <th>Payment_ID</th>
            <th>name</th>
            <th>fare</th>
            <th>ticket_generated</th>
            </thead>
            <tbody>
                {generate_payment_rows(payment_rows)}
            </tbody>
            </table>
            
            </form> 
        """

@app.route('/', methods=['GET', 'POST'])
def index():
    connection = get_db_connection()
#     connection = mysql.connector.connect(user='Yousaf', password='readmymind3', host='localhost', port=3306,
#  database='dexter')
    if request.method == 'POST':
        # Get the form data from the request
        Name = request.form['Name']
        CNIC = request.form['CNIC']
        age = request.form['age']
        gender = request.form['gender']
        phone = request.form['phone']
        source_ID = request.form['source_ID']

        cursor = connection.cursor()

        # Insert the data into the Passenger table
        sql = "INSERT INTO Passenger (Name, CNIC, age, gender, phone , source_ID) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (Name, CNIC, age, gender, phone, source_ID)
        cursor.execute(sql, values)
        connection.commit()

        passenger_ID = cursor.lastrowid
        print (passenger_ID)
        # Close the connection
        cursor.close()
        connection.close()

        # return redirect(url_for('dex', passenger_ID))
        
        return redirect(f'''/booking/{passenger_ID}''')
    else:

        cursor = connection.cursor(dictionary=True)
        cursor.execute("""SELECT * from station""")
        
        # Fetch the rows and store them in a list
        station = cursor.fetchall()
        print(station)
        # Close the connection
        cursor.close()
        connection.close()

        return f'''

<body style="background-image: url('https://images.unsplash.com/photo-1580940583249-77175ce5f75a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80'); background-repeat: no-repeat; background-size: cover;">


            <form method="POST" align="center">
            <h1 style ="color : white">Raliway Management System Project - DBMS</h1>
            <h3 style ="color : white"><i><marquee>created by Dexter</marquee></i></h3>
                <h2 style ="color : white"> Add Passenger details to continue</h2>
                    Name: <input type="text" name="Name" placeholder="Slade Wilson" ><br><br>
                    CNIC: <input type="text" name="CNIC" placeholder="3311120155254"><br><br>
                    Age: <input type="number" name="age" placeholder="69"><br><br>
                    Gender: <input type="text" name="gender" placeholder="M or F"><br><br>
                    Phone: <input type="text" name="phone" placeholder="03215887445"><br><br>

                    <label for="source_ID">Choose your current station: </label>
                    <select name="source_ID" id="source_ID">
                     {generate_options(station)}   
                    </select>

                    <input type="submit" value="Submit" padding><br>

            </form>
            </body>
    '''


def generate_single_row(row):
    return f"""
        <tr>
            <td>{row['train_ID']}</td>
            <td>{row['name']}</td>
            <td>{row['dep_time']}</td>
            <td>{row['arival_time']}</td>
            <td>{row['station_ID']}</td>
            <td>{row['station_name']}</td>
            <td>{row['station_Adress']}</td>
        </tr>
    """


def generate_rows(schedules):
    rows = ""
    for schedule in schedules:
        rows += generate_single_row(schedule)
        rows += "\n"
    return rows

@app.route(f"/booking/<passenger_ID>", methods=['GET', 'POST'])
def dex(passenger_ID):
    if request.method == 'POST':
        # Get the form data from the request
        station_ID = request.form['station_ID']
        passenger_ID = request.form['passenger_ID']
        source_ID = request.form['source_ID']
        train_ID = request.form['train_ID']
        Seat_no = request.form['Seat_no']
        fare = request.form['fare']
        payment_status = request.form['payment_status']

        print(passenger_ID)
        
        # Connect to the database
        connection = get_db_connection()
        cursor = connection.cursor()

        # Insert the data into the Passenger table
        sql = "INSERT INTO payment (station_ID, passenger_ID, source_ID, train_ID, Seat_no ,fare, payment_status) VALUES (%s, %s, %s, %s, %s,%s,%s)"
        values = (station_ID, passenger_ID, source_ID, train_ID, Seat_no,fare, payment_status)
        cursor.execute(sql, values)
        connection.commit()
        # Close the connection
        cursor.close()
        connection.close()
        # get_payment_rows()
        # print("Passenger_ID", passenger_ID)
        return redirect(f'''/payments''')
        
    else:
        return f'''

            <form method="POST" align="center">
                <h2> booking screen</h2>
                    station_ID: <input type="number" name="station_ID" placeholder="1 - 4"><br>
                    passenger_ID: <input type="number" name="passenger_ID" placeholder="available in the URL" value={passenger_ID}><br>
                    source_ID: <input type="number" name="source_ID" placeholder="1 - 4"><br>
                    train_ID: <input type="number" name="train_ID" placeholder="1 - 4"><br>
                    Seat_no: <input type="number" name="Seat_no" placeholder="to be decided by the booking person"><br>
                    fare: <input type="number" name="fare" placeholder="100 rs/station"><br>
                    payment_status: <input type="text" name="payment_status" placeholder="done / due"><br>
                  <input type="submit" value="Submit"><br>
            </form>

            {get_schedule()}
    '''
def get_schedule():
    connection = mysql.connector.connect(user='Yousaf', password='readmymind3', host='localhost', port=3306,
 database='dexter')
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""SELECT tr.train_ID, tr.name , sh.dep_time , sh.arival_time, st.station_ID, st.station_name, st.station_Adress
                        FROM schedule as sh
                        INNER JOIN train as tr
                        ON sh.train_ID = tr.train_ID 
                        inner join station as st
                        on st.station_ID = sh.station_ID
                        ORDER BY tr.name""")
        
    schedules = cursor.fetchall()
    print(schedules)
    
    # Close the connection
    cursor.close()
    connection.close()
    return f"""
        <form align="center">
            <table align = "center">
            <thead align = "center">
            <th>Train ID</th>
            <th>Train name</th>
            <th>arrival time</th>
            <th>departure time</th>
            <th>station ID</th>
            <th>station name</th>
            <th>station city</th>
            </thead>
            <tbody>
                {generate_rows(schedules)}
            </tbody>
            </table>
            
            </form> 
        """
def get_db_connection():
    return mysql.connector.connect(user='Yousaf', password='readmymind3', host='localhost', port=3306,
 database='dexter')

if __name__ == '_main_':
    app.run()
app.run(debug=True)
