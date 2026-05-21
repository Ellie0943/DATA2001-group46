import requests
import pandas as pd

url = "https://maps.six.nsw.gov.au/arcgis/rest/services/public/NSW_POI/MapServer/0/query"

params = {
    "where": "1=1",
    "geometry": "151.05,-33.85,151.18,-33.74",
    "geometryType": "esriGeometryEnvelope",
    "spatialRel": "esriSpatialRelIntersects",
    "outFields": "*",
    "returnGeometry": "true",
    "f": "json"
}

all_features = []

offset = 0

batch_size = 1000

while True:

    params = {
        "where": "1=1",
        "geometry": "151.05,-33.85,151.18,-33.74",
        "geometryType": "esriGeometryEnvelope",
        "spatialRel": "esriSpatialRelIntersects",
        "outFields": "*",
        "returnGeometry": "true",
        "f": "json",
        "resultOffset": offset,
        "resultRecordCount": batch_size
    }

    response = requests.get(url, params=params)

    data = response.json()

    features = data.get("features", [])

    all_features.extend(features)

    print("offset:", offset, "records:", len(features))

    if len(features) < batch_size:
        break

    offset += batch_size




print(len(features))
print(features[0])

rows = []

for place in all_features:

    name = place['attributes']['poiname']

    x = place['geometry']['x']

    y = place['geometry']['y']

    rows.append(["Ryde", name, x, y])

df = pd.DataFrame(rows, columns=['sa4_name', 'name', 'x', 'y'])

print(df)

df.to_csv('ryde_poi.csv', index=False)

print("CSV saved")


poi_count = len(df)

summary = pd.DataFrame({
    "sa4_name": ["Ryde"],
    "poi_count": [poi_count]
})

print(summary)

summary.to_csv("ryde_poi_summary.csv", index=False)

print("Summary CSV saved")