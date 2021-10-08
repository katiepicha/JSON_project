import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# ------------------------ US_fires_9_1 ---------------------------

infile = open('US_fires_9_1.json', 'r')

fire1_data = json.load(infile)

lats1, lons1, brights1 = [], [], []

for fires in fire1_data:
    if fires["brightness"] > 450:
        lat = fires["latitude"]
        lon = fires["longitude"]
        bright = fires["brightness"]
        lats1.append(lat)
        lons1.append(lon)
        brights1.append(bright)

print(lats1[:5])
print(lons1[:5])
print(brights1[:5])

data1 = [{
    'type': 'scattergeo',
    'lon': lons1,
    'lat': lats1,
    'marker': {
        'size': 20,
        'color': brights1,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'}
    }
}]

my_layout1 = Layout(title = 'US Fires - 9/1/2020 through 9/13/2020')

fig = {'data': data1, 'layout': my_layout1}

offline.plot(fig, filename = 'usfires1.html')


# ------------------------ US_fires_9_14 --------------------------

infile = open('US_fires_9_14.json', 'r')

fire2_data = json.load(infile)

lats2, lons2, brights2 = [], [], []

for fires in fire2_data:
    if fires["brightness"] > 450:
        lat = fires["latitude"]
        lon = fires["longitude"]
        bright = fires["brightness"]
        lats2.append(lat)
        lons2.append(lon)
        brights2.append(bright)

print(lats2[:5])
print(lons2[:5])
print(brights2[:5])

data2 = [{
    'type': 'scattergeo',
    'lon': lons2,
    'lat': lats2,
    'marker': {
        'size': 20,
        'color': brights2,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'}
    }
}]

my_layout2 = Layout(title = 'US Fires - 9/14/2020 through 9/20/2020')

fig = {'data': data2, 'layout': my_layout2}

offline.plot(fig, filename = 'usfires2.html')