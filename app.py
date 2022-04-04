from flask import Flask, render_template, request
import pickle
import numpy as np

ani_df = pickle.load(open('anime_sim_df.pkl','rb'))
ani_cols = list(ani_df.columns)


app = Flask(__name__)

@app.route('/')
def main():
    return render_template('home.html', ani_cols = ani_cols)

def anime_rec_list(ani_name):
    rec_list = []
    for anime in ani_df.sort_values(by=ani_name, ascending=False).index[1:6]:
        rec_list.append(anime)
    return rec_list

# @app.route('/predict', methods=['POST'])
# def home():
#     data1 = request.form.get('ani_name')
#     return render_template('after.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)















