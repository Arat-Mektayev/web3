from flask import Flask, render_template, request, abort, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'rrdxbdy122qdrh'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Для примера используем SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Создание экземпляра приложения Flask

db = SQLAlchemy(app)
