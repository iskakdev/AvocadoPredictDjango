from django.shortcuts import render
from rest_framework import views, status
from rest_framework.response import Response
from .serializers import AvocadoSerializers
import joblib
import os
import numpy as np
from django.conf import settings

scaler_path = os.path.join(settings.BASE_DIR, 'scaler_avocado.pkl')
model_path = os.path.join(settings.BASE_DIR, 'log_model_avocado.pkl')

scaler = joblib.load(scaler_path)
model = joblib.load(model_path)

color_category = ['dark green', 'green', 'purple']

class AvocadoPredict(views.APIView):
    def post(self, request):
        serializer = AvocadoSerializers(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            new_color_category = data.get('color_category')
            color_category1or_0 = [1 if new_color_category == i else 0 for i in color_category]

            features = [data['firmness'], data['hue'], data['saturation'],
                        data['brightness'], data['sound_db'], data['weight_g'],
                        data['size_cm3']] + color_category1or_0
            scaled_data = scaler.transform([features])
            proba = model.predict_proba(scaled_data)[0]
            ripeness_map = ['hard', 'pre-conditioned', 'breaking', 'firm-ripe', 'ripe']
            pred_index = np.argmax(proba)
            return Response({
                "ripeness": ripeness_map[pred_index],
                "probability": round(float(proba[pred_index]), 2)
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
