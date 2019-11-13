from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Blotter
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, JSONParser, FormParser, MultiPartParser

# Create your views here.


class BlotterView(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    #parser_classes = [FormParser, MultiPartParser]

    def get(self, request, format=None):
        blotter = Blotter.objects.all().order_by('-reporting_datetime')
	    #serializer_class = SightingSerializer
        #serializer = BlotterSerializer(blotter, many=True)
        #return Response(serializer.data)

        return Response({"message": "Hello, world!"})



	#def post(self, request, format=None)
		#sighting = SightingSerializer(data=request)
		#sighting.is_valid()
		# True
		#sighting.validated_data
		# OrderedDict([('title', ''), ('code', 'print("hello, world")\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
		#sighting_saved = sighting.save()
		# <Snippet: Snippet object>
		#return Response({sighting_id: sighting_saved.sighting_id})



    def post(self, request, format=None):
        #serializer = BlotterSerializer(email=request.POST["email"], accident_type=request.POST["accident_type"], kill_type=request.POST["kill_type"], group_type=request.POST["group_type"], sex=request.POST["sex"])
        
        #data = {"email": request.POST["email"], "observation_type": request.POST["observation_type"], "accident_type": request.POST["accident_type"], "group_type": request.POST["group_type"], "kill_type": request.POST["kill_type"], "cause_of_death": "cd", "sex": request.POST["sex"], "user_note": request.POST["user_note"], "number_of_tuskers": request.POST["number_of_tuskers"], "number_of_tots": request.POST["number_of_tots"], "location_point": [request.POST["latitude"], request.POST["longitude"]], "admin_comment": request.POST["admin_comment"], "admin_rating": request.POST["admin_rating"], "display": "ad", "sighting_datetime": datetime.datetime.utcnow()}

        #serializer = BlotterSerializer(data=data)
        #serializer = BlotterSerializer(data=request.POST)

        #contents = request.FILES["photo"].file

        #print(request.body)
        #print(str(request.FILES["file"]))
        #print(serializer.is_valid())
        #print(serializer.errors)
        #print(serializer.data)

        #print(request.FILES["photo"].filename)

		# True
		#serializer.validated_data
		# OrderedDict([('title', ''), ('code', 'print("hello, world")\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
		#serializer.save()
		# <Snippet: Snippet object>

        #size = 128, 128
        #temp = BytesIO()

        #im = Image.open(contents)
        #im.thumbnail(size)
	    #im.save(file.filename, "JPEG")
        #im.save(temp, format="JPEG")
	    #seek
        #temp.seek(0)


	    #s3
        #client_s3 = boto3.client('s3')

	    #jwt
	    #current_user = get_jwt_identity()
	    
        #client_s3.upload_fileobj(
        #    temp, # This is what i am trying to upload
        #    "trunksnleaves",
        #    "static/test_file.jpg",
        #    ExtraArgs={
        #        'ACL': 'public-read',
        #        "ContentType": 'image/jpeg'
        #    }
        #)

        #if serializer.is_valid():
        #    serializer.save()
        #    return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({"serializer.data1": "data"})

        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

