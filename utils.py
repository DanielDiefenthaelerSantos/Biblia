import requests
from time import sleep
from threading import Thread, Event
from tkinter.ttk import Combobox

def randomVerse():
    """
    Returns a dictionary with a random verse.\n

    {\n
        "book": "book name.",\n
        "chapter": "verse chapter.",\n
        "number": "the number of verses.",\n
        "text": "the text of the verse."\n
    }
    """
    response = requests.get("https://www.abibliadigital.com.br/api/verses/nvi/random")
    response = response.json()
    response = {
        "book": response['book']['name'],
        "chapter": response["chapter"],
        "number": response["number"],
        "text": response["text"]
    }
    return response

def getBooks():
    """
    Returns a list of dictionaries of all books.\n

    [\n
        {\n
            "abbrev": "abbrev of name book.",\n
            "name": "name of the book."\n
        },\n
        {...},\n
    ]
    """
    refined = []

    response = requests.get("https://www.abibliadigital.com.br/api/books")
    response = response.json()

    for r in response:
        refined.append({"abbrev": r['abbrev']['pt'], "name": r['name'], "chapters": r['chapters']})
    
    return response

    return [{'abbrev': {'pt': 'gn'}, 'name': 'Gênesis', 'chapters': 50}, {'abbrev': {'pt': 'ex'}, 'name': 'Êxodo', 'chapters': 40}, {'abbrev': {'pt': 'lv'}, 'name': 'Levítico', 'chapters': 27}, {'abbrev': {'pt': 'nm'}, 'name': 'Números', 'chapters': 36}, {'abbrev': {'pt': 'dt'}, 'name': 'Deuteronômio', 'chapters': 34}, {'abbrev': {'pt': 'js'}, 'name': 'Josué', 'chapters': 24}, {'abbrev': {'pt': 'jz'}, 'name': 'Juízes', 'chapters': 21}, {'abbrev': {'pt': 'rt'}, 'name': 'Rute', 'chapters': 4}, {'abbrev': {'pt': '1sm'}, 'name': '1º Samuel', 'chapters': 31}, {'abbrev': {'pt': '2sm'}, 'name': '2º Samuel', 'chapters': 24}, {'abbrev': {'pt': '1rs'}, 'name': '1º Reis', 'chapters': 22}, {'abbrev': {'pt': '2rs'}, 'name': '2º Reis', 'chapters': 25}, {'abbrev': {'pt': '1cr'}, 'name': '1º Crônicas', 'chapters': 29}, {'abbrev': {'pt': '2cr'}, 'name': '2º Crônicas', 'chapters': 36}, {'abbrev': {'pt': 'ed'}, 'name': 'Esdras', 'chapters': 10}, {'abbrev': {'pt': 'ne'}, 'name': 'Neemias', 'chapters': 13}, {'abbrev': {'pt': 'et'}, 'name': 'Ester', 'chapters': 10}, {'abbrev': {'pt': 'job'}, 'name': 'Jó', 'chapters': 42}, {'abbrev': {'pt': 'sl'}, 'name': 'Salmos', 'chapters': 150}, {'abbrev': {'pt': 'pv'}, 'name': 'Provérbios', 'chapters': 31}, {'abbrev': {'pt': 'ec'}, 'name': 'Eclesiastes', 'chapters': 12}, {'abbrev': {'pt': 'ct'}, 'name': 'Cânticos', 'chapters': 8}, {'abbrev': {'pt': 'is'}, 'name': 'Isaías', 'chapters': 66}, {'abbrev': {'pt': 'jr'}, 'name': 'Jeremias', 'chapters': 52}, {'abbrev': {'pt': 'lm'}, 'name': 'Lamentações de Jeremias', 'chapters': 5}, {'abbrev': {'pt': 'ez'}, 'name': 'Ezequiel', 'chapters': 48}, {'abbrev': {'pt': 'dn'}, 'name': 'Daniel', 'chapters': 12}, {'abbrev': {'pt': 'os'}, 'name': 'Oséias', 'chapters': 14}, {'abbrev': {'pt': 'jl'}, 'name': 'Joel', 'chapters': 3}, {'abbrev': {'pt': 'am'}, 'name': 'Amós', 'chapters': 9}, {'abbrev': {'pt': 'ob'}, 'name': 'Obadias', 'chapters': 1}, {'abbrev': {'pt': 'jn'}, 'name': 'Jonas', 'chapters': 4}, {'abbrev': {'pt': 'mq'}, 'name': 'Miquéias', 'chapters': 7}, {'abbrev': {'pt': 'na'}, 'name': 'Naum', 'chapters': 3}, {'abbrev': {'pt': 'hc'}, 'name': 'Habacuque', 'chapters': 3}, {'abbrev': {'pt': 'sf'}, 'name': 'Sofonias', 'chapters': 3}, {'abbrev': {'pt': 'ag'}, 'name': 'Ageu', 'chapters': 2}, {'abbrev': {'pt': 'zc'}, 'name': 'Zacarias', 'chapters': 14}, {'abbrev': {'pt': 'ml'}, 'name': 'Malaquias', 'chapters': 4}, {'abbrev': {'pt': 'mt'}, 'name': 'Mateus', 'chapters': 28}, {'abbrev': {'pt': 'mc'}, 'name': 'Marcos', 'chapters': 16}, {'abbrev': {'pt': 'lc'}, 'name': 'Lucas', 'chapters': 24}, {'abbrev': {'pt': 'jo'}, 'name': 'João', 'chapters': 21}, {'abbrev': {'pt': 'at'}, 'name': 'Atos', 'chapters': 28}, {'abbrev': {'pt': 'rm'}, 'name': 'Romanos', 'chapters': 16}, {'abbrev': {'pt': '1co'}, 'name': '1ª Coríntios', 'chapters': 16}, {'abbrev': {'pt': '2co'}, 'name': '2ª Coríntios', 'chapters': 13}, {'abbrev': {'pt': 'gl'}, 'name': 'Gálatas', 'chapters': 6}, {'abbrev': {'pt': 'ef'}, 'name': 'Efésios', 'chapters': 6}, {'abbrev': {'pt': 'fp'}, 'name': 'Filipenses', 'chapters': 4}, {'abbrev': {'pt': 'cl'}, 'name': 'Colossenses', 'chapters': 4}, {'abbrev': {'pt': '1ts'}, 'name': '1ª Tessalonicenses', 'chapters': 5}, {'abbrev': {'pt': '2ts'}, 'name': '2ª Tessalonicenses', 'chapters': 3}, {'abbrev': {'pt': '1tm'}, 'name': '1ª Timóteo', 'chapters': 6}, {'abbrev': {'pt': '2tm'}, 'name': '2ª Timóteo', 'chapters': 4}, {'abbrev': {'pt': 'tt'}, 'name': 'Tito', 'chapters': 3}, {'abbrev': {'pt': 'fm'}, 'name': 'Filemom', 'chapters': 1}, {'abbrev': {'pt': 'hb'}, 'name': 'Hebreus', 'chapters': 13}, {'abbrev': {'pt': 'tg'}, 'name': 'Tiago', 'chapters': 5}, {'abbrev': {'pt': '1pe'}, 'name': '1ª Pedro', 'chapters': 5}, {'abbrev': {'pt': '2pe'}, 'name': '2ª Pedro', 'chapters': 3}, {'abbrev': {'pt': '1jo'}, 'name': '1ª João', 'chapters': 5}, {'abbrev': {'pt': '2jo'}, 'name': '2ª João', 'chapters': 1}, {'abbrev': {'pt': '3jo'}, 'name': '3ª João', 'chapters': 1}, {'abbrev': {'pt': 'jd'}, 'name': 'Judas', 'chapters': 1}, {'abbrev': {'pt': 'ap'}, 'name': 'Apocalipse', 'chapters': 22}]

def getBook(book : str):
    """
    Returns a dictionary with the selected book.\n

    {param book} abbreviated book name.\n

    {\n
        "name": "book name.",\n
        "abbrev": "abbreviated name of the book.",\n
        "chapters": "number of chapters in the book.",\n
        "group": "the book group"\n
    }
    """

    response = requests.get(f"https://www.abibliadigital.com.br/api/books/{book}")
    response = response.json()
    response = {
        "name": response['name'],
        "abbrev": response['abbrev']['pt'],
        "chapters": response["chapters"],
        "group": response["group"],
    }

    return response

    return {'name': 'Gênesis', 'abbrev': 'gn', 'chapters': 50, 'group': 'Pentateuco'}

def getChapter(book : str, chapter : str | int):
    """
    Returns a dictionary list with all verses from a selected chapter.\n
    
    {param book} chapter abbreviated book name.\n
    {param chapter} chapter number.\n

    [\n
        {\n
            "number": "the number of verse.",\n
            "text": "the text of the verse."\n
        },\n
        {...},\n
    ]
    """
    response = requests.get(f"https://www.abibliadigital.com.br/api/verses/nvi/{book}/{chapter}")
    response = response.json()
    response = response["verses"]

    return response

    return [{'number': 1, 'text': 'Quando os homens começaram a multiplicar-se na terra e lhes nasceram filhas,'}, {'number': 2, 'text': 'os filhos de Deus viram que as filhas dos homens eram bonitas e escolheram para si aquelas que lhes agradaram.'}, {'number': 3, 'text': 'Então disse o Senhor: "Por causa da perversidade do homem, meu Espírito não contenderá com ele para sempre; e ele só viverá cento e vinte anos".'}, {'number': 4, 'text': 'Naqueles dias havia nefilins na terra, e também posteriormente, quando os filhos de Deus possuíram as filhas dos homens e elas lhes deram filhos. Eles foram os heróis do passado, homens famosos.'}, {'number': 5, 'text': 'O Senhor viu que a perversidade do homem tinha aumentado na terra e que toda a inclinação dos pensamentos do seu coração era sempre e somente para o mal.'}, {'number': 6, 'text': 'Então o Senhor arrependeu-se de ter feito o homem sobre a terra; e isso cortou-lhe o coração.'}, {'number': 7, 'text': 'Disse o Senhor: "Farei desaparecer da face da terra o homem que criei, os homens e também os animais grandes, os animais pequenos e as aves do céu. Arrependo-me de havê-los feito".'}, {'number': 8, 'text': 'A Noé, porém, o Senhor mostrou benevolência.'}, {'number': 9, 'text': 'Esta é a história da família de Noé: Noé era homem justo, íntegro entre o povo da sua época; ele andava com Deus.'}, {'number': 10, 'text': 'Noé gerou três filhos: Sem, Cam e Jafé.'}, {'number': 11, 'text': 'Ora, a terra estava corrompida aos olhos de Deus e cheia de violência.'}, {'number': 12, 'text': 'Ao ver como a terra se corrompera, pois toda a humanidade havia corrompido a sua conduta,'}, {'number': 13, 'text': 'Deus disse a Noé: "Darei fim a todos os seres humanos, porque a terra encheu-se de violência por causa deles. Eu os destruirei juntamente com a terra.'}, {'number': 14, 'text': 'Você, porém, fará uma arca de madeira de cipreste; divida-a em compartimentos e revista-a de piche por dentro e por fora.'}, {'number': 15, 'text': 'Faça-a com cento e trinta e cinco metros de comprimento, vinte e dois metros e meio de largura e treze metros e meio de altura.'}, {'number': 16, 'text': 'Faça-lhe um teto com um vão de quarenta e cinco centímetros entre o teto e corpo da arca. Coloque uma porta lateral na arca e faça um andar superior, um médio e um inferior.'}, {'number': 17, 'text': '"Eis que vou trazer águas sobre a terra, o Dilúvio, para destruir debaixo do céu toda criatura que tem fôlego de vida. Tudo o que há na terra perecerá.'}, {'number': 18, 'text': 'Mas com você estabelecerei a minha aliança, e você entrará na arca com seus filhos, sua mulher e as mulheres de seus filhos.'}, {'number': 19, 'text': 'Faça entrar na arca um casal de cada um dos seres vivos, macho e fêmea, para conservá-los vivos com você.'}, {'number': 20, 'text': 'De cada espécie de ave, de cada espécie de animal grande e de cada espécie de animal pequeno que se move rente ao chão virá um casal a você para que sejam conservados vivos.'}, {'number': 21, 'text': 'E armazene todo tipo de alimento, para que você e eles tenham mantimento".'}, {'number': 22, 'text': 'Noé fez tudo exatamente como Deus lhe tinha ordenado.'}]

def getVerse(book : str, chapter : str | int, verse : str | int):
    """
    Returns a dictionary with the selected verse.\n

    {param book} verse abbreviated book name.\n
    {param chapter} verse chapter.\n
    {param verse} verse number.\n

    {\n
        "book": "book name.",\n
        "chapter": "verse chapter.",\n
        "number": "the number of verses.",\n
        "text": "the text of the verse."\n
    }
    """    
    response = requests.get(f"https://www.abibliadigital.com.br/api/verses/nvi/{book}/{chapter}/{verse}")
    response = response.json()
    response = {
        "book": response['book']['name'],
        "chapter": response["chapter"],
        "number": response["number"],
        "text": response["text"]
    }

    return response

    return {'book': 'Gênesis', 'chapter': 6, 'number': 6, 'text': 'Então o Senhor arrependeu-se de ter feito o homem sobre a terra; e isso cortou-lhe o coração.'}

def center(win):
    """
    Centers a tkinter window.\n

    {param win} the main window or Toplevel window to center.
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

def bookChapterThread(cmb_book : Combobox, cmb_chapter : Combobox):
    """
    Prepare a function to use per a thread in checkBook().\n

    {param cmb_book} the Combobox to check.\n
    {param cmb_chapter} the Combobox to alter.
    """
    last = "Selecione"
    array_aux = []
    while True:
        sleep(1)
        try:
            if cmb_book.get() != last:
                last = cmb_book.get()
                book = getBook(cmb_book.get())
                for i in range(1, book['chapters']+1):
                    array_aux.append(i)
                cmb_chapter['values'] = array_aux
        except:
            break

def chapterVerseThread(cmb_book : Combobox, cmb_chapter : Combobox, cmb_verse : Combobox):
    """
    Prepare a function to use per a thread in checkBook().\n

    {param cmb_chapter} the Combobox to check.
    {param cmb_verse} the Combobox to alter.\n
    """
    last_book = "Selecione"
    last_chapter = "Selecione"
    array_aux = []
    while True:
        sleep(1)
        try:
            if cmb_book.get() != last_book or cmb_chapter.get() != last_chapter:
                last_book = cmb_book.get()
                last_chapter = cmb_chapter.get()
                chapter = getChapter(cmb_book.get(), cmb_chapter.get())
                for i in range(len(chapter)+1):
                    array_aux.append(i)
                cmb_verse['values'] = array_aux
        except:
            break

def asyncCombobox(cmb_book : Combobox, cmb_chapter : Combobox, cmb_verse : Combobox):
    """
    Uses Thread to check the Combobox value.\n

    {param cmb_book} the Combobox to check.\n
    {param cmb_chapter} the Combobox to check/alter.\n
    {param cmb_verse} the Combobox to alter.
    """

    threadA = Thread(target=bookChapterThread, args=(cmb_book, cmb_chapter))
    threadB = Thread(target=chapterVerseThread, args=(cmb_book, cmb_chapter, cmb_verse))
    threadA.start()
    threadB.start()