from flask import Flask, render_template
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

# Generate sample data
def generate_data():
    np.random.seed(0)
    dates = pd.date_range('2024-01-01', periods=100)
    data = pd.DataFrame(np.random.randn(100, 4), index=dates, columns=list('ABCD'))
    return data

# Function to create a line plot
def create_line_plot(data):
    plt.figure(figsize=(10, 6))
    for column in data.columns:
        plt.plot(data.index, data[column], label=column)
    plt.title('Line Plot')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    # Convert plot to base64 encoded image
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_image = base64.b64encode(buffer.getvalue()).decode()
    plt.close()
    return plot_image

@app.route('/')
def index():
    # Generate sample data
    data = generate_data()
    
    # Create line plot
    plot_image = create_line_plot(data)
    
    # Pass plot image and data to template
    return render_template('index.html', plot_image=plot_image, data_table=data.to_html())

if __name__ == '__main__':
    app.run(debug=True)
