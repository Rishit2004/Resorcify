import os
import pandas as pd
import mysql.connector

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='ritu12345',
        database='resorcify'
    )

    sql = "select * from employee;"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    df = pd.DataFrame(myresult)

    # Check if the HTML file already exists
    html_path = 'templates/sql-data.html'
    if os.path.exists(html_path):
        # Load existing HTML file and append new data
        existing_df = pd.read_html(html_path)[0]
        df = pd.concat([existing_df, df], ignore_index=True)

    # Save the updated DataFrame to HTML
    df.to_html(html_path, index=False)

    return render_template('sql-data.html', tables=[df.to_html(classes='data')], titles=df.columns.values)

if __name__ == '__main__':
    app.run(debug=True)
