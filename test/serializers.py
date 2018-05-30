from rest_framework import serializers
from .models import pharjinny_registration,likes,mass_post



# class customer_detilsSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model=company_profiles
#         fields=('company_name','company_logo','company_details','directors','specialities','departments','company_size','establishment','awards_and_accomplishment','main_products'
#                 ,'technologies_used','company_type','share_details','trade_assuranc','location','website_link')


# class Pharajinny_registration(serializers.ModelSerializer):
#     class Meta:
#         model=pharjinny_registration
#         fields=('email_id','password','confirm_password','first_name','last_name','DOB','gender','contact_no')



class pharjinny_registrationserializer(serializers.ModelSerializer):

       class Meta:
           model=pharjinny_registration
           fields='__all__'

class likesserializer(serializers.ModelSerializer):
        class Meta:
            mdoels=likes
            fields='__all__'

class mass_postserializer(serializers.ModelSerializer):
       class Meta:
           models=mass_post
           fields='__all__'