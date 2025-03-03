#imports the matplotlib libray to show the data graphicaly 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg #for the image

# This creates the class and the contented within
class basic:
    def __init__(self, direction, strength, range, heading, tide, tempW, tempA):
        self.direction = direction
        self.strength = strength
        self.range = range
        self.heading = heading
        self.tide = tide
        self.tempW = tempW
        self.tempA = tempA

# This simmulates data
boat1 = basic("NW", "17.2 kn", "18.1 - 19.2 kn", "Close-Reach", "Low : 4.59 ft", "45.5 F", "34 F")

# Creates a figure for the data and image
fig, (ax_image, ax_plot) = plt.subplots(2, 1, figsize=(8, 10), gridspec_kw={'height_ratios': [1, 4]})

# Adds title / heading data to image
fig.suptitle('Headding: Close-Reach', fontsize=16, fontweight='bold')
#shows the image in the first figure
img = mpimg.imread('sailingchart.png')
ax_image.imshow(img)
ax_image.axis('off') 

# Adds the data and sytles it 
#HCI: Color was used to help group together simmilar types of data. Bellow all data associated with wind is blue and phsyically seperated from the 
#other data to futher show its distinct type
ax_plot.text(0.5, 0.9, f"Wind", fontsize=16, fontweight='bold', color='#0E01A2', ha='center', va='center')
ax_plot.text(0.5, 0.8, f"Direction: {boat1.direction}", fontsize=16, fontweight='bold', color='#0E01A2', ha='center', va='center')
ax_plot.text(0.5, 0.7, f"Strength: {boat1.strength}", fontsize=16, fontweight='bold', color='#0E01A2', ha='center', va='center')
ax_plot.text(0.5, 0.6, f"Puff: {boat1.range}", fontsize=16, fontweight='bold', color='#0E01A2', ha='center', va='center')
#HCI: The Starbord data point is the most important data point shown. It keeps the sailors from hitting one another when on differnet tacks
#This data point was made to have a different layout to help it stand out from all other data points and be eye catching to make the sailor 
#instictivly look at it
ax_plot.text(0.5, 0.5, f"Starbord", fontsize=16, fontweight='bold', color='white', ha='center', va='center', 
             bbox=dict(facecolor='#1C5505', edgecolor='black', boxstyle='round,pad=0.5'))
#HCI: This data is also physically group together as is locations are offset from the wind data by .1
#This helps the sailor use the negative space to see the data quicker as there are  'landmarks' for the eye to look for
#the color of this data is also changed to help futher make it distinct
ax_plot.text(0.5, 0.3, f"Temp (Water): {boat1.tempW}", fontsize=16, fontweight='bold', color='#1C5505', ha='center', va='center')
ax_plot.text(0.5, 0.2, f"Temp (Air): {boat1.tempA}", fontsize=16, fontweight='bold', color='#1C5505', ha='center', va='center')
ax_plot.text(0.5, 0.1, f"Tide: {boat1.tide}", fontsize=16, fontweight='bold', color='#A50A0B', ha='center', va='center')
ax_plot.axis('off')
#HCI:Here I used highgh text to background contrast to make the text readable and a large font (16 p Bold)
#Red Contrast Ratio: 7.93:1 / Blue Contrast Ratio:  13.59:1 / Green Contast Ratio: 8.93:1 (All contrasts are higher than the required 4.5:1)

#plt.tight_layout() ensures that elements like labels and axis dont get cut off
#HCI: This is connected to HCI as ensuring the spacing remains uniform for all elements helps to not have 
#any elements stand out from one another and look more important when they are not
plt.tight_layout()  
# Shows the plot
plt.show()

