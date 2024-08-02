import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image

# GIF dosyasının yolu
gif_path = r'C:\Users\USER\Desktop\smtgif.gif'

# Matplotlib figürü oluştur
fig = plt.figure()

# GIF dosyasını aç
gif = Image.open(gif_path)

# GIF dosyasındaki her kareyi ekle
ims = []
try:
    while True:
        im = plt.imshow(gif.copy(), animated=True)
        ims.append([im])
        gif.seek(gif.tell() + 1)
except EOFError:
    pass

# Animasyonu oluştur
ani = animation.ArtistAnimation(fig, ims, interval=100, blit=True, repeat_delay=1000)

# Animasyonu göster
plt.show()
