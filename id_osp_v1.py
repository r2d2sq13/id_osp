import streamlit as st

def generate_luhn_checksum(number):
    total = 0
    reverse_digits = [int(digit) for digit in str(number)[::-1]]
    for i, digit in enumerate(reverse_digits):
        if i % 2 == 0:
            total += digit
        else:
            doubled = digit * 2
            if doubled > 9:
                doubled -= 9
            total += doubled
    checksum = (10 - (total % 10)) % 10
    return checksum

def generate_identification_numbers(count):
    base_number = 1000000
    numbers = []
    for i in range(count):
        number = base_number + i
        checksum = generate_luhn_checksum(number)
        full_number = int(str(number) + str(checksum))
        numbers.append(full_number)
    return numbers

def validate_identification_number(number):
    original_checksum = int(str(number)[-1])
    base_number = int(str(number)[:-1])
    calculated_checksum = generate_luhn_checksum(base_number)
    return original_checksum == calculated_checksum

st.title("OSP Strażaków Numer Identyfikacyjny")

menu = ["Generowanie Numerów", "Sprawdzanie Numeru", "Autorzy"]
choice = st.sidebar.selectbox("Wybierz opcję:", menu)

if choice == "Generowanie Numerów":
    st.header("Generowanie Numerów Identyfikacyjnych")
    count = st.number_input("Podaj liczbę numerów identyfikacyjnych do wygenerowania:", min_value=1, value=1)
    if st.button("Generuj Numery"):
        numbers = generate_identification_numbers(count)
        st.write("Wygenerowane numery identyfikacyjne:")
        st.write(numbers)

elif choice == "Sprawdzanie Numeru":
    st.header("Sprawdzanie Numeru Identyfikacyjnego")
    check_number = st.number_input("Podaj numer identyfikacyjny do sprawdzenia:", min_value=10000000, value=10000000)
    if st.button("Sprawdź Numer"):
        if validate_identification_number(check_number):
            st.success("Numer identyfikacyjny jest poprawny.")
        else:
            st.error("Numer identyfikacyjny jest niepoprawny.")

elif choice == "Autorzy":
    st.header("Autorzy")
    st.write("Autor: Komenda Główna Państwowej Straży Pożarnej PSP / Michał Kłosiński")
    st.write("Link do kodu: [GitHub](https://github.com/r2d2sq13/id_osp/blob/main/id_osp_v1.py)")
    st.write("e-mail: mklosinski@kg.straz.gov.pl")
