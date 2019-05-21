import matplotlib
matplotlib.__version__'3.0.3'
import PIL
PIL.__version__'6.0.0'
import scipy
scipy.__version__'1.2.1' #importerar de funktioner som behövs för att det ska funka




from matplotlib import image as imgimage = img.imread('./banana1.jpg')
image.shape # Det manuella programmet som ska försöka att på ett simplare sätt avläsa bilder som att hitta bildens dominanta färg
(355, 355, 3) # Antalet pixlar bilden har och en 3:a som representerar att de 3 olika typerna av färgvärden (rgb)

%matplotlib inlinefrom matplotlib import pyplot as pltplt.imshow(image)
plt.show()

r = []
g = []
b = []for line in image:
for pixel in line:
temp_r, temp_g, temp_b = pixel
r.append(temp_r)
g.append(temp_g)
b.append(temp_b)


from mpl_toolkits.mplot3d import Axes3Dfig = plt.figure() #Koden för att 3d visualisera bildens färger (en 3d graf som visar r,g och b värdena på varje axel för att visualisera den vanligaste färgen)
ax = Axes3D(fig)
ax.scatter(r, g, b)
plt.show() #"Kommandot" som visar grafen

import pandas as pddf = pd.DataFrame({'red': r,
'blue': b,
'green': g})

from scipy.cluster.vq import whitendf['scaled_red'] = whiten(df['red'])
df['scaled_blue'] = whiten(df['blue'])
df['scaled_green'] = whiten(df['green'])
df.sample(n = 10)

from scipy.cluster.vq import kmeanscluster_centers, distortion = kmeans(df[['scaled_red', 'scaled_green', 'scaled_blue']], 2)

print(cluster_centers)
[[2.94579782 3.1243935 3.52525635]
[0.91860119 1.05099931 1.4465091 ]]



colors = []r_std, g_std, b_std = df[['red', 'green', 'blue']].std()for cluster_center in cluster_centers:
scaled_r, scaled_g, scaled_b = cluster_center
colors.append((
scaled_r * r_std / 255, # Delar färgen med 255 för att ge ett rgb-värde mellan 0 till 1
scaled_g * g_std / 255,
scaled_b * b_std / 255
))
plt.imshow([colors]) # Tar 0 till 1 värderna och genererar bildens "medelfärg"
plt.show()