from django.db import IntegrityError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core.exceptions import ValidationError

from reg_users.models import Profile, Report, Language


def create_profile(request):
    if request.method == "POST":
        # try:
        try:
            profile = Profile()
            profile.first_name = request.POST.get("first_name")
            profile.last_name = request.POST.get("last_name")
            profile.telegram_link = request.POST.get("telegram_link")

        except IntegrityError:
            return HttpResponse(" Ваш телеграм профиль не уникален. Проверьте правильность написания.")
        try:
            profile.full_clean()


            # try:
            profile.save()
            print(profile.id)
            return HttpResponseRedirect(f"report/?profile_id={profile.id}")
        except ValidationError:
            return HttpResponse("Поля не должны быть пустыми")
    # except ValidationError:
    #     return HttpResponse("dwasdw")
    return render(request, "index.html")


def create_report(request):
    profile_id = request.GET.get("profile_id")
    prof = Profile.objects.filter(id=profile_id)
    for i in Profile.objects.filter(id=25):
        for r in i.reports.all():
            print(r.description)
    context = {"profile_id": profile_id}
    # print(Profile.reports.all())
    if request.method == "POST":
        report = Report()
        report.theme = request.POST.get("theme")
        report.description = request.POST.get("description")
        report.conclusion = request.POST.get("conclusion")
        report.what_learned = request.POST.get("what_learned")
        report.save()
        Language.objects.create(
            programming_language=request.POST.get("programming_language"),
            profile_id=int(profile_id),
            report_id=report.id
        )
        # language.programming_language = request.POST.get("programming_language")
        # language.profile = int(profile_id)
        # language.report = report.id
        # language.save()
        print(report.id)

    return render(request, "report.html", context)


def open_profile(request):
    if request.method == "POST":
        profile = Profile.objects.filter(
            telegram_link=request.POST.get("telegram_link"))
        for profil in profile:
            profile_id = profil.id
        if profile:
            # return HttpResponse("неправильный id")

            return HttpResponseRedirect(f"report/?profile_id={int(profile_id)}")
        else:
            return HttpResponse("неправильный id")

    return render(request, 'open_profile.html')
