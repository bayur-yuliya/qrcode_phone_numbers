import qrcode

def generate_qr_code(phone_number):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data("tel:" + phone_number)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white")

    qr_img.save("phone_number_qr_code.png")

    print("QR-код для номера телефона успешно создан и сохранен в файл 'phone_number_qr_code.png'.")


if __name__ == "__main__":
    phone_number = input("Введите номер телефона для создания QR-кода: ")
    generate_qr_code(phone_number)