def admin_menu(request):
    if not request.path.startswith("/admin_panel/"):
        return {}

    return {
        "menu_items": [
            {"title": "داشبورد", "url": "/admin_panel/", "icon": "home"},
            {"title": "دسته‌بندی‌ها", "url": "/admin_panel/categories", "icon": "tag"},
            {"title": "محصولات", "url": "/admin_panel/products", "icon": "box"},
        ]
    }
