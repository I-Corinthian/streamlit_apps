import streamlit as st

def calculate(ingredients,expected_weight,total_weight):    
    scale = expected_weight / total_weight
    print(f"Scale: {scale}, expected_weight: {expected_weight}, total_weigh: {total_weight}")
    new_ingredients = {}
    for ingredient in ingredients:
        new_ingredients[ingredient] = round(ingredients[ingredient] * scale,2)

    return new_ingredients
    
def display_ingredients(ingredients,is_output=False):
    if is_output:
        st.subheader("UPDATED INGREDIENTS 📜✨✨")
        for ingredient in ingredients:
            col1, col2, col3 = st.columns([0.7,0.15,0.15])
            with col1:
                st.write(ingredient)
            with col2:
                st.write(f"{ingredients[ingredient]} g")
    else:
        st.subheader("INGREDIENTS 📜✨✨")
        for ingredient in ingredients:
            col1, col2, col3 = st.columns([0.7,0.15,0.15])
            with col1:
                st.write(f"{ingredient}: {st.session_state.ingredients[ingredient]} g")
            with col2:
                if st.button("Delete",key=f"delete_{ingredient}"):
                    st.session_state.total_weight -= st.session_state.ingredients[ingredient]
                    del st.session_state.ingredients[ingredient]
                    st.rerun()

st.title("FOOD CALCULATOR 🍪👩‍🍳")


if 'ingredients' not in st.session_state:
    st.session_state.ingredients = {}
if 'total_weight' not in st.session_state:
    st.session_state.total_weight = 0

new_ingredient = st.text_input("enter ingredient 📝")
updated_ingredient = {}
weight = st.number_input("enter weights (g)", label_visibility="collapsed")

if st.button("add ingredient") and new_ingredient and new_ingredient not in st.session_state.ingredients.keys():
    st.session_state.ingredients[new_ingredient] = weight
    st.session_state.total_weight += weight

st.write(f"Total ingredients weight: {st.session_state.total_weight}")
display_ingredients(st.session_state.ingredients)

new_weights = st.number_input("enter new weights (g)")

if st.button('calculate'):
    updated_ingredient = calculate(st.session_state.ingredients,new_weights,st.session_state.total_weight)

if updated_ingredient:
    print(updated_ingredient)
    display_ingredients(updated_ingredient,True)

