'''
ΑΣΚΗΣΗ 9
'''
import math
# File input
# Έβαλα encoding='utf8' επειδή μερικές φορές ανάλογα το κείμενο μου βγάζει
# 'charmap' codec can't decode byte 0x9d in position ....
f = input("Enter file name: ")
file = open(f, "r", encoding='utf8')
my_text = file.read()
# Πίνακας πλήθους για τα γράμματα
char_count = [0]*13
# Αρχικοποίηση συνολικού πλήθους μονών χαρακτήρων
length = 0
# Γράμμα γράμμα
for letter in my_text:
    num_ascii = ord(letter)
    # Έλεγχος αν έχει μονό ascii αριθμό
    if num_ascii % 2 == 1:
        # Έλεγχος αν έιναι κεφαλαίο,μικρό γράμμα ή σύμβολο(και δεν κανει τπτ).
        # Κάνω (num_ascii-65) // 2 ώστε ο ascii αριθμός να γίνει θέση του
        # πίνακα. Τα κεφαλαία και τα μικρά είναι στην ίδια θέση.
        if 65 <= num_ascii < 90:
            #  num_ascii >= 65 and num_ascii < 90
            char_count[(num_ascii-65) // 2] += 1
            length += 1
        elif 97 <= num_ascii < 122:
            # num_ascii >= 97 and num_ascii < 122
            char_count[(num_ascii-97) // 2] += 1
            length += 1
        else:
            pass
# Αρχείο χωρίς κανένα γράμμα με μονό ASCII αριθμό ή κενό αρχείο
if length == 0:
    print("Δεν υπάρχει γράμμα με μονό ASCII αριθμό!!")
else:
    # αρχείο έχει έστω ένα γράμμα με μονό ascii αριθμό
    for i in range(13):
        letter = chr(i*2+65)
        # Ποσοστό μονών γραμμάτων είναι το πλήθος του ενός γράμματος/ το
        # το σύνολο των μονών γραμμάτων
        pososto = round(char_count[i]/length*100)
        print(letter + ": " + "*" * math.ceil(pososto))
file.close()
