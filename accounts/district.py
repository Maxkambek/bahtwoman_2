from rest_framework.response import Response
from rest_framework.views import APIView
import pandas as pd
from accounts.models import District


class CityCreateView(APIView):

    def post(self, request):
        file = request.data.get("file")
        rd = pd.read_csv(f"{file}")
        df = pd.DataFrame(rd)

        for row in df.itertuples():
            District.objects.create(
                region_id=row[2],
                name_uz=row[3],
                name_ky=row[4]
            )
        return Response('success')
