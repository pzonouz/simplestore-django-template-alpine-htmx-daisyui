from django.shortcuts import render


def home(request):
    menu_items = [
        {"title": "صفحه نخست", "url": "/"},
        {
            "title": "مواد شیمیایی",
            "children": [
                {"title": "کلیه مواد شیمیایی", "url": "/chemicals"},
                {"title": "مواد آزمایشگاهی", "url": "/lab-materials"},
                {
                    "title": "مواد زیستی",
                    "children": [
                        {
                            "title": "محیط کشت",
                            "children": [
                                {
                                    "title": "محیط کشت میکروبی",
                                    "url": "/microbial-culture",
                                },
                                {"title": "محیط کشت سلولی", "url": "/cell-culture"},
                            ],
                        }
                    ],
                },
            ],
        },
    ]
    return render(request, "pages/main/home.django", context={"menu_items": menu_items})
