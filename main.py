import functions3

def main():
    while True:
        print("\nLog File Analysis Menu")
        print("1. Display unique messages")
        print("2. Search for IP addresses")
        print("3. Count events per node")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            messages = functions3.get_unique_messages("applog.txt")
            print("\nUnique Messages:")
            for msg in messages:
                print("-", msg)
        
        elif choice == "2":
            octet = input("Enter an octet value (first or fourth octet): ")
            unique_ips = functions3.get_ips_by_octet("applog.txt", octet)
            print("\nMatching IP Addresses:")
            for ip in unique_ips:
                print(ip)
            print(f"Total unique matching IPs: {len(unique_ips)}")
        
        elif choice == "3":
            node_counts = functions3.count_events_per_node("applog.txt")
            print("\nEvent Counts per Node:")
            for node, count in node_counts.items():
                print(f"{node}: {count} events")
        
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
