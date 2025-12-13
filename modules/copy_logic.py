def copy_to_clipboard(app, text_box):
    text = text_box.get("1.0", "end-1c")
    app.clipboard_clear()
    app.clipboard_append(text)