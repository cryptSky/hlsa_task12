from flask import Response, request
from flask import current_app as app
from db.models import User
from flask_restful import Resource
from mongoengine.errors import DoesNotExist, NotUniqueError, ValidationError
from errors import InternalServerError, SchemaValidationError, UserNotFoundError, EmailAlreadyExistError
from redis import Redis
from datetime import timedelta
import json
from random import randrange
import math
from faker import Faker
from faker.providers import date_time
import greenstalk

fake = Faker()
fake.add_provider(date_time)

redis = Redis("redis", 6379)
redis_aof = Redis("redis-aof", 6380)

beanstalkd = greenstalk.Client(('beanstalkd', 11300))

CACHE_TIMEOUT = 100

class UsersApi(Resource):

	def post(self):
		try:
			body = request.get_json()
			
			body['birthdate'] = fake.date()
			body["name"] = fake.name()
			body["email"] = fake.email()

			
			user = User(name=body["name"], email=body["email"], birthdate=body["birthdate"])

			id = body['email'] + body['birthdate']

			if body['type'] == 'redis':
				redis.setex(str(id), timedelta(seconds=CACHE_TIMEOUT), value=json.dumps(body),)
			elif body['type'] == 'redis-aof':
				redis_aof.setex(str(id), timedelta(seconds=CACHE_TIMEOUT), value=json.dumps(body),)
			elif body['type'] == 'beanstalkd':
				beanstalkd.put(json.dumps(body))

			return {'id': str(id)}, 201
		except Exception as e:
			app.logger.error(e)
			raise InternalServerError
