from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from logs.models import LogCollection, LogFile

@csrf_exempt
def index(request):
    if request.method == 'GET':
        return HttpResponse('WebRTC Log Collection Server')
    elif request.method == 'POST':
        collection = LogCollection(
                         description=request.POST.get('Description')
                     )
        collection.save()

        for file_group in request.FILES.lists():
            file_type = file_group[0]
            for file in file_group[1]:
              collection.logfile_set.create(
                                         filename=file.name,
                                         filetype=file_type,
                                         fileobj=file
                                     )
        rsp_html = '<a href="http://webrtc-dev.paas.allizom.org/logs/%d">Log Collection</a>' % (collection.id)
        return HttpResponse(rsp_html)


