import tweepy
# Twitter API
auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")
K = tweepy.API(auth)
eisodos = input("Δ΄ώσε όνομα του χρήστη στα αγγλικά:")
stuff = K.user_timeline(eisodos, count=10, include_rts=True)
# Παίρνω τα tweets και τα βάζω όλα σε λίστα
Lista = []
y = ""
for info in stuff[:]:
    for z in str(info.text):
        if z == " ":
            Lista.append(y)
            y = ""
        else:
            y = y+z
# Κάνω Bubble Sort για να ταξινομήσω την λιστα σε φθίνουσα σειρά
Length = len(Lista)
for i in range(1, Length):
    for x in range(Length-1, i-1, -1):
        if len(Lista[x]) < len(Lista[x-1]):
            # Αντιμετάθεση
            Lista[x], Lista[x-1] = Lista[x-1], Lista[x]
# Κοιτάω αν έχει κάποιο special χαρακτήρα που τον αποθώ
Num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
for w in range(Length-1, -1, -1):
    if ("https" in Lista[w]) or ("#" in Lista[w]) or ("\\" in Lista[w]) or ("/" in Lista[w]) or ("@" in Lista[w]) or ("\"" in Lista[w]) or ("\'" in Lista[w]) or ("_" in Lista[w]) or ("." in Lista[w]) or ("," in Lista[w]) or (":" in Lista[w]) or ("!" in Lista[w]) or ("-" in Lista[w]):
        Lista.pop(w)
for w in range(Length-1, -1, -1):
    for y in range(10):
        if Num[y] in Lista[w]:
            Lista.pop(w)
# Έξοδος
print("Οι μακρύτερες λέξεις είναι:", Lista[-5], Lista[-4], Lista[-3], Lista[-2], Lista[-1])
print("Οι μικρότερες λέξεις είναι:", Lista[0], Lista[1], Lista[2], Lista[3], Lista[4])
