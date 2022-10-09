import streamlit as st

from mySpellCheck import mySymSpell,ngramSpell

st.title('Statistical Spelling Correction for Burmese language')
text = st.text_area("Enter Text:", value='', height=None, max_chars=None, key=None)

corrected = mySymSpell(text)

if st.button('Correction result'):
    if text == '':
        st.write('Please enter text for checking') 
    else: 
        result_dict = parser.parse(text)
        st.markdown('**Corrected Sentence - **' + corrected)
else: pass
