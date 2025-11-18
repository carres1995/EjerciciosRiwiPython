"""1. Sistema de Biblioteca Virtual
Descripción:
Crea un programa que permita gestionar una pequeña biblioteca.

Debe permitir:

Ver los libros disponibles.
Agregar nuevos libros.
Prestar libros (cambiar su estado a “prestado”).
Devolver libros.
Ver el historial de préstamos."""

def main():
    while True:
        print("1. Add new books")
        print("2. View books")
        print("3. Books loans")
        print("4. View books loans")
        print("5. Exit")
        try:
            option=int(input("\nEscoge una opcion: "))
        except ValueError:
            print("Option not validate")  
            continue

        if option == 1:
            nombre=input("\nEnter book name: ")
            autor=input("Enter autor name: ")
            editor= input("Enter editorial ")
            createBooks(nombre,autor,editor)
        elif option == 2:
            readBooks()
        elif option == 3:
            menuLedingBooks()
        elif option == 4:
            historialBook()
        elif option == 5:
            print("\nThanks you for logging!")
            break
        else:
            print("option not validate.\n")

libros= []

def createBooks(nombre, autor, editor):
    id=len(libros)+1
    
    libros.append({
        "id":id,
        "name": nombre,
        "author":autor,
        "editor":editor,
        "state":"available"
    })
    return print(f"\nID: {id} | Book: {nombre} | Author | {autor} | Editor: {editor}\n")

def readBooks():
    if not libros:
        print("Empty list")
    else:
        print(f"\n------------------------------BOOKS LIST------------------------------------------------")
        for i in libros:
            print(f"| ID: {i["id"]:5} | Book: {i["name"]:15} | Author | {i["author"]:15} | Editor: {i["editor"]:15} | State: {i["state"]:15} |")
        print("------------------------------------------------------------------------------------------\n")  
historial=[]

def menuLedingBooks():
    while True:
        print("1. Leding Book")
        print("2. Return book")
        print('3. Exit')
        try:
            option=int(input("\nEscoge una opcion: "))
        except ValueError:
            print("Option not validate")  
            continue
        if option == 1:
            readBooks()
            num=int(input('Enter id book: '))
            lendBook(num)
        elif option == 2:
            readBooks()
            num=int(input('Enter id book: '))
            returnBook(num)
        elif option == 3:
            break
        else:
            print('option not validate.\n')   

def historialBook():
    if not historial:
        print("Empty list")
        
    print(f"\n------------------------------HISTORY OF THE BOOKS------------------------------------------------")    
    for h in historial:
        print(f'| ID: {h["id_libro"]:5} | Book: {h["name"]:15} | State | {h["state"]:15} ')
    print("------------------------------------------------------------------------------------------\n")    
def lendBook(id:int):
    if not libros:
        print('Empty list')
    for l in libros:    
        if id == l['id']:
            if l['state'] == 'borrowed':
                print("Book is already on loan")
                return
            l['state']='borrowed'
            print(f'Book {l['name']} succesfully borrowed')
            historial.append({
                'id_libro':l['id'],
                'name':l['name'],
                'state':'borrowed'
            })   
            return 
    print('id not found')    
        
def returnBook(id:int):
    if not libros:
        print('Empty list')
    for h in libros:
        if id == h['id']:
            if h['state'] == 'available':
                print('The book is not borrowed')
            h['state'] = 'available'
            historial.append({
                'id_libro':h['id'],
                'name':h['name'],
                'state':'available'
            }) 
            return
    print('ID not found')       
   
    

if __name__=="__main__":
    main()

