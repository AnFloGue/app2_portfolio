import streamlit as st

st.set_page_config(page_title='My Streamlit App', page_icon=':shark:', layout='wide', initial_sidebar_state='auto')

col1, col2 = st.columns(2)



with col1:
    st.title('APP 01')
    st.image('images/2.png', use_column_width=True)
with col1:
    st.title('APP 01')
    content = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    Suspendisse nec justo ut felis facilisis ultrices.
    consectetur adipiscing elit. Suspendisse nec justo ut felis facilisis ultrices."""
    
    st.write(content)
    st.info('This is an info message')
    st.image('images/1.png', use_column_width=True)
    
    
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
