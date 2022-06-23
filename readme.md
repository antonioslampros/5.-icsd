# Προηγμένα Θέματα Γλωσσών Προγραμματισμού Εργασία 3 (Ομαδική) Antonios Lampros 13100 Panagiotis Stasinos 16188 University of The Aegean
Στο πρώτο ερώτημα καλούμαστε να πάρουμε δεδομένα από μια ιστοσελίδα στην δικία μας περίπτωση από την "https://www.coindesk.com/price/bitcoin/"
Τα δεδομένα που πήραμε είναι τα εξής: 
 1) Από την αρχική σελίδα πήραμε τα πρώτα 5 κρυπτονομίσματα 
 2) Από κάθε κρυπτονόμισμα πήραμε μετά το όνομα του, τη τιμή του, τον όγκο συναλαγών ανά 24 ώρες, τη αλλαγή τιμής ανά 24 ώρες και το συνολικό market cap

Αφού πήραμε τα δεδομένα κάνοντας χρήση κανονικών εκφράσεων και την βιβλιοθήκη xpath 
πχ "doc.xpath('//h1[@class="typography__StyledTypography-owin6q-0 jZEoye long-title"]/text()')[0]" 
τα αποθυκέυσαμε σε ένα pandas dataframe για να τα κάνουμε εξαγωγή σε excel.
![alt text](https://github.com/antonioslampros/5.-icsd/blob/master/1.png)

Στο δεύτερο μέρος έπρεπε να ανοίξουμε το λογιστικό φύλλο που φτιάξαμε στο προηγούμενο ερώτημα και να φτίαξουμε ένα γράφημα με την βιβλιοθήκη "matplotlib"

![alt text](https://github.com/antonioslampros/5.-icsd/blob/master/plot.png)