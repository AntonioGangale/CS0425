
#Programma per sniffing di pacchetti di rete

from scapy.all import sniff

def process_packet(packet):
    print(packet.summary()) #Descrizione breve del pacchetto

print('Start sniffing... press Ctrl+C to stop.')

try:
#Start dello sniffing, 'prn' specifica la funzione da eseguire per ogni pacchetto catturato
#Store = 0 evita di salvare i pacchetti in memoria, riducendo l'uso della RAM
    sniff(prn=process_packet, store=0)
except KeyboardInterrupt:
    print('\nSniffing stopped.')
