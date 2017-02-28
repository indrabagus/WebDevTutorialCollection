from BootStrap.models import CardMember
import random
from datetime import datetime
import time
listnama = [
    "Adriana C. Ocampo Uria",
    "Albert Einstein",
    "Anna K. Behrensmeyer",
    "Blaise Pascal",
    "Caroline Herschel",
    "Cecilia Payne-Gaposchkin",
    "Chien-Shiung Wu",
    "Dorothy Hodgkin",
    "Edmond Halley",
    "Edwin Powell Hubble",
    "Elizabeth Blackburn",
    "Enrico Fermi",
    "Erwin Schroedinger",
    "Flossie Wong-Staal",
    "Frieda Robscheit-Robbins",
    "Geraldine Seydoux",
    "Gertrude B. Elion",
    "Ingrid Daubechies",
    "Jacqueline K. Barton",
    "Jane Goodall",
    "Jocelyn Bell Burnell",
    "Johannes Kepler",
    "Lene Vestergaard Hau",
    "Lise Meitner",
    "Lord Kelvin",
    "Maria Mitchell",
    "Marie Curie",
    "Max Born",
    "Max Planck",
    "Melissa Franklin",
    "Michael Faraday",
    "Mildred S. Dresselhaus",
    "Nicolaus Copernicus",
    "Niels Bohr",
    "Patricia S. Goldman-Rakic",
    "Patty Jo Watson",
    "Polly Matzinger",
    "Richard Phillips Feynman",
    "Rita Levi-Montalcini",
    "Rosalind Franklin",
    "Ruzena Bajcsy",
    "Sarah Boysen",
    "Shannon W. Lucid",
    "Shirley Ann Jackson",
    "Sir Ernest Rutherford",
    "Sir Isaac Newton",
    "Stephen Hawking",
    "Werner Karl Heisenberg",
    "Wilhelm Conrad Roentgen",
    "Wolfgang Ernst Pauli"]


listtempat = ["Bandung","Jakarta","Surabaya","Medan","New York","London","Paris"]
listphoneprefix=["+62818","+62812","+62813"]
listalamat = [
    "Jalan Leumah Neundeut kav 30 blok E no 2",
    "Jalan Leumah Neundeut kav 30 blok D no 2",
    "Jalan Leumah Neundeut kav 31 blok A no 12",
    "Jalan Leumah Neundeut kav 31 blok A no 30",]


def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%Y-%m-%d', prop)    
    # return strTimeProp(start, end, '%m/%d/%Y %I:%M %p', prop)


def Generate(num):
    rand = random.Random()
    rand.seed(datetime.now().microsecond)    
    for i in range(num):
        rndid = 11*100*10000 + (rand.randint(0,99)*10000) + rand.randint(0,9999)
        rndphone = rand.choice(listphoneprefix) + str((rand.randint(0,9999)*10000)+(rand.randint(0,9999))) # 6281809518605
        retval = CardMember(identifier=rndid)
        retval.nama=rand.choice(listnama)
        retval.alamat = rand.choice(listalamat)
        retval.email = str(rndid) + "@xirkachipset.com"
        retval.tempat_lahir = rand.choice(listtempat)
        retval.tgl_lahir=(randomDate("1990-1-1","2000-1-1",random.random()))
        retval.phone = rndphone
        retval.save()
