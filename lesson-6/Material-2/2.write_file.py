# open("dosya_ismi", mode)
# mode: "r", "w"

with open("python_notes.txt", "w") as file:   # olmayan dosyayı oluşturur ve yazar.
    file.write("Python'da indentation önemlidir.\n")
    file.write("Python'da ':' önemlidir.\n")
    file.write("Python'da lütfen sınıfları büyük harfle başlatın.\n")

with open("python_notes.txt", "w") as file:   # var olan dosyanın üzerine yazar. (siler yazar)
    file.write("Blablabla\n")


file.write("abcde")   #ValueError: I/O operation on closed file.
