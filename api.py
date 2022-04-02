from flask import Flask, request
import pandas as pd


app = Flask(__name__)


@app.route('/tech', methods=['POST'])
def by_tech():
    jobs = pd.read_csv('jobs.csv')
    input = request.get_json()
    tech_name = input['techName']
    page = int(input['page']) if input['page'] else 0
    sorting = input['sorting'] if input['sorting'] else 0

    filtered_jobs = jobs.loc[jobs['Tech Stack'].str.contains(tech_name, na=False)]

    if sorting:
        filtered_jobs = filtered_jobs.sort_values(by=[sorting])

    return filtered_jobs[page*10:page*10+10].drop(['Unnamed: 0'], axis=1).to_json(orient='records')


@app.route('/location', methods=['POST'])
def by_location():
    jobs = pd.read_csv('jobs.csv')
    input = request.get_json()
    location = input['location']
    page = int(input['page']) if input['page'] else 0
    sorting = input['sorting'] if input['sorting'] else 0

    filtered_jobs = jobs.loc[jobs['Location'] == location]
    if sorting:
        filtered_jobs = filtered_jobs.sort_values(by=[sorting])

    return filtered_jobs[page*10:page*10+10].drop(['Unnamed: 0'], axis=1).to_json(orient='records')


if __name__ == '__main__':
    app.run(debug=True)