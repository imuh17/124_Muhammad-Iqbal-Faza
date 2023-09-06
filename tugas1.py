"""
Program Menghitung Bangun Ruang!!!
1. Menghitung Volume Balok
2. Menghitung Volume Tabung
"""

print("""
!!!  Program Menghitung Volume Balok  !!!
""")
panjang = int(input("Masukkan Panjang Balok ;"))
lebar = int(input("Masukkan Lebar Balok ;"))
tinggi = int(input("Masukkan Tinggi Balok ;"))
volumeBalok = panjang * lebar * tinggi

print("Volume Balok Tersebut adalah", volumeBalok,"cm")

# Volume Tabung
print("""
!!!  Program Penghitung Volume Balok  !!!
""")
  
jari = float(input("Masukkan Jari-Jari Tabung:"))
tinggiTabung = float(input("Masukkan Tinggi Tabung :"))
phi = 3.14

volumeTabung = phi * jari **2 *tinggiTabung

print("Volume Tabung dengan jari-jari",jari,"dan tinggi", tinggi ,"adalah", volumeTabung, "cm") 