import qrcode

def genQrCode(group_name):
    qr_content = "http://127.0.0.1:8000/join_group/" + group_name
    myqr = qrcode.make(qr_content)
    return myqr
