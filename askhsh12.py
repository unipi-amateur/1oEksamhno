"""
ΑΣΚΗΣΗ 12
"""
# File input
f = input("Enter file name: ")
file = open(f, "r+", encoding='utf8')
my_text = file.read()
length = len(my_text)
# Φτιάχνω λίστα που θα έχει τους αντικατοπτρικόυς χαρακτήρες και αρχικοποιώ
# έναν δείκτη
copyLista = [""] * length
i = 0
# Διαβάζει χαρακτήρα-χαρακτήρα και βάζει στη λίστα τον αντικατοπτρικό
for letter in my_text:
    print(letter)
    num_ascii = ord(letter)
    katoptr = 128 - num_ascii
    copyLista[i] = chr(katoptr)
    i += 1
# Φτιάχνω string για να περιέχει τους αντικατοπτρικούς και να μην είναι λίστα
telikhLista = ""
for x in range(length):
    telikhLista = telikhLista + copyLista[x]
# Αντιστρέφω το string για το επιθυμητό αποτέλεσμα και το εμφανίζω
#
# NOTE!! Για κάποιο λόγο αν υπάρχουν συγκεκριμένα μικρά γράμματα στο αρχείο
# δεν εμφανίζει τίποτα ο διερμηνευτής. Ούτε το αποτέλεσμα που θέλουμε (string)
# Ούτε καν κάποιο error. Απλά τελειώνει το πρόγραμμα (μάλλον αντικανονικά)
# και δεν εμφανίζει τίποτα. Ακόμα και αν υπάρχει κάποιο
# print() πριν βάλουμε τους αντικατοπτρικούς.
telikhLista = telikhLista[::-1]
print(telikhLista)
file.close()
