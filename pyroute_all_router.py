from pyroutelib3 import Router
import folium
import os

route = [[14.693425 , -17.447938],              #Dakar
          [14.7948093 , -16.9529272],           #Thies
          [16.0179, -16.4896],                  #Saint-Lious
          [14.7043898 , -16.0511737],           #Diourbel
          [14.04807735 , -16.015508291809287],  #Kaolack
          [13.9406041 , -16.4024021],           #Fatick
          [14.2824927 , -15.0247364],           #Kaffrine
          [15.2401304 , -15.3441834],           #Louga
          [15.0028849 , -13.9240088],           #Matam
          [13.8301533 , -13.0891759],           #Tambacounda
          [12.885677300000001 , -12.286363169419786],   #kédougou
          [13.1291507 , -14.418147374323599],   #Kolda
          [12.5634929 , -16.2724609],           #Ziguinchor
          [12.9102548 , -15.55298390097876],    #Sédhiou
          ]      
m = folium.Map(location=[45.5236, -122.6750], zoom_start=6)

# marquer les villes
for i in route:
    loc = i
    marker = folium.Marker(location = loc)
    marker.add_to(m)



def findAway(dico):
    router = Router("car")
    coord_depart = []
    coord_arrive = []
    for i in dico:
        coord_depart = i
        for j in dico:
            coord_depart = i
            coord_arrive = j
            start = router.findNode(coord_depart[0], coord_depart[1])
            end = router.findNode(coord_arrive[0], coord_arrive[1])
            status, route = router.doRoute(start, end)
            if status == 'success':
                routeLatLons = list(map(router.nodeLatLon, route))
            print(routeLatLons)
            for coord in routeLatLons:
                coord = list(coord)
                folium.CircleMarker(coord,radius = 3,fill=True, color='red' ).add_to(m)

            folium.PolyLine(routeLatLons, color="blue", weight=2.5, opacity=1).add_to(m)

    fichier_carte = 'routage.html'
    m.save(fichier_carte)
    rep_cour = os.getcwd()
    fichier = 'Edge file://'+rep_cour +'/'+ fichier_carte
    os.popen(fichier)

findAway(route)
