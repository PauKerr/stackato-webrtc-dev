from django.http import HttpResponse, FileResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from logs.models import LogCollection, LogFile

@csrf_exempt
def index(request):
    if request.method == 'GET':
        collection_list = LogCollection.objects.order_by('-received_on')
        return render(request, 'logs/index.html', {'collection_list': collection_list})

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
                                         filetype=(file_type or ''),
                                         content_type=(file.content_type or ''),
                                         char_set=(file.charset or ''),
                                         fileobj=file,
                                         )
        rsp_html = ('<a href="http://webrtc-dev.paas.allizom.org'
                    '/logs/%d">Log Collection</a>') % (collection.id)
        return HttpResponse(rsp_html)

def collection(request, collection_id):
    log_collection = get_object_or_404(LogCollection, pk=collection_id)
    return render(request, 'logs/collection.html',
                  {'collection': log_collection, 'file_list': log_collection.logfile_set.all()})

def file(request, file_id):
    log_file = get_object_or_404(LogFile, pk=file_id)
    try:
        response = FileResponse(log_file.fileobj)
        # Re-use recorded content-type, if available. Else, have FileResponse guess the type.
        if log_file.content_type:
            response['Content-Type'] = log_file.content_type
        response['Content-Disposition'] = 'attachment; filename=%s' % log_file.filename
    except IOError:
        return HttpResponseNotFound()
    return response

