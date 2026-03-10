import json

import geopandas as gpd
import pandas as pd
import pydeck as pdk
import streamlit as st

st.set_page_config(page_title="Carte des communes - pp_total_24", layout="wide")
st.title("Carte des communes et variable pp_total_24")


@st.cache_data
def load_datasets() -> gpd.GeoDataFrame:
	commune_maps = gpd.read_file("data/communes-1000m.geojson")
	data = pd.read_csv(
		"data/lovac-opendata-communes.csv",
		sep=";",
		encoding="latin1",
		dtype={"CODGEO_25": "string"},
		low_memory=False,
	)

	commune_maps["code"] = commune_maps["code"].astype(str).str.zfill(5)
	data["CODGEO_25"] = data["CODGEO_25"].astype(str).str.zfill(5)

	merged = commune_maps.merge(
		data[["CODGEO_25", "LIBGEO_25", "pp_total_24"]],
		left_on="code",
		right_on="CODGEO_25",
		how="left",
	)

	merged["pp_total_24"] = pd.to_numeric(merged["pp_total_24"], errors="coerce")
	merged["nom_commune"] = merged["LIBGEO_25"].fillna(merged["nom"])

	# Keep label points inside polygons to avoid labels being outside narrow communes.
	merged["label_point"] = merged.geometry.representative_point()
	merged["lon"] = merged["label_point"].x
	merged["lat"] = merged["label_point"].y

	return merged


def color_scale(value: float, vmin: float, vmax: float) -> list[int]:
	if pd.isna(value):
		return [200, 200, 200, 120]

	if vmax == vmin:
		ratio = 1.0
	else:
		ratio = float((value - vmin) / (vmax - vmin))

	ratio = max(0.0, min(1.0, ratio))
	r = int(230 - ratio * 200)
	g = int(245 - ratio * 170)
	b = int(255 - ratio * 140)
	return [r, g, b, 170]


gdf = load_datasets()

valid_values = gdf["pp_total_24"].dropna()
if valid_values.empty:
	st.error("Aucune valeur numérique disponible dans pp_total_24.")
	st.stop()

vmin = float(valid_values.min())
vmax = float(valid_values.max())
gdf["fill_color"] = gdf["pp_total_24"].apply(lambda v: color_scale(v, vmin, vmax))

geojson_data = json.loads(gdf.drop(columns=["label_point"]).to_json())

st.caption(
	"Chaque commune est colorée selon pp_total_24. Survolez la carte pour afficher le nom et la valeur."
)

show_labels = st.checkbox("Afficher les noms de communes (peut ralentir l'affichage)", value=False)
label_limit = st.slider("Nombre maximal de labels", min_value=100, max_value=2000, value=400, step=100)

layers = [
	pdk.Layer(
		"GeoJsonLayer",
		data=geojson_data,
		pickable=True,
		stroked=True,
		filled=True,
		extruded=False,
		line_width_min_pixels=0.2,
		get_line_color=[120, 120, 120, 60],
		get_fill_color="properties.fill_color",
	)
]

if show_labels:
	label_data = (
		gdf.dropna(subset=["pp_total_24"])
		.sort_values("pp_total_24", ascending=False)
		.head(label_limit)[["nom_commune", "lon", "lat"]]
	)

	layers.append(
		pdk.Layer(
			"TextLayer",
			data=label_data,
			pickable=False,
			get_position="[lon, lat]",
			get_text="nom_commune",
			get_color=[40, 40, 40, 180],
			get_size=11,
			size_units="pixels",
		)
	)

view_state = pdk.ViewState(latitude=46.6, longitude=2.3, zoom=5.1, min_zoom=4.3, max_zoom=12)

deck = pdk.Deck(
	layers=layers,
	initial_view_state=view_state,
	map_style="mapbox://styles/mapbox/light-v10",
	tooltip={
		"html": "<b>{nom_commune}</b><br/>Code INSEE: {code}<br/>pp_total_24: {pp_total_24}",
		"style": {"backgroundColor": "#ffffff", "color": "#222222"},
	},
)

st.pydeck_chart(deck, width="stretch")

st.write(
	f"Communes affichées: {len(gdf):,}".replace(",", " "),
	"|",
	f"pp_total_24 min: {int(vmin):,}".replace(",", " "),
	"|",
	f"pp_total_24 max: {int(vmax):,}".replace(",", " "),
)