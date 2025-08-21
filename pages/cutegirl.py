 import steamlit as st

st.set_page_config(
    page_title="테토/에겐 테스트",
    layout="centered"
)

teto_score = 0
egen_score = 0

st.title("테토/에겐 테스트")
st.markdown("질문을 읽고 평소의 나에게 더 가까 답을 선택해주세요!")

name = st.text_input("이름을 입력하세요")

gender = st.radio("성별을 선택하세요", ["남자","여자"], horizontal=True)

Q1 = st.radio("친구들과 만날 때 나는?", ["어디서든 분위기를 주도하는 편","조용히 따라가며 분위기를 맞춰주는 편"], horizontal=True)
if Q1 == "어디서든 분위기를 주도하는 편":
    teto_score += 1
else:
    egen_score += 1
 
Q2 = st.radio("갈등이 생겼을 때 나의 대처 방식은?", ["바로 이야기해서 해결한다","시간을 두고 우회적으로 풀어나간다"], horizontal=True)
if Q2 == "바로 이야기해서 해결한다":
    teto_score += 1
else:
    egen_score += 1
 
Q3 = st.radio("내가 선호하는 패션 스타일은?", ["심플하고 기본적인 스타일(무지티, 청바지 등)","디테일이 살아있는 예쁜 스타일(패턴, 액세서리 등)"], horizontal=True)
if Q3 == "심플하고 기본적인 스타일(무지티, 청바지 등)":
    teto_score += 1
else:
    egen_score += 1
 
Q4 = st.radio("연애할 때 나는?", ["내가 주도하며 이끌어감","상대방에게 맞춰주는 편"], horizontal=True)
if Q4 == "내가 주도하며 이끌어감":
    teto_score += 1
else:
    egen_score += 1
 
Q5 = st.radio("스트레스 받을 때 나의 해소 방식은?", ["운동이나 수다 등 활동적인 것","게임 등 혼자만의 시간을 가지며 조용히 보내는 것"], horizontal=True)
if Q5 == "운동이나 수다 등 활동적인 것":
    teto_score += 1
else:
    egen_score += 1
 
Q6 = st.radio("나의 의사결정 스타일은?", ["빠르게 결정하고 바로 행동한다","신중하게 고민하고 여러 의견을 들어본다"], horizontal=True)
if Q6 == ""빠르게 결정하고 바로 행동한다":
    teto_score += 1
else:
    egen_score += 1
 
Q7 = st.radio("새로운 환경에서 나는?", ["빠르게 적응하고 새로운 사람들과 어울린다","시간을 두고 천천히 적응해나간다"], horizontal=True)
if Q7 == "빠르게 적응하고 새로운 사람들과 어울린다":
    teto_score += 1
else:
    egen_score += 1
 
Q8 = st.radio("내가 좋아하는 대화 주제는?", ["시사,스포츠,현실적인 이야기","감정,관계,일상의 소소한 이야기"], horizontal=True)
if Q8 == ""시사,스포츠,현실적인 이야기":
    teto_score += 1
else:
    egen_score += 1
 
Q9 = st.radio("친구가 고민 상담을 할 떄 나는?", [해결책을 제시하고 직접적인 조연을 해준다","공감해주고 감정을 들어주는 편이다"], horizontal=True)
if Q9 == "해결책을 제시하고 직접적인 조연을 해준다":
    teto_score += 1
else:
    egen_score += 1
                                      
Q10 = st.radio("나의 라이프스타일은?", ["목표 지향적이고 계획적으로 산다","감정과 직감을 따라 자연스러게 산다"], horizontal=True)
if Q10 == "목표 지향적이고 계획적으로 산다":
    teto_score += 1
else:
    egen_score += 1
 
Q11 = st.radio("데이트할 때 선호하는 분위기는?", ["활동적이고 역동적인 데이트","조용하고 로맨틱한 분위기의 데이트"], horizontal=True)
if Q11 == "활동적이고 역동적인 데이트":
    teto_score += 1
else:
    egen_score += 1
 
Q12 = st.radio("나를 가장 잘 표현하는 말은?", ["당당하고 솔직한 사람","섬세하고 배려심 많은 사람"], horizontal=True)
if Q12 == "당당하고 솔직한 사람":
    teto_score += 1
else:
    egen_score += 1

if gende
