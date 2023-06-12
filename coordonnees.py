from geopy.geocoders import Nominatim
import folium
import webbrowser

region = ["Dakar",
          "Thies", 
          "Diourbel", 
          "Kaolack", 
          "Fatick", 
          "Kaffrine", 
          "Louga", 
          "Matam", 
          "Tambacounda", 
          "Kédougou", 
          "Kolda", 
          "Ziguinchor", 
          "Sédhiou"
          ]
liaison = [["Dakar", "Pikine", "Guediawaye", "Rufisque", "Keur Massar"],
                ["Thies", "Mbour", "Tivaoune"],
                ["Diourbel", "Bambey", "Mbacké"],
                ["Fatick", "Foundiougne","Gossas"],
                ["Kaolack", "Guingueneo", "Nioro Du Rip"],
                ["Kaffrine", "Birkelane", "Malem Hodar", "Koungheul"],
                ["Louga", "Kébémer"],
                ["Saint-Louis", "Dagana", "Podor"],
                ["Matam", "Kanel", "Ranerou"],
                ["Tambacounda", "Koumpentoum", "Goudiry", "Bakel"],
                ["Kédougou", "Sareya", "Salemata"],
                ["Kolda", "Vélingara", "Medina Yoro Foula"],
                ["Ziguinchor", "Oussouye", "Bignona",],  
                ["Sédhiou", "Goudomp", "Bounkiling"],

]
Coord = []
geolocator = Nominatim(user_agent="Microsoft Edge")
for i in region:
    location = geolocator.geocode(i)
    Coord += [[location.latitude, location.longitude]]
    #print(i, " a pour coordonnées : ", location.latitude, ",", location.longitude)
    #print()
    #print("***************************************************************************")

my_map = folium.Map(location=[14.814349, -17.249890],zoom_start=6)
k = 0
for each in Coord:
    folium.Marker(location=each, popup=region[k]).add_to(my_map);
    k+=1

for i in region:
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent="Microsoft Edge")
    location = geolocator.geocode(i)
    Coord += [[location.latitude,location.longitude]]
    folium.PolyLine(Coord, color="blue", weight=3, opacity=1).add_to(my_map)


my_map.save("C:\\Users\\HP\\Documents\\code_python\\macarte1.html")
url = 'C:\\Users\\HP\\Documents\\code_python\\macarte1.html'
webbrowser.open_new_tab(url)
