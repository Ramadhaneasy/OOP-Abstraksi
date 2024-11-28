from abc import ABC, abstractmethod

# Membuat kelas abstrak
class Laptop(ABC):
    @abstractmethod
    def spesifikasi(self):
        pass  # Metode abstrak pertama (harus diimplementasikan oleh subclass)

    @abstractmethod
    def harga(self):
        pass  # Metode abstrak kedua (harus diimplementasikan oleh subclass)

# Kelas Turunan
class GamingLaptop(Laptop):
    def spesifikasi(self):
        return "Gaming laptop memiliki spesifikasi tinggi untuk menjalankan game berat."

    def harga(self):
        return "Harga gaming laptop berkisar antara 15 juta hingga 50 juta rupiah."

class Ultrabook(Laptop):
    def spesifikasi(self):
        return "Ultrabook dirancang untuk portabilitas dan efisiensi daya."

    def harga(self):
        return "Harga ultrabook berkisar antara 10 juta hingga 30 juta rupiah."

# Penggunaan
gaming_laptop = GamingLaptop()
ultrabook = Ultrabook()

print(gaming_laptop.spesifikasi())  # Output: Gaming laptop memiliki spesifikasi tinggi untuk menjalankan game berat.
print(gaming_laptop.harga())       # Output: Harga gaming laptop berkisar antara 15 juta hingga 50 juta rupiah.

print(ultrabook.spesifikasi())     # Output: Ultrabook dirancang untuk portabilitas dan efisiensi daya.
print(ultrabook.harga())           # Output: Harga ultrabook berkisar antara 10 juta hingga 30 juta rupiah.
