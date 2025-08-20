 import steamlit as st

st.title('당신은 테토녀? 에겐남?')
if st.button("테토,에겐은 무엇일까?"):
  st.session_state.count += 1
'''st.columns(n): 화면을 n개의 수직 열로 나눕니다
col1, col2 = st.columns(2) 

with col1:
  st.
with col2:
    st.write("오른쪽 열입니다.")  # 두 번째 열에 내용 작성
    '''
