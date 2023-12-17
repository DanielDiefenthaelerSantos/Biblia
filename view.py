import tkinter as tk
import tkinter.ttk as ttk
from utils import randomVerse, getVerse, getBook, getBooks, getChapter, center, asyncCombobox

def verseWindow(root : object):
    """
    Change the main window to display a verse.\n

    {param root} the window to change.
    """
    for widget in root.winfo_children():
        widget.destroy()

    btn_back = ttk.Button(root, text="Voltar", command=lambda : generateMainButtons(root))
    btn_back.pack(anchor="nw", padx=5, pady=5)

    frm_choices = ttk.Frame(root)
    frm_choices.pack(expand=True)

    frm_select = ttk.Frame(frm_choices)
    frm_select.pack(side="top", expand=True)

    frm_confirm = ttk.Frame(frm_choices)
    frm_confirm.pack(side="top", expand=True)

    cmb_book = ttk.Combobox(frm_choices)
    cmb_book.pack(side="left", padx=10)
    
    cmb_chapter = ttk.Combobox(frm_choices)
    cmb_chapter.pack(side="left", padx=10)

    cmb_verse = ttk.Combobox(frm_choices)
    cmb_verse.pack(side="left", padx=10)

    books = getBooks()

    values_books = ["Selecione"]
    values_chapters = ["Selecione"]
    values_verses = ["Selecione"]

    asyncCombobox(cmb_book, cmb_chapter, cmb_verse)

    for book in books:
        values_books.append(book['name'])

    cmb_book['values'] = values_books
    cmb_chapter['values'] = values_chapters
    cmb_verse['values'] = values_verses
    cmb_book.current(0)
    cmb_chapter.current(0)
    cmb_verse.current(0)

def chapterWindow(root : object, book : str, chapter : str | int):
    """
    Change the main window to display the selected chapter.\n

    {param root} the window to change.\n
    {param book} the chapter book.\n
    {param chapter} the chapter number.
    """
    for widget in root.winfo_children():
        widget.destroy()

    btn_back = ttk.Button(root, text="Voltar", command=lambda : listChapterWindow(root, book))
    btn_back.pack(anchor="nw", padx=5, pady=5)

    verses = getChapter(book, chapter)

    main_frame = ttk.Frame(root)
    main_frame.pack(fill="both", expand=True)

    canva_verse = tk.Canvas(main_frame)
    canva_verse.pack(side="left", fill="both", expand=True)

    scroll_verses = ttk.Scrollbar(main_frame, orient="vertical", command=canva_verse.yview)
    scroll_verses.pack(side="right", fill="y")

    canva_verse.configure(yscrollcommand=scroll_verses.set)
    canva_verse.bind("<Configure>", lambda e: canva_verse.configure(scrollregion=canva_verse.bbox("all")))

    frm_verses = ttk.Frame(canva_verse)

    canva_verse.create_window((0, 0), window=frm_verses, anchor="nw")

    for verse in verses:
        lbn_number = ttk.Label(frm_verses, text=verse['number']).grid(row=(verse['number']-1), column=0, padx=5)
        lbn_text = ttk.Label(frm_verses, text=verse['text'], width=100, wraplength=700).grid(row=(verse['number']-1), column=1, pady=10)

def listChapterWindow(root : object, book : str):
    """
    Change the main window to display a chapter list of selected book.\n

    {param root} the window to change.\n
    {param book} the chapter book.
    """
    for widget in root.winfo_children():
        widget.destroy()

    btn_back = ttk.Button(root, text="Voltar", command=lambda : booksWindow(root))
    btn_back.pack(anchor="nw", padx=5, pady=5)

    info_book = getBook(book)

    frm_chapters = ttk.Frame(root)
    frm_chapters.pack(expand=True)

    buttons_list = []
    for chapter in range(1, (info_book['chapters'] + 1)):
        buttons_list.append(ttk.Button(frm_chapters, text=chapter, width=5, command=lambda abbrev = info_book['abbrev'], chapter = chapter: chapterWindow(root, abbrev, chapter)))

    row_cont = 0
    column_cont = 0
    if info_book['abbrev'] == "sl":
        for i in range(0, len(buttons_list)):
            buttons_list[i].grid(row=row_cont, column=column_cont, padx=5, pady=5)

            if column_cont == 11:
                column_cont = 0
                row_cont += 1
            else:
                column_cont += 1
    else:
        for i in range(0, len(buttons_list)):
            buttons_list[i].grid(row=row_cont, column=column_cont, padx=5, pady=5)

            if column_cont == 5:
                column_cont = 0
                row_cont += 1
            else:
                column_cont += 1

def booksWindow(root : object):
    """
    Change the main window to display the random verse.\n

    {param root} the window to change.
    """
    for widget in root.winfo_children():
        widget.destroy()

    books = getBooks()
    
    btn_back = ttk.Button(root, text="Voltar", command=lambda : generateMainButtons(root))
    btn_back.pack(anchor="nw", padx=5, pady=5)

    frm_books = ttk.Frame(root)
    frm_books.pack(expand=True)

    buttons_list = []

    for book in books:
        buttons_list.append(ttk.Button(frm_books, text=book['name'], width=20,command=lambda abbrev=book['abbrev']['pt']: listChapterWindow(root, abbrev)))

    row_cont = 0
    column_cont = 0
    for i in range(0, len(buttons_list)):
        buttons_list[i].grid(row=row_cont, column=column_cont, padx=5, pady=5)

        if column_cont == 5:
            column_cont = 0
            row_cont += 1
        else:
            column_cont += 1

def randomWindow(root : object):
    """
    Change the main window to display the random verse.\n

    {param root} the window to change.
    """
    for widget in root.winfo_children():
        widget.destroy()

    btn_back = ttk.Button(root, text="Voltar", command=lambda : generateMainButtons(root))
    btn_back.pack(anchor="nw", padx=5, pady=5)

    verse = randomVerse()

    frm_title = ttk.Frame(root)
    frm_title.pack(anchor="center")

    lbn_book = ttk.Label(frm_title, text=verse['book'], font=("-size", 30, "-weight", "bold"),)
    lbn_book.pack(padx=5, side="left")

    lbn_chapter = ttk.Label(frm_title, text=f"{verse['chapter']}:", font=("-size", 30, "-weight", "bold"),)
    lbn_chapter.pack(side="left")

    lbn_number = ttk.Label(frm_title, text=verse['number'], font=("-size", 30, "-weight", "bold"),)
    lbn_number.pack(side="left")

    lbn_verse = ttk.Label(root, text=verse['text'], wraplength=500, justify="center", font=("-size", 15))
    lbn_verse.pack(expand=True)

def generateMainButtons(root : object):
    """
    Generate initial buttons.\n

    {param root} the window for placing buttons.
    """
    for widget in root.winfo_children():
        widget.destroy()

    frm_buttons = ttk.Frame(root)
    frm_buttons.pack(expand=True)

    btn_books = ttk.Button(frm_buttons, width=20, text="Biblia", command=lambda : booksWindow(root))
    btn_verse = ttk.Button(frm_buttons, width=20, text="Procure um versículo", command=lambda : verseWindow(root))
    btn_random = ttk.Button(frm_buttons, width=20, text="Versículo aleatório", command=lambda : randomWindow(root))

    btn_books.pack(padx=5, pady=5)
    btn_verse.pack(padx=5, pady=5)
    btn_random.pack(padx=5, pady=5)

def root():
    """
    Create the main window.
    """
    root = tk.Tk()
    root.title("Python Bible")
    root.geometry("1100x600")
    center(root)

    root.tk.call("source", "./Azure-ttk-theme-main/azure.tcl")
    root.tk.call("set_theme", "dark")

    generateMainButtons(root)

    root.mainloop()

if __name__ == "__main__":
    root()