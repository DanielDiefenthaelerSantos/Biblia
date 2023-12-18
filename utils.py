import requests
from time import sleep
from threading import Thread
from tkinter.ttk import Combobox
from tkinter import Tk, Toplevel

def checkConnection(req : dict | list):
    """
    Checks successful request.\n

    {param req} request to check.
    """
    if "msg" in req:
        print(req['msg'])
        return False
    else:
        return True

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
    
    if(checkConnection(response)):
        response = {
            "book": response['book']['name'],
            "chapter": response["chapter"],
            "number": response["number"],
            "text": response["text"]
        }
        return response
    else:
        return {"book": 'Gênesis', "chapter": 1, "number": 1, "text": 'No princípio criou Deus o céu e a terra.'}

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

    if(checkConnection(response)):
        for r in response:
            refined.append({"abbrev": r['abbrev']['pt'], "name": r['name'], "chapters": r['chapters']})
        
        return response
    else:
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
    if(checkConnection(response)):
        response = {
            "name": response['name'],
            "abbrev": response['abbrev']['pt'],
            "chapters": response["chapters"],
            "group": response["group"],
        }

        return response
    else:
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

    if(checkConnection(response)):
        response = response["verses"]
        return response
    else:
        return [{'number': 1, 'text': 'No princípio criou Deus o céu e a terra.'}, {'number': 2, 'text': 'E a terra era sem forma e vazia; e havia trevas sobre a face do abismo; e o Espírito de Deus se movia sobre a face das águas.'}, {'number': 3, 'text': 'E disse Deus: Haja luz; e houve luz.'}, {'number': 4, 'text': 'E viu Deus que era boa a luz; e fez Deus separação entre a luz e as trevas.'}, {'number': 5, 'text': 'E Deus chamou à luz Dia; e às trevas chamou Noite. E foi a tarde e a manhã, o dia primeiro.'}, {'number': 6, 'text': 'E disse Deus: Haja uma expansão no meio das águas, e haja separação entre águas e águas.'}, {'number': 7, 'text': 'E fez Deus a expansão, e fez separação entre as águas que estavam debaixo da expansão e as águas que estavam sobre a expansão; e assim foi.'}, {'number': 8, 'text': 'E chamou Deus à expansão Céus, e foi a tarde e a manhã, o dia segundo.'}, {'number': 9, 'text': 'E disse Deus: Ajuntem-se as águas debaixo dos céus num lugar; e apareça a porção seca; e assim foi.'}, {'number': 10, 'text': 'E chamou Deus à porção seca Terra; e ao ajuntamento das águas chamou Mares; e viu Deus que era bom.'}, {'number': 11, 'text': 'E disse Deus: Produza a terra erva verde, erva que dê semente, árvore frutífera que dê fruto segundo a sua espécie, cuja semente está nela sobre a terra; e assim foi.'}, {'number': 12, 'text': 'E a terra produziu erva, erva dando semente conforme a sua espécie, e a árvore frutífera, cuja semente está nela conforme a sua espécie; e viu Deus que era bom.'}, {'number': 13, 'text': 'E foi a tarde e a manhã, o dia terceiro.'}, {'number': 14, 'text': 'E disse Deus: Haja luminares na expansão dos céus, para haver separação entre o dia e a noite; e sejam eles para sinais e para tempos determinados e para dias e anos.'}, {'number': 15, 'text': 'E sejam para luminares na expansão dos céus, para iluminar a terra; e assim foi.'}, {'number': 16, 'text': 'E fez Deus os dois grandes luminares: o luminar maior para governar o dia, e o luminar menor para governar a noite; e fez as estrelas.'}, {'number': 17, 'text': 'E Deus os pôs na expansão dos céus para iluminar a terra,'}, {'number': 18, 'text': 'E para governar o dia e a noite, e para fazer separação entre a luz e as trevas; e viu Deus que era bom.'}, {'number': 19, 'text': 'E foi a tarde e a manhã, o dia quarto.'}, {'number': 20, 'text': 'E disse Deus: Produzam as águas abundantemente répteis de alma vivente; e voem as aves sobre a face da expansão dos céus.'}, {'number': 21, 'text': 'E Deus criou as grandes baleias, e todo o réptil de alma vivente que as águas abundantemente produziram conforme as suas espécies; e toda a ave de asas conforme a sua espécie; e viu Deus que era bom.'}, {'number': 22, 'text': 'E Deus os abençoou, dizendo: Frutificai e multiplicai-vos, e enchei as águas nos mares; e as aves se multipliquem na terra.'}, {'number': 23, 'text': 'E foi a tarde e a manhã, o dia quinto.'}, {'number': 24, 'text': 'E disse Deus: Produza a terra alma vivente conforme a sua espécie; gado, e répteis e feras da terra conforme a sua espécie; e assim foi.'}, {'number': 25, 'text': 'E fez Deus as feras da terra conforme a sua espécie, e o gado conforme a sua espécie, e todo o réptil da terra conforme a sua espécie; e viu Deus que era bom.'}, {'number': 26, 'text': 'E disse Deus: Façamos o homem à nossa imagem, conforme a nossa semelhança; e domine sobre os peixes do mar, e sobre as aves dos céus, e sobre o gado, e sobre toda a terra, e sobre todo o réptil que se move sobre a terra.'}, {'number': 27, 'text': 'E criou Deus o homem à sua imagem; à imagem de Deus o criou; homem e mulher os criou.'}, {'number': 28, 'text': 'E Deus os abençoou, e Deus lhes disse: Frutificai e multiplicai-vos, e enchei a terra, e sujeitai-a; e dominai sobre os peixes do mar e sobre as aves dos céus, e sobre todo o animal que se move sobre a terra.'}, {'number': 29, 'text': 'E disse Deus: Eis que vos tenho dado toda a erva que dê semente, que está sobre a face de toda a terra; e toda a árvore, em que há fruto que dê semente, ser-vos-á para mantimento.'}, {'number': 30, 'text': 'E a todo o animal da terra, e a toda a ave dos céus, e a todo o réptil da terra, em que há alma vivente, toda a erva verde será para mantimento; e assim foi.'}, {'number': 31, 'text': 'E viu Deus tudo quanto tinha feito, e eis que era muito bom; e foi a tarde e a manhã, o dia sexto.'}]

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
    if(checkConnection(response)):
        response = {
            "book": response['book']['name'],
            "chapter": response["chapter"],
            "number": response["number"],
            "text": response["text"]
        }

        return response
    else:
        return {'number': 1, 'text': 'No princípio criou Deus o céu e a terra.'}

def center(win : Tk | Toplevel):
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

def getAbbrev(book : str):
    """
    Returns the abbrev name of the book.\n

    {param book} book name.
    """
    array = [{'abbrev': "gn", 'name': 'Gênesis'}, {'abbrev': "ex", 'name': 'Êxodo'}, {'abbrev': "lv", 'name': 'Levítico'}, {'abbrev': "nm", 'name': 'Números'}, {'abbrev': "dt", 'name': 'Deuteronômio'}, {'abbrev': "js", 'name': 'Josué'}, {'abbrev': "jz", 'name': 'Juízes'}, {'abbrev': "rt", 'name': 'Rute'}, {'abbrev': "1sm", 'name': '1º Samuel'}, {'abbrev': "2sm", 'name': '2º Samuel'}, {'abbrev': "1rs", 'name': '1º Reis'}, {'abbrev': "2rs", 'name': '2º Reis'}, {'abbrev': "1cr", 'name': '1º Crônicas'}, {'abbrev': "2cr", 'name': '2º Crônicas'}, {'abbrev': "ed", 'name': 'Esdras'}, {'abbrev': "ne", 'name': 'Neemias'}, {'abbrev': "et", 'name': 'Ester'}, {'abbrev': "job", 'name': 'Jó'}, {'abbrev': "sl", 'name': 'Salmos'}, {'abbrev': "pv", 'name': 'Provérbios'}, {'abbrev': "ec", 'name': 'Eclesiastes'}, {'abbrev': "ct", 'name': 'Cânticos'}, {'abbrev': "is", 'name': 'Isaías'}, {'abbrev': "jr", 'name': 'Jeremias'}, {'abbrev': "lm", 'name': 'Lamentações de Jeremias'}, {'abbrev': "ez", 'name': 'Ezequiel'}, {'abbrev': "dn", 'name': 'Daniel'}, {'abbrev': "os", 'name': 'Oséias'}, {'abbrev': "jl", 'name': 'Joel'}, {'abbrev': "am", 'name': 'Amós'}, {'abbrev': "ob", 'name': 'Obadias'}, {'abbrev': "jn", 'name': 'Jonas'}, {'abbrev': "mq", 'name': 'Miquéias'}, {'abbrev': "na", 'name': 'Naum'}, {'abbrev': "hc", 'name': 'Habacuque'}, {'abbrev': "sf", 'name': 'Sofonias'}, {'abbrev': "ag", 'name': 'Ageu'}, {'abbrev': "zc", 'name': 'Zacarias'}, {'abbrev': "ml", 'name': 'Malaquias'}, {'abbrev': "mt", 'name': 'Mateus'}, {'abbrev': "mc", 'name': 'Marcos'}, {'abbrev': "lc", 'name': 'Lucas'}, {'abbrev': "jo", 'name': 'João'}, {'abbrev': "at", 'name': 'Atos'}, {'abbrev': "rm", 'name': 'Romanos'}, {'abbrev': "1co", 'name': '1ª Coríntios'}, {'abbrev': "2co", 'name': '2ª Coríntios'}, {'abbrev': "gl", 'name': 'Gálatas'}, {'abbrev': "ef", 'name': 'Efésios'}, {'abbrev': "fp", 'name': 'Filipenses'}, {'abbrev': "cl", 'name': 'Colossenses'}, {'abbrev': "1ts", 'name': '1ª Tessalonicenses'}, {'abbrev': "2ts", 'name': '2ª Tessalonicenses'}, {'abbrev': "1tm", 'name': '1ª Timóteo'}, {'abbrev': "2tm", 'name': '2ª Timóteo'}, {'abbrev': "tt", 'name': 'Tito'}, {'abbrev': "fm", 'name': 'Filemom'}, {'abbrev': "hb", 'name': 'Hebreus'}, {'abbrev': "tg", 'name': 'Tiago'}, {'abbrev': "1pe", 'name': '1ª Pedro'}, {'abbrev': "2pe", 'name': '2ª Pedro'}, {'abbrev': "1jo", 'name': '1ª João'}, {'abbrev': "2jo", 'name': '2ª João'}, {'abbrev': "3jo", 'name': '3ª João'}, {'abbrev': "jd", 'name': 'Judas'}, {'abbrev': "ap", 'name': 'Apocalipse'}]

    for item in array:
        if item['name'] == book:
            return item['abbrev']

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
                book = getBook(getAbbrev(cmb_book.get()))
                print("opa")
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
            if cmb_book.get() != last_book and cmb_chapter.get() != last_chapter:
                last_book = cmb_book.get()
                last_chapter = cmb_chapter.get()
                chapter = getChapter(getAbbrev(cmb_book.get()), cmb_chapter.get())
                print("opa")
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

    thread_book_chapter = Thread(target=bookChapterThread, args=(cmb_book, cmb_chapter))
    thread_chapter_verse = Thread(target=chapterVerseThread, args=(cmb_book, cmb_chapter, cmb_verse))
    thread_book_chapter.start()
    thread_chapter_verse.start()