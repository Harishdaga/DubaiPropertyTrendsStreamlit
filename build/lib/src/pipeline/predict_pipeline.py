import pandas as pd
from src.exception import CustomException
import sys
import os
from src.utils import load_object
from src.logger import logging

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            logging.info('model and preprocessor readed successfully')
            model=load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            logging.info('model and preprocessor loaded successfully')
            data_scaled = preprocessor.transform(features)
            pred = model.predict(data_scaled)
            return pred
        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(
            self,
            latitude, 
            longitude,
            size_in_sqft,
            no_of_bedrooms,
            no_of_bathrooms,
            quality,
            maid_room,
            unfurnished,
            balcony,
            barbecue_area,
            built_in_wardrobes,
            central_ac,
            childrens_play_area,
            childrens_pool,
            concierge,
            covered_parking,
            kitchen_appliances,
            lobby_in_building,
            maid_service,
            networked,
            pets_allowed,
            private_garden,
            private_gym,
            private_jacuzzi,
            private_pool,
            security,
            shared_gym,
            shared_pool,
            shared_spa,
            study,
            vastu_compliant,
            view_of_landmark,
            view_of_water,
            walk_in_closet 
    ):
        self.latitude = latitude
        self.longitude = longitude
        self.size_in_sqft = size_in_sqft
        self.no_of_bedrooms = no_of_bedrooms
        self.no_of_bathrooms = no_of_bathrooms
        self.quality = quality
        self.maid_room = maid_room
        self.unfurnished = unfurnished
        self.balcony = balcony
        self.barbecue_area = barbecue_area
        self.built_in_wardrobes = built_in_wardrobes
        self.central_ac = central_ac
        self.childrens_play_area = childrens_play_area
        self.childrens_pool = childrens_pool
        self.concierge = concierge
        self.covered_parking = covered_parking
        self.kitchen_appliances = kitchen_appliances
        self.lobby_in_building = lobby_in_building
        self.maid_service = maid_service
        self.networked = networked
        self.pets_allowed = pets_allowed
        self.private_garden = private_garden
        self.private_gym = private_gym
        self.private_jacuzzi = private_jacuzzi
        self.private_pool = private_pool
        self.security = security
        self.shared_gym = shared_gym
        self.shared_pool = shared_pool
        self.shared_spa = shared_spa
        self.study = study
        self.vastu_compliant = vastu_compliant
        self.view_of_landmark = view_of_landmark
        self.view_of_water = view_of_water
        self.walk_in_closet = walk_in_closet

    def get_data_as_dataframe(self):
        custom_data_input_dict = {
            'latitude': [self.latitude], 
            'longitude': [self.longitude],
            'size_in_sqft': [self.size_in_sqft],
            'no_of_bedrooms': [self.no_of_bedrooms],
            'no_of_bathrooms': [self.no_of_bathrooms],
            'quality': [self.quality],
            'maid_room': [self.maid_room],
            'unfurnished': [self.unfurnished],
            'balcony': [self.balcony],
            'barbecue_area': [self.barbecue_area],
            'built_in_wardrobes': [self.built_in_wardrobes],
            'central_ac': [self.central_ac],
            'childrens_play_area': [self.childrens_play_area],
            'childrens_pool': [self.childrens_pool],
            'concierge': [self.concierge],
            'covered_parking': [self.covered_parking],
            'kitchen_appliances': [self.kitchen_appliances],
            'lobby_in_building': [self.lobby_in_building],
            'maid_service': [self.maid_service],
            'networked': [self.networked],
            'pets_allowed': [self.pets_allowed],
            'private_garden': [self.private_garden],
            'private_gym': [self.private_gym],
            'private_jacuzzi': [self.private_jacuzzi],
            'private_pool': [self.private_pool],
            'security': [self.security],
            'shared_gym': [self.shared_gym],
            'shared_pool': [self.shared_pool],
            'shared_spa': [self.shared_spa],
            'study': [self.study],
            'vastu_compliant': [self.vastu_compliant],
            'view_of_landmark': [self.view_of_landmark],
            'view_of_water': [self.view_of_water],
            'walk_in_closet': [self.walk_in_closet]
            }
        return pd.DataFrame(custom_data_input_dict)