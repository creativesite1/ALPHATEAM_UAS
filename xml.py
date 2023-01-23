from dash import dash
import pandas as pd

@app.get('data_xml')
def data_xml():
    df = pd.read_csv('Cars.csv')
    df.to_xml('Cars.xml')
    return FileResponse('cars.xml')

if __name__ == '__main__':
    app.run_server(debug=True)