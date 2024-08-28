from uia import note
obj = note()

def test_edit():
    obj.open_npd()
    obj.new_file()
    obj.edit()
    obj.close_npd()

def test_font():
    obj.open_npd()
    obj.edit()
    obj.font()
    obj.close_npd()

def test_find():
    obj.open_npd()
    obj.edit()
    obj.find()
    obj.close_npd()

def test_replace():
    obj.open_npd()
    obj.edit()
    obj.replace()
    obj.close_npd()

def test_time():
    obj.open_npd()
    obj.time()
    obj.close_npd()

def test_select_delete():
    obj.open_npd()
    obj.edit()
    obj.select_all()
    obj.close_npd()

def test_view():
    obj.open_npd()
    obj.edit()
    obj.view()
    obj.close_npd()

def test_about():
    obj.open_npd()
    obj.about()
    obj.close_npd()

def test_pagesetup():
    obj.open_npd()
    obj.pagesetup()
    obj.close_npd()

def test_prrint():
    obj.open_npd()
    obj.edit()
    obj.print()
    obj.close_npd()

def test_save_as():
    obj.open_npd()
    obj.edit()
    obj.saveas()
    obj.close_npd()

def test_open():
    obj.open_npd()
    obj.open()

