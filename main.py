import sys
from assets.ui import banner, clear, log, Y, G, W, R, C
from core.generator import LeadGenerator
from core.validator import LeadValidator

def main():
    clear()
    banner()
    
    gen = LeadGenerator()
    val = LeadValidator()

    print(f"{W}[1] Leads Generator")
    print(f"{W}[2] Leads Validator")
    print(f"{W}[0] Exit")

    choice = input(f"\n{C}>> Enter Choice: {W}")

    if choice == "1":
        country = input(f"{C}>> Enter Country Code (e.g: ID, US, MY): {W}")
        try:
            amount = int(input(f"{C}>> Enter amount to generate: {W}"))
            output_file = input(f"{C}>> Enter Output Path: {W}")
            
            log(f"Generating {amount} leads for {country}...")
            numbers = gen.generate(country, amount)
            
            with open(output_file, 'w') as f:
                for n in numbers:
                    f.write(n + "\n")
            
            log(f"Numbers generated >>>> {len(numbers)}", "success")
            log(f"Saved to: {output_file}", "info")
        except ValueError:
            log("Invalid amount!", "error")

    elif choice == "2":
        # Logika validator akan saya sambung di pesan berikutnya biar gak kepotong
        pass

if __name__ == "__main__":
    main()
    elif choice == "2":
        input_file = input(f"{C}>> Enter Generated Numbers File name: {W}")
        output_file = input(f"{C}>> Enter Output Path for Valid Leads: {W}")
        
        try:
            with open(input_file, 'r') as f:
                raw_numbers = [line.strip() for line in f if line.strip()]
            
            log(f"Loading Numbers >>>> {len(raw_numbers)}", "info")
            log("Validating... Please wait.", "info")
            
            valid_leads, invalid_count = val.validate(raw_numbers)
            
            with open(output_file, 'w') as f:
                for v in valid_leads:
                    f.write(v + "\n")
            
            print(f"\n{W}{'='*40}")
            log(f"Checked: {len(raw_numbers)}", "info")
            log(f"Valid  : {len(valid_leads)}", "success")
            log(f"Errors : {invalid_count}", "error")
            print(f"{W}{'='*40}")
            log(f"Valid leads saved to: {output_file}", "success")
            
        except FileNotFoundError:
            log(f"File {input_file} tidak ditemukan!", "error")
        except Exception as e:
            log(f"Terjadi kesalahan: {e}", "error")

    elif choice == "0":
        log("Exiting... Stay secure!", "info")
        sys.exit()

    else:
        log("Pilihan tidak tersedia!", "error")

    # Opsi untuk kembali ke menu utama
    input(f"\n{Y}Press Enter to return to menu...{W}")
    main()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{R}[!] Program dihentikan paksa oleh user.{W}")
        sys.exit()
