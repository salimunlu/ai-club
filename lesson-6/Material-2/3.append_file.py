with open("python_notes.txt", "a") as file:
    file.write("Python'da dosyalar ile çalışırken çalışma dizinini kontrol edin.\n")



file_name = "python_notes.txt"
f = open(file_name, "a")
f.write("Python'da birçok uygulama geliştirilebilir.\n")
f.close()

f.write("Python'da birçok uygulama geliştirilebilir.\n")