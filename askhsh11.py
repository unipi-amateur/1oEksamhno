file = input("Enter file name: ")
f = open(file, "r", encoding="utf8")
text = f.read()
keys = ""
while (len(text) != 1):
    # Τα κλειδιά είναι πάντα με ",' και πίσω τους έχουν παντα {} ή ,
    #
    # Δε βρήκα πως να κανω μια εντολή να είναι πολλαπλές σειρές
    if ((text[0] + text[1]) == "{\"" or (text[0] + text[1]) == ",\"" or (text[0] + text[1]) == "{\'" or (text[0] + text[1]) == "{'"):
        x = text.find(":")
        y = text[:x]
        text = text[x:]
        # y[2:-1] ωστε να μην βάλω τα {' {" ,' ," και το τελευταιο στοιχειο
        # που δεν ειναι της λεξης
        keys += y[2:-1]
        keys += " "
    else:
        text = text[1:]
# Τη κάνω λίστα και μετά sort για ευκολία
teliko = keys.split()
teliko.sort(key=str.lower)
print(teliko)
plh8os = 0
max_Plh8os = 0
max_Key = ''
for i in range(len(teliko)):
    # Το πρώτο κλειδί
    if i == 0:
        plh8os = 1
    else:
        # Επόμενα κλειδιά
        #
        # Πρώτο if αν είναι ίδιο κλειδί με το προηγούμενο
        if teliko[i] == teliko[i-1]:
            plh8os += 1
        else:
            plh8os = 1
    # Εύρεση του max (αφότου έχει αλλάξει το πλήθος στη περίπτωση που άλλαξε
    # γράμμα)
    if max_Plh8os < plh8os:
        max_Plh8os = plh8os
        max_Key = teliko[i]
print('ΠΙΟ ΣΥΧΝΟ ΚΕΥ ΕΙΝΑΙ ΤΟ ', max_Key, 'με τοσες εμφανισεις ', max_Plh8os)
f.close()
