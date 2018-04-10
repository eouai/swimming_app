from flask import Flask, render_template, request
import bokeh
import pandas as pd
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file

app = Flask(__name__)

df = pd.read_csv('static/swimming_data.csv')


def create_figure(current_feature_name, bins):
    p = Histogram(iris_df, current_feature_name, title=current_feature_name, color='Species',
                  bins=bins, legend='top_right', width=600, height=400)

    # Set the x axis label
    p.xaxis.axis_label = current_feature_name

    # Set the y axis label
    p.yaxis.axis_label = 'Count'
    return p


@app.route('/')
def homepage():
    return render_template("main.html")


@app.route('/dashboard/')
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run()
