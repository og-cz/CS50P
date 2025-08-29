from calculator import square

# pytest 02_pytest.py


def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
    assert square("cat")
    for i in range(0, 100):
        assert square(i) == (i * i)


# ============================================================ test session starts =============================================================
# platform win32 -- Python 3.13.5, pytest-8.4.1, pluggy-1.6.0
# rootdir: C:\Users\Asus\Documents\ogcz\_DEV\cs50p-journey\week5
# collected 0 items / 1 error

# =================================================================== ERRORS ===================================================================
# _______________________________________________________ ERROR collecting 02_pytest.py ________________________________________________________
# 02_pytest.py:1: in <module>
#     from calculator import square
# calculator.py:13: in <module>
#     main()
# calculator.py:2: in main
#     x = int(input("What's X? "))
#             ^^^^^^^^^^^^^^^^^^^
# C:\Users\Asus\AppData\Local\Programs\Python\Python313\Lib\site-packages\_pytest\capture.py:229: in read
#     raise OSError(
# E   OSError: pytest: reading from stdin while output is captured!  Consider using `-s`.
# -------------------------------------------------------------- Captured stdout ---------------------------------------------------------------
# What's X?
# ========================================================== short test summary info ===========================================================
# ERROR 02_pytest.py - OSError: pytest: reading from stdin while output is captured!  Consider using `-s`.
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ============================================================== 1 error in 0.14s ==============================================================
