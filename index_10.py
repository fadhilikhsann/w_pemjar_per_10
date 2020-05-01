import list_3_6
import list_3_8

def init():
    while True:
        print()
        print("MENU PILIHAN:")
        print("1. Mengetahui interface UP")
        print("2. Mengetahui proses IPC")
        print("3. Exit")
        print()
        pilihan=int(input("Masukkan pilihan: "))
        print()
        if (pilihan==1):
            iface=str(input("Masukkan interface: "))
            print ("Interface [%s] is: %s" %(ifname, list_3_6.get_interface_status(ifname)))      
        elif (pilihan==2):
            print ("Proses IPC socket pair akan muncul")
            list_3_8.test_socketpair()
        elif (pilihan==3):
            print("Bye.")
            break
        else:
            print("Pilihan %s tidak ada"%pilihan)

if __name__ == '__main__':
    init()