import random
import phonenumbers
from phonenumbers import phoneNumberMetadata

class LeadGenerator:
    def __init__(self):
        pass

    def get_country_info(self, country_code):
        try:
            # Mengambil metadata format telepon berdasarkan kode negara (contoh: ID, US, MY)
            region_code = country_code.upper()
            return region_code
        except:
            return None

    def generate(self, country_code, amount):
        generated = []
        try:
            # Ambil dial code (contoh: ID -> 62)
            example_number = phonenumbers.example_number(country_code.upper())
            dial_code = example_number.country_code
            
            # Ambil panjang nomor rata-rata
            national_number = str(example_number.national_number)
            length = len(national_number)

            for _ in range(amount):
                # Generate angka acak sesuai panjang nomor nasional negara tersebut
                start_digit = national_number[0] # Biar prefix-nya masuk akal
                suffix_length = length - 1
                random_suffix = ''.join([str(random.randint(0, 9)) for _ in range(suffix_length)])
                
                full_number = f"+{dial_code}{start_digit}{random_suffix}"
                generated.append(full_number)
            
            return generated
        except Exception as e:
            return f"Error: {str(e)}"
