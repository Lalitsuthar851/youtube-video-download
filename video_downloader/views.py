from django.shortcuts import render
from django.http import HttpResponse
from pytube import YouTube
def home(request,
         ):
    if request.method == "POST":
        link = request.POST.get("link",
                                )
        type = request.POST.get("type",
                              )
        Video_quality = request.POST.get("quality",
                                         )
        print(type,Video_quality[:-1])
        print("Downloding...")

        # data=YouTube(str(link)).streams.filter(type=str(type)).first()
        # print(str(data)[-7:-2])

        if type == "audio":
            data = YouTube("https://www.youtube.com/watch?v=UnVyNh6P6FQ",
                           ).streams.get_highest_resolution()
            # YouTube(str(link)).streams.filter(type=str(type)).first().download()
            print(str(data)[41:51])
            print(str(data)[46:49])

            return render(request,
                          "download.html",
                          {"type":str(type).upper()},
                          )

        if type == "video":
            high_quality = YouTube(str(link)).streams.get_highest_resolution()
            print(high_quality)
            if int(Video_quality[:-1]) <= int(str(high_quality)[46:49]):
                # YouTube(str(link)).streams.filter(res=Video_quality).first().download()
                return render(request,
                              "download.html",
                              {"type":str(type).upper()},
                              )
            else:
                return HttpResponse("<script>alert('please select a lower quality')</script>")

    return render(request,
                  "index.html",
                  )

