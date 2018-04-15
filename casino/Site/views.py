# django settings
from django.shortcuts import render, redirect
from django.forms.models import modelform_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth, messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


# Create your views here.
from .models import Login1
from hashlib import sha256

import sys
import os
import requests


@csrf_exempt
def index( request ) :
	if request.user.is_authenticated :
		return render( request, 'index.html', { 'user_name': request.session['name'] } )
	else :
		return render( request, 'index.html' )



@csrf_exempt
def login_register_page( request ) :

	try :

		if request.POST :
			post = request.POST
			print( post )
			isLogin = post.get('phone_login', None)


			# Login
			if isLogin is not None :


				try :
					obj = Login1.objects.get( account=post.get('phone_login', ''))
				except :
					messages.info( request, 'No Such User!')
					return HttpResponseRedirect('/signin/')

				name = obj.name
				phone = obj.account
				success = obj.password == post.get('pwd_login', '')


				if success :

					if request.user.is_authenticated: 
						messages.info( request, 'The User is Logined!')
						return HttpResponseRedirect('/index/')
					
					user = auth.authenticate( username=name, email=phone, password=obj.password )

					if user is not None and user.is_active :

						if user.is_active :

							auth.login( request, user )
							messages.success( request,'Success Login!')
							request.session['name'] = name

							print (request.session['name'])
							print (name)

							return render( request, 'index.html', { 'user_name': request.session['name'] } )
				else :

					messages.error( request, 'Wrong Password!')
					return HttpResponseRedirect('/signin/')

				
			# signup
			else :
				
				msg = ''
				
				name = post.get('user_signup', None)
				phone = post.get('phone_signup', None)
				password = post.get('pwd_signup', None)
				password_confirm = post.get('pwd2_signup', None)


				if all( [name, phone, password, password_confirm] ) :
					if password == password_confirm :
						
						print( 'yes')

						Successed = False; Registered = False

						try :
							Login1.objects.get( account=email )
							Registered = True

						except Exception as e :
							Registered = False


						if not Registered :
							
							Login1( name=name, account=phone, password=password, certified=0, money=0, bet=0, totalMoney=0, totalIntro=0, totalPer=0, introBet=0, authority=0).save()
							user = User.objects.create_user(username=name, email=phone, password=password)
							user.save()
							msg = 'Register Successed!!'; Successed = True

						else :
							msg = 'The User Has Signed Up Before!'; Successed = False

					else :
						msg = 'Check The Confirm Password!'; Successed = False

				else :
					msg = 'Empty Values!'; Successed = False


				if Successed :
					messages.success( request, msg )
					return HttpResponseRedirect('/index/')
				else :
					messages.info( request, msg ) 
					return HttpResponseRedirect('/signin/')


				

		else :
			print( 'not post')

		
		return render( request, 'login.html' )

	except Exception as e :
		exc_type, exc_obj, exc_tb = sys.exc_info()
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		print(exc_type, fname, exc_tb.tb_lineno)
		return HttpResponse( '%s %s %s\n%s' % (str(exc_type), str(fname), str(exc_tb.tb_lineno), str(e) ) )



def logout( request ) :
	msg = ''
	try :
		auth.logout( request )
		msg = 'Success Logout'
	except Exception as e :
		msg = 'Fail To Logout: %s' % ( str(e) )

	messages.info( request, msg )
	return HttpResponseRedirect( '/index/' )