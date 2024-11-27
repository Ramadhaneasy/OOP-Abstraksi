from abc import ABC, abstractmethod

# Membuat kelas abstrak
class Kendaraan(ABC):
    @abstractmethod
    def bergerak(self):
        pass  # Metode abstrak (harus diimplementasikan oleh subclass)

# Kelas Turunan
class GamingLaptop(Kendaraan):
    def bergerak(self):
        return "Gaming laptop digunakan untuk bermain game berat."

class Ultrabook(Kendaraan):
    def bergerak(self):
        return "Ultrabook digunakan untuk pekerjaan ringan dan portabilitas tinggi."

# Penggunaan
gaming_laptop = GamingLaptop()
ultrabook = Ultrabook()

print(gaming_laptop.bergerak())  # Output: Gaming laptop digunakan untuk bermain game berat.
print(ultrabook.bergerak())  # Output: Ultrabook digunakan untuk pekerjaan ringan dan portabilitas tinggi.
