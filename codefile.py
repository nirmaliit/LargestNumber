
import streamlit as st

def getLargerNumber(num1, num2, num3):

    if (num1 >= num2) and (num1>= num3):
        return num1
    elif (num2 >= num1) and (num2 >= num3):
        return num2
    else:
        return num3
    
def get_numbers():

    col1, col2, col3 = st.columns(3)

    with col1:
        number1 = st.number_input('First number', value = 5., placeholder = 'Type a number...', step = 1.)

    with col2:
        number2 = st.number_input('Second number', value = 6., placeholder = 'Type a number...', step = 1.)

    with col3:
        number3 = st.number_input('Third number', value = 4., placeholder = 'Type a number...', step = 1.)
    
    return number1, number2, number3

if __name__ == "__main__":

    st.subheader('Select/Enter Three Numbers Program will Finding the largest among the given numbers')
    st.write('#')
    number1, number2, number3 = get_numbers()
    largest = getLargerNumber(number1, number2, number3)
    st.write('#')
    st.success(f'Result: Largest number is : {largest}')
                                              
