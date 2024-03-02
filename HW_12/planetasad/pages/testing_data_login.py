def data_login(data):
    for i, l in enumerate(data):
        data[i] = (l['sign_in_email_inp'], l['sign_in_pwd_inp'])
    return data


test_cases = [
    {
        "sign_in_email_inp": "none",
        "sign_in_pwd_inp": "none",
    },
    {
        "sign_in_email_inp": "biohazard138akasa@rambler.ru",
        "sign_in_pwd_inp": "Q32sM_4",
    },

]
