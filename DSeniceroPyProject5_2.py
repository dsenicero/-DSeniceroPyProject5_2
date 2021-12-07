import folium
import webbrowser

#Creation of map with the focus of the Waco TSTC
dSeniceroMap = folium.Map(location=[31.64, -97.08], zoom_start = 12)

#circle marker with home campus and waco
folium.CircleMarker(location=[31.55, -97.14], radius = 500, popup="Waco").add_to(dSeniceroMap)

#Marker - Waco
folium.Marker([31.55, -97.14], popup="Waco").add_to(dSeniceroMap)

#Marker - TSTC Waco Campus
folium.Marker([31.64, -97.08], popup="Waco Home TSTC Campus").add_to(dSeniceroMap)

#Marker - State Capitol
folium.Marker([30.27, -97.74], popup="State Capitol, Austin, TX").add_to(dSeniceroMap)

#Marker - TSTC San Anonio Campus
folium.Marker([30.33, -97.61], popup="San Antonio TSTC Campus").add_to(dSeniceroMap)

#TSTC home campus to your hometown
folium.PolyLine(locations=[(31.64, -97.08), (31.55, -97.14)], line_opacity=.6).add_to(dSeniceroMap)

#your hometown to the capitol building
folium.PolyLine(locations=[(31.55, -97.14), (30.27, -97.74)], line_opacity=.6).add_to(dSeniceroMap)

#the capitol building and ending at the second TSTC campus
folium.PolyLine(locations=[(30.27, -97.74), (30.33, -97.61)], line_opacity=.6).add_to(dSeniceroMap)

#Save map to file
dSeniceroMap.save("DSeniceroMap.html")

#open in browser
webbrowser.open("DSeniceroMap.html")