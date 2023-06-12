import folium
from folium import plugins
import webbrowser
from tkinter import *
map_plot_antroute = folium.Map(location=[14.814349, -17.249890], zoom_start=4)
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
          [14.751544 , -17.396413],             #Pikine
          [14.7771207 , -17.390071],            #Guediawaye
          [14.716417 , -17.273844],             #Rufisque
          [14.7822567 , -17.311199],            #Keur Massar
          [14.4385618 , -16.2941072],           #Mbour
          [ 14.8110278 , -17.27780139121729],   #Tivaoune
          [14.69548 , -16.449262],              #Bambey
          [14.7971224 , -15.9066608],           #Mbacké
          [14.1263545 , -16.4674807],           #Foundiougne
          [14.8337008 , -15.5739878],           #Gossas
          [13,7486, -15,7824],                  #Nioro du Rip
          [13,4333, -15,5333],                  #Soma   
          [12,8051, -16,2346],                  #Bignona   
          ]                  

plugins.AntPath(route).add_to(map_plot_antroute)
for i in route:
    loc = i
    marker = folium.Marker(location = loc)
    marker.add_to(map_plot_antroute)
map_plot_antroute.save("C:\\Users\\HP\\Documents\\code_python\\myroute.html")
url = 'C:\\Users\\HP\\Documents\\code_python\\myroute.html'

fenetre = Tk()
fenetre.title('Dijkstra-Roads')
fenetre.geometry("500x500")
def open_browser(e):
    webbrowser.open_new_tab(url)

my_button = Button(fenetre, text="Find a easy way to travel", font=("Helvetica", 24), command= lambda: open_browser(1))
my_button.pack(pady=50)


fenetre.mainloop()
