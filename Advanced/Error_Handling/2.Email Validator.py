from Custum_Exeptions import MustContainAtSymbolError, NameTooShortError, InvalidDomainError

while True:
    line = input()
    if line == "End":
        break
    valid_domains = {".com", ".bg", ".org", ".net"}
    email = line
    email_parts = email.split("@")

    if len(email_parts) != 2:
        raise MustContainAtSymbolError("Email must contain @")

    name, dom = email_parts

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    domain = f".{dom.split('.')[-1]}"

    if domain not in valid_domains:
        raise InvalidDomainError(f"Domain must be one of the following: {','.join(valid_domains)}")

    print("Email is valid")