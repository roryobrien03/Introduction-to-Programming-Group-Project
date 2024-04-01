import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime as dt
import plotly.express as plx
from pandas_datareader import data as pdr
import sys
import time
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.tree import DecisionTreeRegressor
import seaborn as sns
import math
def febcalendar(): #Prints calendar for February
    print("=" * 36)
    row = "| {:2} | {:2} | {:2} | {:2} | {:2} | {:2} | {:2} | "
    print(row.format("M", "T", "W", "T", "F", "S", "S"))
    print("-" * 36)
    print(row.format("01", "02", "03", "04", "05", "06", "07"))
    print("-" * 36)
    print(row.format("08", "09", "10", "12", "13", "14", "15"))
    print("-" * 36)
    print(row.format("16", "17", "18", "19", "20", "21", "22"))
    print("-" * 36)
    row = "| {:2} | {:2} | {:2} | {:2} | {:2} | {:2} | "
    print(row.format("23", "24", "25", "26", "27", "28"))
    print("=" * 36)
def feb_leapyear_calendar():
    print("=" * 36)
    row = "| {:2} | {:2} | {:2} | {:2} | {:2} | {:2} | {:2} | "
    print(row.format("M", "T", "W", "T", "F", "S", "S"))
    print("-" * 36)
    print(row.format("01", "02", "03", "04", "05", "06", "07"))
    print("-" * 36)
    print(row.format("08", "09", "10", "12", "13", "14", "15"))
    print("-" * 36)
    print(row.format("16", "17", "18", "19", "20", "21", "22"))
    print("-" * 36)
    row = "| {:2} | {:2} | {:2} | {:2} | {:2} | {:2} | {:2} |"
    print(row.format("23", "24", "25", "26", "27", "28","29"))
    print("=" * 36)
def calendar30(): #Prints calendar for months with 30 days
    print("=" * 36)
    row = "| {:2} | {:2} | {:2} | {:2} | {:2} | {:2} | {:2} | "
    print(row.format("M", "T", "W", "T", "F", "S", "S"))
    print("-" * 36)
    print(row.format("01", "02", "03", "04", "05", "06", "07"))
    print("-" * 36)
    print(row.format("08", "09", "10", "12", "13", "14", "15"))
    print("-" * 36)
    print(row.format("16", "17", "18", "19", "20", "21", "22"))
    print("-" * 36)
    print(row.format("23", "24", "25", "26", "27", "28", "29"))
    print("-" * 36)
    row = "| {:2} | "
    print(row.format("30"))
    print("=" * 36)
def calendar31(): #Prints calendar for months with 31 days
    print("=" * 36)
    row = "| {:2} | {:2} | {:2} | {:2} | {:2} | {:2} | {:2} | "
    print(row.format("M", "T", "W", "T", "F", "S", "S"))
    print("-" * 36)
    print(row.format("01", "02", "03", "04", "05", "06", "07"))
    print("-" * 36)
    print(row.format("08", "09", "10", "12", "13", "14", "15"))
    print("-" * 36)
    print(row.format("16", "17", "18", "19", "20", "21", "22"))
    print("-" * 36)
    print(row.format("23", "24", "25", "26", "27", "28", "29"))
    print("-" * 36)
    row = "| {:2} | {:2} |"
    print(row.format("30", "31"))
    print("=" * 36)
def quit_moving_message(): #Goodbye message
    hyphens = ("\n" + '-'*50 + "\n") # skips one command line, prints 50 hyphens then skips another command line
    for l in hyphens:
        sys.stdout.write(l) #Prints hypens variable on screen
        sys.stdout.flush()
        time.sleep(0.008) #Time delay
    thanksmessage = ("Thank you for using RRD Finance LTD\nWe hope to see you again soon !\n\n")
    for l in thanksmessage:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.02)
    time.sleep(1.8)
    bye = ("Goodbye"+"\n\n")
    for l in bye:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.08)
