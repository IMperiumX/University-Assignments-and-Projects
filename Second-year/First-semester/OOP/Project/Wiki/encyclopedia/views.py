from django.shortcuts import render, redirect
from django.urls import reverse
from markdown2 import markdown
from random import randint
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {"titles": util.list_entries()})


def entry(request, title):
    context = {"content": markdown(util.get_entry(title.strip())), "title": title}
    return render(request, "encyclopedia/entry.html", context)


def search(request):
    q = request.GET.get("q").strip()
    filenames = util.list_entries()
    search_result = [file for file in filenames if q in (file and file.lower())]
    if q in filenames:
        return redirect(reverse("entry", kwargs={"title": q}))
    return render(
        request, "encyclopedia/search.html", {"titles": search_result, "q": q}
    )


def create(request):
    if request.method != "POST":
        return render(request, "encyclopedia/create.html")
    title = request.POST.get("title").strip()
    content = request.POST.get("content").strip()
    if not (title or content):
        return render(
            request,
            "encyclopedia/create.html",
            {
                "message": "Can't be saved with empty fields!.",
                "title": title,
                "content": content,
            },
        )
    if title in util.list_entries():
        return render(
            request,
            "encyclopedia/create.html",
            {
                "message": "Be Creative! That Entry Exists.",
                "title": title,
                "content": content,
            },
        )
    util.save_entry(title, content)
    return redirect(reverse("entry", kwargs={"title": title}))


def edit(request, title):
    content = util.get_entry(title.strip())
    if content == "## Page was not found":
        return render(request, "encyclopedia/edit.html", {"error": content})

    if request.method == "POST":
        content = request.POST.get("content").strip()
        if content == "":
            return render(
                request,
                "encyclopedia/edit.html",
                {
                    "message": "Can't be saved with empty fields!.",
                    "title": title,
                    "content": content,
                },
            )
        util.save_entry(title, content)
        return redirect(reverse("entry", kwargs={'title': title}))
    return render(
        request, "encyclopedia/edit.html", {"content": content, "title": title}
    )


def random_page(request):
    Entries = util.list_entries()
    Choice = randint(0, len(Entries) - 1)
    title = Entries[Choice]
    content = markdown(util.get_entry(title))

    return render(
        request, "encyclopedia/random_page.html", {"content": content, "title": title}
    )
