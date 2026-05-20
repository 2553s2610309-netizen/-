import streamlit as st

# 페이지 제목
st.title("🐶 강아지 종 소개")

# 강아지 데이터
dogs = {
    "말티즈": {
        "info": "작고 애교가 많은 반려견입니다.",
        "image": "https://images.unsplash.com/photo-1596495577886-d920f1fb7238"
    },
    "푸들": {
        "info": "똑똑하고 털 빠짐이 적습니다.",
        "image": "https://images.unsplash.com/photo-1517849845537-4d257902454a"
    },
    "골든리트리버": {
        "info": "온순하고 가족 친화적인 대형견입니다.",
        "image": "https://images.unsplash.com/photo-1552053831-71594a27632d"
    }
}

# 선택 박스
selected_dog = st.selectbox(
    "강아지 종을 선택하세요",
    list(dogs.keys())
)

# 정보 출력
st.subheader(selected_dog)
st.write(dogs[selected_dog]["info"])

# 이미지 출력
st.image(
    dogs[selected_dog]["image"],
    width=400
)
