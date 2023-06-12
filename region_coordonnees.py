from geopy import Nominatim
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
          "Sédhiou",
          "Pikine",
          "Guediawaye", 
          "Rufisque", 
          "Keur Massar",
          "Mbour", 
          "Tivaoune",
          "Bambey", 
          "Mbacké",
          "Foundiougne", 
          "Gossas",
          "Guingueneo", 
          "Nioro Du Rip",
          "Birkelane", 
          "Malem Hodar", 
          "Koungheul",
          "Kébémer",
          "Dagana", 
          "Podor",
          "Kanel", 
          "Ranerou",
          "Koumpentoum", 
          "Goudiry", 
          "Bakel",
          "Sareya", 
          "Salemata",
          "Vélingara", 
          "Medina Yoro Foula",
          "Oussouye", 
          "Bignona",
          "Goudomp", 
          "Bounkiling"
          ]

Coord = []
geolocator = Nominatim(user_agent="Microsoft Edge")
for i in region:
    location = geolocator.geocode(i)
    Coord += [[location.latitude, location.longitude]]
    print(i, " a pour coordonnées : ", location.latitude, ",", location.longitude)
    print()
    print("***************************************************************************")