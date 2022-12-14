import streamlit as st

from mySpellCorrect import mySymSpell,ngramSpell

st.title('Statistical Spelling Correction for Burmese language')
text = st.text_area("Enter Text:", value='', height=None, max_chars=None, key=None)

corrected = mySymSpell(text)
corrected = str(corrected[0])

if st.button('Correction result'):
    if text == '':
        st.write('Please enter text for checking') 
    else: 
        st.markdown('**Corrected Sentence - **' + corrected)
else: pass
