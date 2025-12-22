#!/usr/bin/env python3
"""
Script interattivo per visualizzare le informazioni personali
"""

def mostra_menu():
    """Mostra il menu delle opzioni disponibili"""
    print("\n" + "="*50)
    print("Informazioni Personalizzate - Sistema Interattivo")
    print("="*50)
    print("1. Presentazione personale")
    print("2. Interessi")
    print("3. Attività di studio")
    print("4. Esperienze formative")
    print("5. Collaborazioni")
    print("6. Contatti")
    print("7. Mostra tutte le informazioni")
    print("0. Esci")
    print("="*50)

def mostra_info(opzione):
    """Mostra le informazioni specifiche in base all'opzione selezionata"""
    info = {
        1: {
            "titolo": "Presentazione Personale",
            "contenuto": [
                "👋 Ciao, sono @GPuntobit",
                "📍 Vivo nella città metropolitana di Bologna"
            ]
        },
        2: {
            "titolo": "Interessi",
            "contenuto": [
                "👀 Sono interessato a:",
                "   • Sviluppo di giochi (CSharp)",
                "   • Progettazione web (Ruby on Rails)",
                "   • Intelligenza Artificiale (Ruby)"
            ]
        },
        3: {
            "titolo": "Attività di Studio",
            "contenuto": [
                "📖 Attualmente sto imparando ProLog",
            ]
        },
        4: {
            "titolo": "Esperienze Formative",
            "contenuto": [
                "🌱 Ho completato il corso Full-Stack Web Developer presso Refresh Academy",
                "📅 Il corso è iniziato alla fine di gennaio 2025"
            ]
        },
        5: {
            "titolo": "Collaborazioni",
            "contenuto": [
                "💞 Cerco collaborazioni attraverso stage per migliorare le mie competenze"
            ]
        },
        6: {
            "titolo": "Contatti",
            "contenuto": [
                "📫 Puoi contattarmi tramite LinkedIn:",
                "   www.linkedin.com/in/gabriel-schipor"
            ]
        }
    }
    
    if opzione == 7:  # Mostra tutte le informazioni
        print("\n" + "="*50)
        print("TUTTE LE INFORMAZIONI")
        print("="*50)
        for key in sorted(info.keys()):
            print(f"\n{info[key]['titolo']}:")
            print("-" * len(info[key]['titolo']) + "-")
            for riga in info[key]['contenuto']:
                print(f"  {riga}")
        print("\n" + "="*50)
    elif opzione in info:
        print(f"\n{info[opzione]['titolo']}:")
        print("-" * len(info[opzione]['titolo']) + "-")
        for riga in info[opzione]['contenuto']:
            print(f"  {riga}")
    else:
        print("\nOpzione non valida!")

def main():
    """Funzione principale dello script interattivo"""
    print("Benvenuto nel sistema interattivo per visualizzare le informazioni personali!")
    
    while True:
        mostra_menu()
        try:
            scelta = input("\nSeleziona un'opzione (0-7): ").strip()
            
            if scelta == '0':
                print("\nGrazie per aver utilizzato il sistema interattivo. Arrivederci! 👋")
                break
            elif scelta.isdigit() and 1 <= int(scelta) <= 7:
                mostra_info(int(scelta))
                
                # Chiedi se l'utente vuole continuare
                continua = input("\nVuoi vedere altre informazioni? (s/N): ").strip().lower()
                if continua not in ['s', 'si', 'y', 'yes']:
                    print("\nGrazie per aver utilizzato il sistema interattivo. Arrivederci! 👋")
                    break
            else:
                print("\nOpzione non valida! Inserisci un numero da 0 a 7.")
                
        except KeyboardInterrupt:
            print("\n\nInterruzione ricevuta. Uscita dal programma... 👋")
            break
        except Exception as e:
            print(f"\nSi è verificato un errore: {e}")

if __name__ == "__main__":
    main()