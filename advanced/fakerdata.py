from faker import Factory


if __name__ == '__main__':
    fake = Factory().create('zh_CN')

    for i in range(10):
        print("{name}   {phone}     {address}   {email}"
              .format(name=fake.name(),
                      phone=fake.phone_number(),
                      address=fake.address(),
                      email=fake.email()
        ))


