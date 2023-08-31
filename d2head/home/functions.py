def handle_uploaded_file(f):
    with open('d2head/static/upload'+f.name,'wb+')as destination:
        for chunk in f.chunks():
            destination.write(chunk)
