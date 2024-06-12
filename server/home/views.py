from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse as HttpJsonResponse
from django.views.decorators.csrf import csrf_exempt
import cv2
import numpy as np
import pandas as pd
import tensorflow as tf  # 2.13.0
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import load_model


map_dict = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F",
    16: "G",
    17: "H",
    18: "I",
    19: "J",
    20: "K",
    21: "L",
    22: "M",
    23: "N",
    24: "O",
    25: "P",
    26: "Q",
    27: "R",
    28: "S",
    29: "T",
    30: "U",
    31: "V",
    32: "W",
    33: "X",
    34: "Y",
    35: "Z",
    36: "a",
    37: "b",
    38: "d",
    39: "e",
    40: "f",
    41: "g",
    42: "h",
    43: "n",
    44: "q",
    45: "r",
    46: "t",
}


# Create your views here.
def home(request):
    return render(request, "home.html")


def call_model():
    model = load_model("models/my_model.h5")
    print(model.summary())
    return model


def process_image(image):
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Change size image: to 28x28
    resized_image = cv2.resize(gray_image, (28, 28))

    # Expand dimensions to fit input model
    processed_image = resized_image.reshape(1, 28, 28, 1)

    # Convert image to float 32
    processed_image = processed_image.astype("float32")

    return processed_image


@csrf_exempt
def get_image(request):
    if request.method == "POST":
        model = call_model()

        image_data = request.FILES["image"].read()
        nparr = np.frombuffer(image_data, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        processed_image = process_image(image)
        # print(processed_image.shape)
        prediction = model.predict(processed_image)
        top_5 = np.argsort(prediction[0])[:-6:-1]
        top_5_labels = [map_dict[i] for i in top_5]
        print(top_5_labels)
        print(f"Result: {top_5_labels[0]}")
        print(prediction)

        response_data = {"text_summary": top_5_labels[0]}

        return HttpJsonResponse(response_data)
