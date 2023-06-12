from pyroutelib3 import Router # Import the router
import folium
import os
import webbrowser
m = folium.Map(location=[14.814349, -17.249890], zoom_start=15)
coord_depart = [14.693425 , -17.447938]
coord_arrive = [14.7948093 , -16.9529272]

folium.Marker(location=coord_depart, popup="Départ").add_to(m)
folium.Marker(location=coord_arrive, popup="Arrivé").add_to(m)
router = Router("car") # Initialise it

start = router.findNode(14.693425 , -17.447938) # Find start and end nodes
end = router.findNode(14.7948093 , -16.9529272)

status, route = router.doRoute(start, end) # Find the route - a list of OSM nodes

if status == 'success':
    routeLatLons = list(map(router.nodeLatLon, route)) # Get actual route coordinates
#print(routeLatLons)

for coord in routeLatLons:
    coord = list(coord)
    folium.CircleMarker(coord,radius = 3,fill=True, color='red' ).add_to(m)

folium.PolyLine(routeLatLons, color="blue", weight=2.5, opacity=1).add_to(m)

#fichier_carte = 'C:\\Users\\HP\\Documents\\code_pythonroute.html'
m.save("C:\\Users\\HP\\Documents\\code_pythonroute.html")
url = 'C:\\Users\\HP\\Documents\\code_pythonroute.html'
webbrowser.open_new_tab(url)

# ouvrir le fichier dans le navigateur
#rep_cour = os.getcwd()
#fichier = 'Edge file://'+rep_cour +'/'+ fichier_carte
#os.popen(fichier)