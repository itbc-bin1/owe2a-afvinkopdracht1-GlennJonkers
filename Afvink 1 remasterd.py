# Naam:     Glenn Jonkers
# Datum:    17-11-17
# Versie:   1.3

def main():
    try:
        bestands_naam = "alpaca.fna"#"alpaca.fna"
        headers, seqs = lees_inhoud(bestands_naam)              #Lees het bestand in en import de lijsten
        print(len(headers),len(seqs))
        zoekwoord = (input("Geef een zoekwoord op: "))
        if zoekwoord == '':
            print(" Er was geen woord opgegeven")
        for i in range(len(headers)):
            if zoekwoord in headers[i]:
                print("Header:",headers[i])
                check_is_dna = is_dna(seqs[i])
                if check_is_dna:
                    print("Sequentie is DNA")
                    knipt(seqs[i])
                else:
                    print("Sequentie is geen DNA. Er is iets fout gegaan.")
                #raise TypeError
    except UnboundLocalError:
        print("File Not Found")
    except KeyboardInterrupt :
        print("Gestopt door User")
    except AssertionError:
        print("Het is geen Fasta Bestand")
    except UnboundLocalError:
        print("variabel probleem")
    except TypeError:
        print("type error")

def lees_inhoud(bestands_naam):
    bestand = open(bestands_naam)
    if bestands_naam[0][0] == '>':
        raise AssertionError
    headers = []
    seqs = []
    seq = ""
    for line in bestand:
        line=line.strip()
        if ">" in line:
            if seq != "":
                seqs.append(seq)
                seq = ""
            headers.append(line)
        else:
            seq += line.strip()
    seqs.append(seq)
       #print("Dit bestand kon niet gevonden worden")
    return headers, seqs
                
def is_dna(seq):
    dna = False
    a = seq.count("A")
    t = seq.count("T")
    c = seq.count("C")
    g = seq.count("G")
    total = a + t + c + g
    if total == len(seq):
        dna = True
    return dna 

def knipt(alpaca_seq):
    bestand = open("enzymen.txt")
    for line in bestand:
        naam, seq = line.split(" ")
        seq = seq.strip().replace("^","")
        if seq in alpaca_seq:
            print(naam, "knipt in sequentie")
main() 
