import ast
import hashlib
import json
import re
import uuid
from random import randrange
from datetime import datetime
from wikiapi import WikiApi
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.core.mail import EmailMessage
from rest_framework.decorators import api_view
from django.db import models, connection
from .models import pharjinny_registration,likes,mass_post
import base64
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
#from crypt.cipher import AES
from Crypto.Cipher import AES
from bcrypt import hashpw, gensalt


# ************Registration of login**********************************
def pharjinny_registration_form(request):
    if request.method == 'POST':
        objs = json.loads(request.body)
        email_id = objs['email_id']
        email_valid = pharjinny_registration.objects.filter(email_id__icontains=email_id)

        if email_valid.exists():
            return JsonResponse({
                'response': 'Email_id already exists Please try again'
            })
        else:
            pharjinny_registration.objects.create(

                email_id=objs['email_id'],
                password=objs['password'],
                confirm_password=objs['confirm_password'],
                first_name=objs['first_name'],
                last_name=objs['last_name'],
                DOB=objs['DOB'],
                gender=objs['gender'],
                contact_no=objs['contact_no'],
            ),

            subject = 'Thank you'
            email = EmailMessage(subject, 'Thank you for signingup in pharajinny', to=[email_id])
            email.send()
            return JsonResponse({
                'response': 'Data added successfully',

            })
    else:
        return JsonResponse({
            'response': 'Error in inserting',
        })


# **********************Login api *************************************
@api_view(['GET', 'POST'])
def pharjinny_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email_id = data['email_id']
        password = data['password']
        pharjinny_user = pharjinny_registration.objects.filter(email_id__icontains=email_id,
                                                               password__icontains=password)
        if pharjinny_user.exists():
            login_data = pharjinny_registration.objects.filter(email_id__icontains=email_id,
                                                               password__icontains=password)
            posts_serialized = serializers.serialize('json', login_data)
            return JsonResponse({
                "response": "data saved",
                "data": posts_serialized
            })

# **********************search api *************************************
def search(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        cursor = connection.cursor()
        cursor.execute('select table_name from  INFORMATION_SCHEMA.TABLES where  TABLE_SCHEMA ="nodeDb"')
        for (table_name,) in cursor:
            #print table_name
            #cursor.execute('select column_name from INFORMATION_SCHEMA.COLUMNS where TABLE_SCHEMA ="nodeDb" and table_name ="+table_name+"')
            cursor.execute("select column_name from INFORMATION_SCHEMA.COLUMNS where TABLE_SCHEMA ='nodeDb' and table_name ='%s'"%(table_name))
            #data3=cursor.fetchall()
            #print data3

            for(column_name,) in cursor:
               # print column_name

                if column_name!="DOB" and  column_name!="updated_at" and  column_name!="created_at":

                 cursor.execute("select * from "+table_name +" where "+column_name+" LIKE '%"+str(search)+"%'")
                 data=cursor.fetchall()
                 for row in data:
                    #data.encode('utf-8')
                   # ast.literal_eval(data)
                    data10=json.dumps({"lists":str(data)})
                    #print filter(lambda x: x, [data10])

                    #astr = data10.encode("utf-8")

                    return JsonResponse({
                     "response":"success",
                     "data":data10
                 })


# **********************Post api *************************************
def post_like(request):
    if request.method=='POST':
        video=request.FILES.get('video')
        # data = json.loads(request.body)
        # email_id = data['email_id']
        # password = data['password']
        # format, imgstr = data['photo'].split(';base64,')
        # ext = format.split('/')[-1]
        # irand = randrange(0, 10000)
        # irand1=str(irand)
        #data1 = ContentFile(base64.b64decode(imgstr), name=irand1+'.' + ext)
        fs = FileSystemStorage()
        filename = fs.save(video.name, video)
        #data1 = ContentFile(video, name="video"+ '.' + "mp4")
        #file_name = "'myphoto." + ext
        #data1.save()

        # user_like = pharjinny_registration.objects.filter(email_id__icontains=email_id,
        #                                                   password__icontains=password)
        #if user_like.exists():
        likes.objects.create(
                # pharjinny_registration_id=user_like[0].pk,
                # status=data['status'],
                # comments=data['comments'],
                # photo=data1,
                #video=data['video'],
                video=filename
                #content=data['content'],
            )

        # else:
        #     return JsonResponse({
        #         "response":"Please login in"
        #     })
    return JsonResponse({
        "response":"Data saved successfully"
    })

def update_like(request):
    if request.method=='POST':
        data = json.loads(request.body)
        email_id = data['email_id']
        password = data['password']
        user_like=pharjinny_registration.objects.filter(email_id__icontains=email_id,
                                                               password__icontains=password)
        if user_like.exists():
            data=likes.objects.filter(status="likes")
            if data.exists():
                data1=likes.objects.filter(pk=1).update(
                    status="unlikes"
                )
                #posts_serialized = serializers.serialize('json', data1)
                return JsonResponse({
                    "response": "Like updated Successfully",
                    #"data": posts_serialized
                })
            else:
                data1 = likes.objects.filter(pk=1).update(
                    status="likes"
                )
               # posts_serialized = serializers.serialize('json', data1)
                return JsonResponse({
                    "response": "Unlike updated Successfully",
                  #  "data": posts_serialized
                })
            posts_serialized = serializers.serialize('json',data)
            return JsonResponse({
                "response": "data saved",
                "data": posts_serialized
            })
        else:
            return JsonResponse({
                'response': 'Error in inserting',
            })

    else:
        return JsonResponse({
            'response': 'Please try again.......',
        })


def posts(request):
    if request.method=='POST':
        data=json.loads(request.body)
        email_id = data['email_id']
        password = data['password']
        user_like = pharjinny_registration.objects.filter(email_id__icontains=email_id,
                                                          password__icontains=password)
        posts_serialized = serializers.serialize('json', user_like)
        if user_like.exists():
            user_content = likes.objects.filter(pharjinny_registration_id__icontains=user_like[0].pk)
            mass_post.objects.create(
                content_id=user_content[0].pk,
                user_id=user_like[0].pk,
                status=data['status'],
                comment=data['comment']

             )
            return JsonResponse({
                "response":"Data saved successfully"
            })
        else:
            return JsonResponse({
                "response":"User doesnot exists"


         })

def fetch_post(request):
    if request.method=='POST':
        data=json.loads(request.body)

        email_id = data['email_id']
        password = data['password']
        user_like = pharjinny_registration.objects.filter(email_id__icontains=email_id,
                                                          password__icontains=password)
        posts_serialized = serializers.serialize('json', user_like)
        #time=user_like[0].created_at.strftime('%H:%M:%S')
        #return JsonResponse(time,safe=False)
        if user_like.exists():
            #fetch=mass_post.objects.filter(user_id__icontains=user_like[0].id)
            #count=mass_post.objects.filter(status="likes").count()
            #count1=mass_post.objects.filter(status="unlikes").count()
            fetch_postdata=likes.objects.filter(pharjinny_registration_id=user_like[0].pk)
            time = fetch_postdata[0].created_at.strftime('%H:%M:%S')
            fetch_serializar = serializers.serialize('json', fetch_postdata)
            fetch_json = json.loads(fetch_serializar.replace("\'", '"'))
            #print fetch_json.fields
            return JsonResponse({
               # "no_of_likes":count,
               # "no_of_unlikes":count1
                "response":fetch_json,
                "time":time
            })

def wikiapi(request):
 if request.method=='GET':
    search = request.GET.get('search')
    wiki=WikiApi()
    wiki=WikiApi({'locale': 'en'})
    results = wiki.find(search)
    article=wiki.get_article(results[0])
    content=article.content
    # print content
    return HttpResponse(content)

def code(request):
    if request.method=='GET':
        message = request.GET.get('message')
        message=message.encode('UTF-8')
        hashed = hashpw(message, gensalt())
        print hashed
        if hashpw(message,hashed)==hashed:
            print "Match found"
        else:
            print "Please try password again"
    return HttpResponse("mast hoon")
