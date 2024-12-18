import streamlit as st
from src.pipeline.predict_pipeline import CustomData, PredictPipeline


custom_css = """
<style>
h1 {
        font-size: 3rem;
        color: #ABBA7C; /* Main heading color */
        text-align: center;
        margin-top: 20px;
        margin-bottom: 20px;
        font-family: Verdana, Geneva, Tahoma, sans-serif;
    }
    h1:hover {
        color: #FFE31A; /* Accent color on hover */
    }
        legend {
        font-size: 2rem;
        color: #ABBA7C; /* Matches primary text theme */
        text-align: center;
        margin-bottom: 10px;
        font-family: Verdana, Geneva, Tahoma, sans-serif;
    }
    legend:hover {
        color: #FFE31A; /* Accent color on hover */
    }

</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)
st.markdown("<h1>Dubai Property Trends</h1>", unsafe_allow_html=True)
st.markdown("<legend>Property Price Prediction</legend>", unsafe_allow_html=True)

with st.form(key='user_form', border=False, enter_to_submit=True):
    a, b, c, d, e = st.columns(gap='small', vertical_alignment='top', spec=[.2, .2, .2, .2, .2])
    latitude = a.number_input("Select Latitude",min_value=24.950000, max_value=25.400000, step=0.001)
    longitude = b.number_input('Select Longitude', min_value=54.950000, max_value=55.550000, step=0.001)
    size_in_sqft = c.number_input('Size in SQFT', min_value=0, max_value=250000)
    no_of_bedrooms = d.number_input('No of Bedrooms', min_value=0, max_value=30, step=1)
    no_of_bathrooms = e.number_input('No of Bathrooms', min_value=0, max_value=20, step=1)

    quality = a.selectbox('Quality', options=['Select an option', 'Low', 'Medium', 'High', 'Ultra'])
    maid_room = b.selectbox('Maid Room', options=['Select an option', True, False])
    unfurnised = c.selectbox('Unfurnised', options=['Select an option', True, False])
    balcony = d.selectbox('Balcony', options=['Select an option', True, False])
    barbecue_area = e.selectbox('Barbecue area', options=['Select an option', True, False])
    built_in_wardrobes = a.selectbox('Built in Wardrobes', options=['Select an option', True, False])
    central_ac = b.selectbox('Central AC', options=['Select an option', True, False])
    childrens_play_area = c.selectbox('Childrens Play Area', options=['Select an option', True, False])
    childrens_pool = d.selectbox('Childrens Pool', options=['Select an option', True, False])
    concierge = e.selectbox('Concierge', options=['Select an option', True, False])
    covered_parking = a.selectbox('Covered Parking', options=['Select an option', True, False])
    kitchen_appliances = b.selectbox('Kitchen Appliances', options=['Select an option', True, False])
    lobby_in_building = c.selectbox('Lobby in Building', options=['Select an option', True, False])
    maid_service = d.selectbox('Maid Service', options=['Select an option', True, False])
    networked = e.selectbox('Networked', options=['Select an option', True, False])
    pets_allowed = a.selectbox('Pets Allowed', options=['Select an option', True, False])
    private_garden = b.selectbox('Private Garden', options=['Select an option', True, False])
    private_gym = c.selectbox('Private Gym', options=['Select an option', True, False])
    private_jacuzzi = d.selectbox('Private Jacuzzi', options=['Select an option', True, False])
    private_pool = e.selectbox('Private Pool', options=['Select an option', True, False])
    security = a.selectbox('Security', options=['Select an option', True, False])
    shared_gym = b.selectbox('Shared Gym', options=['Select an option', True, False])
    shared_pool = c.selectbox('Shared Pool', options=['Select an option', True, False])
    shared_spa = d.selectbox('Shared Spa', options=['Select an option', True, False])
    study = e.selectbox('Study', options=['Select an option', True, False])
    vastu_compliant = a.selectbox('Vastu Compliant', options=['Select an option', True, False])
    view_of_landmark = b.selectbox('View of Landmark', options=['Select an option', True, False])
    view_of_water = c.selectbox('View of Water', options=['Select an option', True, False])
    walk_in_closet = d.selectbox('Walk in Closet', options=['Select an option', True, False])
    submit_button = st.form_submit_button('Predict')

if submit_button:
    default_value = 'Select an option'
    if latitude and longitude and size_in_sqft and no_of_bathrooms and no_of_bedrooms and quality and maid_room and unfurnised and balcony and barbecue_area \
    and built_in_wardrobes and central_ac and childrens_play_area and childrens_pool and concierge and covered_parking and kitchen_appliances and lobby_in_building and \
        maid_service and networked and pets_allowed and private_garden and private_gym and private_jacuzzi and private_pool and security and shared_gym and shared_pool \
        and shared_spa and study and vastu_compliant and view_of_landmark and view_of_water and walk_in_closet:
        if quality == default_value or maid_room == default_value or unfurnised == default_value or balcony == default_value \
            or barbecue_area == default_value or built_in_wardrobes == default_value or central_ac == default_value or childrens_play_area == default_value  \
                or childrens_pool == default_value or concierge == default_value or covered_parking == default_value or kitchen_appliances == default_value  \
                    or lobby_in_building == default_value or maid_service == default_value or networked == default_value or pets_allowed == default_value  \
                        or private_garden == default_value or private_gym == default_value or private_jacuzzi == default_value or private_pool == default_value  \
                            or security == default_value or shared_gym == default_value or shared_pool == default_value or shared_spa == default_value \
                                or study == default_value or vastu_compliant == default_value or view_of_landmark == default_value or view_of_water == default_value \
                                    or walk_in_closet == default_value:
                                    st.warning('Select valid Input')

        else:
            input_data = CustomData(latitude=latitude, longitude=longitude, size_in_sqft=size_in_sqft, no_of_bedrooms=no_of_bedrooms, no_of_bathrooms=no_of_bathrooms, \
                                quality=quality, maid_room=maid_room, unfurnished=unfurnised, balcony=balcony, barbecue_area=barbecue_area, built_in_wardrobes=built_in_wardrobes\
                                ,central_ac=central_ac, childrens_play_area=childrens_play_area, childrens_pool=childrens_pool, concierge=concierge, covered_parking=covered_parking,\
                                kitchen_appliances=kitchen_appliances, lobby_in_building=lobby_in_building, maid_service=maid_service, networked=networked, pets_allowed=pets_allowed, private_garden=private_garden,\
                                private_gym=private_gym, private_jacuzzi=private_jacuzzi, private_pool=private_pool, security=security, shared_gym=shared_gym, shared_pool=shared_pool, shared_spa=shared_spa, study=study, \
                                vastu_compliant=vastu_compliant, view_of_landmark=view_of_landmark, view_of_water=view_of_water, walk_in_closet=walk_in_closet)
            pred_df = input_data.get_data_as_dataframe()
            predict_pipeline = PredictPipeline()
            result = round(predict_pipeline.predict(pred_df)[0], -3)
            st.success(result)
    else:
        st.warning('please fill the currect details')
