def calculate_notes(line):
    line = line[:-1]
    list = line.split(':')
    
    studentName = list[0]
    notes = list[1].split(',')

    note1 = int(notes[0])
    note2 = int(notes[1])
    note3 = int(notes[2])

    avg = (note1+note2+note3)/3

    if avg>=90:
        char = "AA"
    elif 85<=avg<90:
        char = "BA"
    elif 80<=avg<85:
        char = "BB"
    elif 75<=avg<80:
        char = "CB"
    elif 70<=avg<75:
        char = "CC"
    elif 65<=avg<70:
        char = "DC"
    elif 60<=avg<65:
        char = "DD"
    elif 50<=avg<60:
        char = "FD"
    else:
        char = "FF"

    return studentName + ": " + "Average Notes: " + str(avg) +" "+ char +"\n"

def avg_show():
    with open ("sinav_notlari.txt","r",encoding="utf-8") as file:
        for line in file:
            print(calculate_notes(line))

def insert_note():
    name = input('Student Name: ')
    last_name = input('Student LastName: ')
    note_1 = input('Student note 1: ')
    note_2 = input('Student note 2: ')
    note_3 = input('Student note 3: ')
    
    with open ("sinav_notlari.txt","a",encoding="utf-8") as file:
        file.write(name+' '+last_name+': '+note_1+','+note_2+','+note_3+"\n")
def save():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        list = []
        for i in file:
            list.append(calculate_notes(i))

        with open("sonuclar.txt","w",encoding="utf-8") as file2:
            for i in list:
                file2.write(i)

while True:
    operation = input('1- Show notes\n2- Insert Note\n3- Save Notes\n4- Quit\n')

    if operation == '1':
        avg_show()
    elif operation == '2':
        insert_note()
    elif operation == '3':
        save()
    elif operation == '4':
        break

        