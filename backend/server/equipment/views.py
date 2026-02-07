from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .models import EquipmentDataset
from .serializers import EquipmentDatasetSerializer
import pandas as pd
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from datetime import datetime


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_csv(request):
    file = request.FILES.get('file')
    df = pd.read_csv(file)

    total = len(df)
    avg_flow = df['Flowrate'].mean()
    avg_pressure = df['Pressure'].mean()
    avg_temp = df['Temperature'].mean()
    type_dist = df['Type'].value_counts().to_dict()

    EquipmentDataset.objects.create(
        total_count=total,
        avg_flowrate=avg_flow,
        avg_pressure=avg_pressure,
        avg_temperature=avg_temp
    )

    if EquipmentDataset.objects.count() > 5:
        EquipmentDataset.objects.first().delete()

    return Response({
        "total_count": total,
        "avg_flowrate": avg_flow,
        "avg_pressure": avg_pressure,
        "avg_temperature": avg_temp,
        "type_distribution": type_dist
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def history(request):
    data = EquipmentDataset.objects.order_by('-uploaded_at')[:5]
    serializer = EquipmentDatasetSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def generate_pdf(request):
    latest = EquipmentDataset.objects.last()

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    p = canvas.Canvas(response)
    p.setFont("Helvetica", 12)

    p.drawString(100, 800, "Chemical Equipment Report")
    p.drawString(100, 770, f"Generated on: {datetime.now()}")

    p.drawString(100, 730, f"Total Count: {latest.total_count}")
    p.drawString(100, 710, f"Avg Flowrate: {latest.avg_flowrate}")
    p.drawString(100, 690, f"Avg Pressure: {latest.avg_pressure}")
    p.drawString(100, 670, f"Avg Temperature: {latest.avg_temperature}")

    p.showPage()
    p.save()

    return response
