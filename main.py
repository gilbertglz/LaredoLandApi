from flask import Flask, jsonify, request
import pandas as pd
app = Flask(__name__)

@app.route('/api/<Lot>/<Block>/<Subdivision>')
def hello(Lot, Block,Subdivision):
    df = pd.read_csv('LaredoLandDetailsClean.csv')
    filtered_df = df[(df['LOT'] == Lot) & (df['BLOCK'] == Block) & (df['SUBDIVISIO'] == Subdivision)]
    return jsonify({'FULLADDRESS': filtered_df['FULLADDRES'].values[0].strip()})

if __name__ == '__main__':
    app.run(debug=True)
