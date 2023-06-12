from geopy.geocoders import Nominatim
#from geopy import distance
import folium
import webbrowser
region = ["Dakar", "Thies", "Diourbel", "Kaolack", "Fatick", "Kaffrine", "Louga", "Matam", "Tambacounda", "Kédougou", "Kolda", "Ziguinchor", "Sédhiou"]


city_liaison = [["Dakar", "Pikine", "Guediawaye", "Rufisque", "Keur Massar"],
                ["Thies", "Mbour", "Tivaoune"],
                ["Diourbel", "Bambey", "Mbacké"],
                ["Fatick", "Foundiougne","Gossas"],
                ["Kaolack", "Guingueneo", "Nioro Du Rip"],
                ["Kaffrine", "Birkelane", "Malem Hodar", "Koungheul"],
                ["Louga", "Kébémer"],
                ["Matam", "Kanel", "Ranerou"],
                ["Tambacounda", "Koumpentoum", "Goudiry", "Bakel"],
                ["Kédougou", "Sareya", "Salemata"],
                ["Kolda", "Vélingara", "Medina Yoro Foula"],
                ["Ziguinchor", "Oussouye", "Bignona",],  
                ["Sédhiou", "Goudomp", "Bounkiling"],

]
# On range les régions dans un listes nommé region
"""region = []
for i in range(0, len(city_liaison)):
    region += [city_liaison[i][0]]"""
# On recupére les coordonnées des régions
geolocator = Nominatim(user_agent="")
Coord = []
for i in region:
    location = geolocator.geocode(i)
    Coord += [[location.latitude, location.longitude]]
"""print(i, "a pour coordonnée :", Coord)
    print()
    print()
    print("------------------------------------------------------------------------------")
    print()"""
# Calcul de distance entre deux villes avec le module distance de geopy
"""
dakar = geolocator.geocode(region[0])
sedhiou = geolocator.geocode(region[13])
ville1 = (dakar.latitude, dakar.longitude)
ville2 = (sedhiou.latitude, sedhiou.longitude)
print("*************************************************************************")
print()
print(distance.distance(ville1, ville2).km)

"""

#Création de ma carte
my_map = folium.Map(location=[14.814349, -17.249890], zoom_start=5)
k=0
# Déssiner le graphe avec les coordonnées des régions
for each in Coord:
    folium.RegularPolygonMarker(location=each, popup=region[k], fill_color ='blue', number_of_sides=10, radius=10).add_to(my_map)
    k+=1

# Nous allons maintenant implémenter les différents liaisons dans notre carte

for i in city_liaison:
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(api_key='AIzaSyDkF6vCarqca4ft4LVAQn2uqf1li-cal_8')
    Coordonnees=[]
    location = geolocator.geocode(i[0])
    Coordonnees += [[location.latitude, location.longitude]]
    for k in range(1, len(i)):
        from geopy.geocoders import Nominatim
        geolocator = Nominatim(api_key='AIzaSyDkF6vCarqca4ft4LVAQn2uqf1li-cal_8')
        location = geolocator.geocode(i[k])
        Coordonnees += [[location.latitude, location.longitude]]
        folium.PolyLine(Coordonnees, color="green", weight=2.5, opacity=1).add_to(my_map)
        Coordonnees = [Coordonnees[0]]

my_map.save("C:\\Users\\HP\\Documents\\code_python\\macarte1.html")
url = 'C:\\Users\\HP\\Documents\\code_python\\macarte1.html'
webbrowser.open_new_tab(url)