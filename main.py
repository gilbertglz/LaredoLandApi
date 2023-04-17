from flask import Flask, jsonify, request
import pandas as pd
import urllib.parse

app = Flask(__name__)

@app.route('/Laredo/<Lot>/<Block>/<Subdivision>')
def hello(Lot, Block, Subdivision):
    df = pd.read_csv('LaredoLandDetailsClean.csv')
    filtered_df = df[(df['LOT'] == Lot) & (df['BLOCK'] == Block) & (df['SUBDIVISIO'] == Subdivision)]
    finalAddress = filtered_df['FULLADDRES'].values[0].strip()
    url_address = urllib.parse.quote_plus(finalAddress + ', Laredo, Texas')
    maps_url = f"https://www.google.com/maps/search/?api=1&query={url_address}"
    return jsonify({'FULL ADDRESS': finalAddress, 'gmapsUrl': maps_url})


if __name__ == '__main__':
    app.run(debug=True)
