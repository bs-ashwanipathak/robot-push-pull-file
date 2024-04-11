try:
    from robot.libraries.BuiltIn import BuiltIn
    from robot.libraries.BuiltIn import _Misc
    import robot.api.logger as logger
    from robot.api.deco import keyword
    ROBOT = False
except Exception:
    ROBOT = False

@keyword("IOSPUSH FILE")
def iospushfile():
     driver = BuiltIn().get_library_instance('AppiumLibrary')._current_application()
     driver.push_file('@com.google.chrome.ios:documents/image1.png', source_path='/path/to/local/file.jpg')

@keyword("IOSPULL FILE")
def iospullfile():
     driver = BuiltIn().get_library_instance('AppiumLibrary')._current_application()
     driver.pull_file("@com.google.chrome.ios:documents/image1.png")
