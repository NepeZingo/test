from module import authentication

def test_validate():
    username = "jonathan"
    password = "anything"
    assert authentication.validate(username, password) == True
    assert authentication.validate("", password) == False 
    assert authentication.validate(username, "") == False

    username = "juan"
    assert authentication.validate(username, password) == False

