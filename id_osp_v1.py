import streamlit as st

def calculate_control_digit(firefighter_number):
    digits = [int(d) for d in str(firefighter_number).zfill(7)]
    weights = range(1, 8)
    product = [d * w for d, w in zip(digits, weights)]
    control_digit = sum(product) % 11
    if control_digit == 10:
        control_digit = 0
    return control_digit

def generate_firefighter_numbers(count):
    numbers = []
    for i in range(count):
        firefighter_number = str(i).zfill(7)
        control_digit = calculate_control_digit(i)
        numbers.append(firefighter_number + str(control_digit))
    return numbers

def is_valid_firefighter_number(number):
    if len(number) != 8:
        return False
    firefighter_number = int(number[:-1])
    control_digit = int(number[-1])
    return calculate_control_digit(firefighter_number) == control_digit

st.title('Generowanie i Walidacja Numerów Strażaków')

st.sidebar.header('Menu')
option = st.sidebar.selectbox('Wybierz opcję:', ('Generuj numery', 'Sprawdź numer'))

if option == 'Generuj numery':
    count = st.number_input('Podaj liczbę numerów do wygenerowania:', min_value=1, value=10)
    if st.button('Generuj'):
        numbers = generate_firefighter_numbers(count)
        st.write('Wygenerowane numery strażaków:')
        for number in numbers:
            st.write(number)

elif option == 'Sprawdź numer':
    number_to_check = st.text_input('Podaj numer strażaka do sprawdzenia:')
    if st.button('Sprawdź'):
        if is_valid_fireather_number(number_to_check):
            st.success('Numer jest poprawny.')
        else:
            st.error('Numer jest niepoprawny.')

