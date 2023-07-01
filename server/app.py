import os

from dotenv import load_dotenv
load_dotenv()

from flask import Flask, jsonify, make_response, request, render_template
from flask_migrate import Migrate
from flask_restful import Api, Resource